import sys
sys.path.append("./videomaev2")

import numpy as np
import torch
import os
from timm.models import create_model
from torchvision import transforms

# NOTE: Do not comment `import models`, it is used to register models
import models  # noqa: F401
from dataset.loader import get_video_loader

from tqdm import tqdm
import pickle


def to_normalized_float_tensor(vid):
    return vid.permute(3, 0, 1, 2).to(torch.float32) / 255

# NOTE: for those functions, which generally expect mini-batches, we keep them
# as non-minibatch so that they are applied as if they were 4d (thus image).
# this way, we only apply the transformation in the spatial domain
def resize(vid, size, interpolation='bilinear'):
    # NOTE: using bilinear interpolation because we don't work on minibatches
    # at this level
    scale = None
    if isinstance(size, int):
        scale = float(size) / min(vid.shape[-2:])
        size = None
    return torch.nn.functional.interpolate(
        vid,
        size=size,
        scale_factor=scale,
        mode=interpolation,
        align_corners=False)

class ToFloatTensorInZeroOne(object):
    def __call__(self, vid):
        return to_normalized_float_tensor(vid)


class Resize(object):
    def __init__(self, size):
        self.size = size

    def __call__(self, vid):
        return resize(vid, self.size)

def get_start_idx_range():
    def medtal_range(num_frames):
        return range(0, num_frames - 15, 16)
    
    return medtal_range

def load_backbone_model(backbone_cfgs):
    model_type, ckpt_path, gpu = backbone_cfgs['model_type'], backbone_cfgs['ckpt_path'], backbone_cfgs['gpu_id']
    device = torch.device("cuda:{}".format(gpu) if torch.cuda.is_available() else "cpu")
    # get model & load ckpt
    model = create_model(
        model_type,
        img_size=224,
        pretrained=False,
        num_classes=710,
        all_frames=16,
        tubelet_size=2,
        drop_path_rate=0.3,
        use_mean_pooling=True)
    print("=> loading checkpoint '{}'".format(ckpt_path))
    ckpt = torch.load(ckpt_path, map_location='cpu')
    for model_key in ['model', 'module']:
        if model_key in ckpt:
            ckpt = ckpt[model_key]
            break
    model.load_state_dict(ckpt)
    model.eval()
    model = model.to(device)
    return model, device

def extract_feature_video(model, device, video_path, feat_cache_path):
    if not os.path.exists(feat_cache_path):
        os.makedirs(feat_cache_path)
    
    video_loader = get_video_loader()
    start_idx_range = get_start_idx_range()
    transform = transforms.Compose(
        [ToFloatTensorInZeroOne(),
         Resize((224, 224))])

    vid_name = video_path.split('/')[-1][:-4]
    url = os.path.join(feat_cache_path, vid_name + ".pkl")
    if os.path.exists(url):
        # if cached, read directly
        f = open(url, 'rb')
        vid_feature = pickle.load(f)
        f.close()
    else:
        # extract
        vr = video_loader(video_path)
        feature_list = []
        for start_idx in start_idx_range(len(vr)):
            print("[Extracting features:{},{}/{}]".format(vid_name, start_idx, len(vr)), end="\r")
            data = vr.get_batch(np.arange(start_idx, start_idx + 16)).asnumpy()
            frame = torch.from_numpy(data)  # torch.Size([16, 566, 320, 3])
            frame_q = transform(frame)  # torch.Size([3, 16, 224, 224])
            input_data = frame_q.unsqueeze(0).to(device)
            with torch.no_grad():
                feature = model.forward_features(input_data)
                feature_list.append(feature.cpu().numpy())
        vid_feature = np.vstack(feature_list)
        with open(url, 'wb') as pkl_file:
            pickle.dump(vid_feature, pkl_file)
    
    return vid_feature

if __name__ == '__main__':
    backbone_cfgs = {
        "gpu_id": 0,
        "model_type": 'vit_giant_patch14_224',
        "ckpt_path": './ckpt/vit_g_hybrid_pt_1200e_k710_ft.pth'
        }
    video_path = "../data/videos/puToJ78AXcE.mp4"
    model, device = load_backbone_model(backbone_cfgs)
    vid_feature = extract_feature_video(model, device, video_path, feat_cache_path = "../data/features")
    print(vid_feature.shape)