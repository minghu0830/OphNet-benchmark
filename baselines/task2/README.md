
## Baseline Experiment Results

### Test split
#### Phase-level 

| Method |  Backbone | IoU@0.3 | IoU@0.4 | IoU@0.5 | IoU@0.6 | IoU@0.7 | AVG mAP[0.3:0.1:0.7] |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|ActionFormer|CSN|30.94|28.62|25.13|20.59|14.10|23.88|
|ActionFormer|SlowFast|32.61|30.09|25.04|19.22|14.95|24.38|
|ActionFormer|SwinViviT|37.62|34.14|28.79|23.49|16.72|28.15|	
|ActionFormer|VideoMAEv2|46.74|44.03|39.74|33.38|25.94|37.97|	
|TriDet|CSN|33.60|30.57|26.43|22.12|17.09|25.96|
|TriDet|SlowFast|35.49|32.83|28.24|23.91|16.99|27.49|
|TriDet|SwinViviT|37.73|33.73|29.12|23.98|17.82|28.48|
|**TriDet**|**VideoMAEv2**|**48.52**|**45.68**|**42.62**|**36.96**|**30.74**|**40.91**|

#### Operation-level

| Method |  Backbone | IoU@0.3 | IoU@0.4 | IoU@0.5 | IoU@0.6 | IoU@0.7 | AVG mAP[0.3:0.1:0.7] |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|ActionFormer|CSN|28.32|25.93|22.01|17.24|12.69|21.24|
|ActionFormer|SlowFast|32.50|29.74|25.89|20.19|15.33|24.73|
|ActionFormer|SwinViviT|33.36|30.74|27.31|21.08|15.39|25.57|
|ActionFormer|VideoMAEv2|44.94|42.49|37.75|32.21|24.83|36.44|
|TriDet|CSN|32.96|30.11|27.04|22.11|16.86|25.82|
|TriDet|SlowFast|34.57|32.49|28.29|23.21|17.97|27.31|
|TriDet|SwinViviT|35.24|32.08|28.82|24.35|18.15|27.73|
|**TriDet**|**VideoMAEv2**|**47.68**|**45.35**|**41.73**|**35.67**|**29.98**|**40.08**|





### Val split
#### Phase-level

| Method |  Backbone | IoU@0.3 | IoU@0.4 | IoU@0.5 | IoU@0.6 | IoU@0.7 | AVG mAP[0.3:0.1:0.7] |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|ActionFormer|CSN|33.13|30.32|26.83|21.55|15.31|25.43|
|ActionFormer|SlowFast|34.83|32.40|28.21|22.34|16.87|26.93|
|ActionFormer|SwinViviT|40.04|36.78|31.34|24.59|17.98|30.15|
|ActionFormer|VideoMAEv2|47.84|44.75|40.73|35.60|27.49|39.28|	
|TriDet|CSN|36.31|33.39|29.27|24.98|19.25|28.64|
|TriDet|SlowFast|35.93|33.57|29.80|25.70|19.79|28.96|
|TriDet|SwinViviT|40.55|37.28|32.84|26.56|20.76|31.60|
|TriDet|VideoMAEv2|49.19|46.29|42.09|37.88|31.16|41.32|

#### Operation-level

| Method |  Backbone | IoU@0.3 | IoU@0.4 | IoU@0.5 | IoU@0.6 | IoU@0.7 | AVG mAP[0.3:0.1:0.7] |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
|ActionFormer|CSN|30.28|28.04|23.64|19.34|14.77|23.21|
|ActionFormer|SlowFast|31.76|29.07|25.54|21.17|15.62|24.63|
|ActionFormer|SwinViviT|34.76|31.48|26.90|21.53|16.31|26.20|
|ActionFormer|VideoMAEv2|45.61|43.36|38.86|33.54|25.65|37.40|
|TriDet|CSN|32.60|30.23|25.92|21.84|16.82|25.48|
|TriDet|SlowFast|33.77|30.46|27.30|22.96|17.90|26.48|
|TriDet|SwinViviT|36.71|33.90|29.51|24.93|18.86|28.78|
|TriDet|VideoMAEv2|47.32|44.68|40.44|35.27|29.45|39.43|




## Installation

1. Please ensure that you have installed PyTorch and CUDA. **(This code requires PyTorch version >= 1.11. We use
   version=1.11.0 in our experiments)**

2. Install the required packages by running the following command:

```shell
pip install  -r requirements.txt
```

3. Install NMS

```shell
cd ./libs/utils
python setup.py install --user
cd ../..
```

4. Done! We are ready to get start!

## Prepare Datasets
You can direct download the we have extracted ([HuggingFace]() | [Baidu Netdisk]()) , then put them into the dataset folder

```bash
cd dataset/features
ln -sT ~/path/to/feature_ophnet/feature ./videomae
```
Or you can extract video features following below steps:

1. Download videos from [OphNet2024](https://huggingface.co/datasets/xioamiyh/OphNet2024
)
```bash
cd dataset
ln -sT ~/path/to/OphNet2024/OphNet2024_all ./videos 
```
2. Extract the videomaev2 features
```bash
cd backbone/videomaev2
bash extract_dataset_feat.sh
```

## Folder Stucture

Check you folder stucture, it should be like:
~~~~
├── backbone  
    ├── videomaev2
├── dataset
    ├── videos
    ├── features
        ├── videomae
            ├── case_0002.pkl
            ├── case_0007.pkl
            └── ...
    ├── tal_annotations
        ├── OphNet2024_operation.json
        └── OphNet2024_phase.json
├── talnets
    ├── actionformer
    └── TriDet
~~~~

## Baseline

We recommend using TriDet as the baseline due to its better performance.

### TriDet

- train
```bash
cd talnets/TriDet
python train.py --config ./configs/medical_videomae_phase.yaml --output baseline
python train.py --config ./configs/medical_videomae_operation.yaml --output baseline
```

- eval
```bash
python eval.py --config ./configs/medical_videomae_phase.yaml --ckpt ~/path/to/checkpoint
python eval.py --config ./configs/medical_videomae_operation.yaml --ckpt ~/path/to/checkpoint
```

- log
```bash
cd ckpt
tensorboard --logdir=./
```

- visualize
```bash
python eval.py --config ./configs/medical_videomae_phase.yaml --ckpt ~/path/to/checkpoint --saveonly
python eval.py --config ./configs/medical_videomae_operation.yaml --ckpt ~/path/to/checkpoint --saveonly
cd ../tools
python visualizer.py

```

### Actionformer

- train
```bash
cd talnets/actionformer
python train.py --config ./configs/medical_videomae_phase.yaml --output baseline
python train.py --config ./configs/medical_videomae_operation.yaml --output baseline
```

- eval
```bash
python eval.py --config ./configs/medical_videomae_phase.yaml --ckpt ~/path/to/checkpoint
python eval.py --config ./configs/medical_videomae_operation.yaml --ckpt ~/path/to/checkpoint
```

- log
```bash
cd ckpt
tensorboard --logdir=./
```
