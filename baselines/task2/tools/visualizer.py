# >> visualize in phase detection
## visualize in figure
import pickle
import json
import os
import numpy as np
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def get_trainval_list(gt_path):
    with open(gt_path, 'r', encoding='gbk') as f:
        gt_dict = json.load(f)
        gt_dict = gt_dict['database']

    train_list, val_list = [], []
    for vid in gt_dict.keys():
        if gt_dict[vid]['subset'] in ['test']:
            val_list.append(vid)
        elif gt_dict[vid]['subset'] in ['train']:
            train_list.append(vid)
        else:
            print('Unkown Subset:{}'.format(gt_dict[vid]['subset']))

    return train_list, val_list

def segment_iou(target_segment, candidate_segments):
    """Compute the temporal intersection over union between a
    target segment and all the test segments.

    Parameters
    ----------
    target_segment : 1d array
        Temporal target segment containing [starting, ending] times.
    candidate_segments : 2d array
        Temporal candidate segments containing N x [starting, ending] times.

    Outputs
    -------
    tiou : 1d array
        Temporal intersection over union score of the N's candidate segments.
    """
    tt1 = np.maximum(target_segment[0], candidate_segments[:, 0])
    tt2 = np.minimum(target_segment[1], candidate_segments[:, 1])
    # Intersection including Non-negative overlap score.
    segments_intersection = (tt2 - tt1).clip(0)
    # Segment union.
    segments_union = (candidate_segments[:, 1] - candidate_segments[:, 0]) \
      + (target_segment[1] - target_segment[0]) - segments_intersection
    # Compute overlap as the ratio of the intersection
    # over union of two segments.
    tIoU = segments_intersection.astype(float) / segments_union
    return tIoU

def match_gtbox(preds, gt):
    pred_box={}
    for cla,pred in preds.items():
        if cla not in gt.keys():
            continue
        pred_box[cla]=[]
        lock_gt=np.ones(len(gt[cla]))
        for seg in pred:
            iou=segment_iou(np.array(seg[0:2]),np.array(gt[cla]))
            match_gt=np.argmax(iou)
            if lock_gt[match_gt]>0:
                pred_box[cla].append(seg)
                lock_gt[match_gt]=0
    return pred_box

def main(gt_path, result_dir, output_dir, plt_type='segment', min_score=0.4):
    '''
    plt_type ('proposal', 'segment')
    '''
    # >> load gt and detection results
    with open(gt_path, 'r', encoding='gbk') as f:
        gt_dict = json.load(f)
        gt_db = gt_dict['database']
    _, val_list = get_trainval_list(gt_path)

    if os.path.exists(result_dir):
        print("Loading Successfuly")
        with open(result_dir, 'rb') as f:
            det_results = pickle.load(f)
    det_results=pd.DataFrame(det_results)

    colors = plt.cm.tab20.colors[:20]
    val_list = val_list[0:50]
    for vid in tqdm(val_list, total=len(val_list)):
        vid_gt = gt_db[vid]
        vid_det = det_results[det_results['video-id'] == vid]

        # process gt
        box_gt={} #sort by class
        for gt in vid_gt['annotations']:
            label = int(gt['label_id'])
            if label not in box_gt.keys():
                box_gt[label]=[]
            box_gt[label].append(gt['segment'])

        # process pred
        box_pred = {}
        for index, pred in vid_det.iterrows():
            if pred['label'] not in box_pred.keys():
                box_pred[pred['label']] = []
            box_pred[pred['label']].append([pred['t-start'], pred['t-end'], pred['score']])

        
        if plt_type == 'proposal':
            fig = plt.figure(figsize=(8, 4))
            # plot gt 
            for anno in vid_gt['annotations']:
                plt.plot(anno['segment'], [1.1]*2,'o-', color=colors[anno['label_id']%len(colors)], linewidth=1, markersize=1)
            # plot preds
            for c in box_pred.keys():
                for pred in box_pred[c]:
                    if pred[2] > min_score:
                        plt.plot([pred[0], pred[1]], [pred[2]]*2,'o-', color=colors[c%len(colors)], linewidth=1, markersize=1)
            plt.title(vid)
            plt.xlabel('Time(s)')
            plt.ylabel('Conf.')
            # output_dir='./outputs/vis_results_matched(prop)'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

        elif plt_type == 'segment':
            # match gt
            box_pred = match_gtbox(box_pred, box_gt)

            gs = gridspec.GridSpec(2, 1, wspace=0.3, hspace=0.3)
            fig = plt.figure()
            fig.set_size_inches((10,1))

            #plot gt
            gt_ax = fig.add_subplot(gs[0,0])
            for anno in vid_gt['annotations']:
                s, e = anno['segment']
                gt_ax.add_patch(plt.Rectangle(xy=(int(s),0),width=int(e)-int(s),
                                    height=1,fill=True,color=colors[anno['label_id']%len(colors)],alpha=1))
            
            gt_ax.set_xticks([])
            gt_ax.set_yticks([])
            gt_ax.set_ylabel('GT')
            gt_ax.set_xlim(0, vid_gt['duration'])
            gt_ax.set_title(vid)

            #plot pred
            pred_ax = fig.add_subplot(gs[1,0])
            tmp_preds = []
            for c in box_pred.keys():
                for pred in box_pred[c]:
                    tmp_preds.append(pred + [c])
            sorted_preds = sorted(tmp_preds, key=lambda x: x[2])
            for pred in sorted_preds:
                s, e, score, c = pred
                pred_ax.add_patch(plt.Rectangle(xy=(int(s),0),width=int(e)-int(s),
                                    height=1,fill=True,color=colors[c%len(colors)],alpha=1))
            pred_ax.set_xticks([])
            pred_ax.set_yticks([])
            pred_ax.set_ylabel('Loc.')
            pred_ax.set_xlim(0, vid_gt['duration'])

            # output_dir='./outputs/vis_results_matched(seg)'
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

        else:
            print("Unrecognized mode")
            continue

        plt.savefig(os.path.join(output_dir, vid+'.png'), dpi=400, bbox_inches='tight')
        plt.close()

if __name__ == '__main__':
    plt_type = 'segment'
    gt_path = '../dataset/tal_annotations/OphNet2024_phase.json'
    result_dir = '../talnets/TriDet/ckpt/medical_videomae_phase_baseline/eval_results.pkl'
    output_dir = './outputs/videomae_phase_{}'.format(plt_type)
    main(gt_path, result_dir, output_dir, plt_type)

    # plt_type = 'proposal'
    # gt_path = '../dataset/tal_annotations/OphNet2024_operation.json'
    # result_dir = '../talnets/TriDet/ckpt/medical_videomae_operation_baseline/eval_results.pkl'
    # output_dir = './outputs/videomae_operation_{}'.format(plt_type)
    # main(gt_path, result_dir, output_dir, plt_type)

    
