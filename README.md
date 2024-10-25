# OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding

<a href='https://minghu0830.github.io/OphNet-benchmark/'><img src='https://img.shields.io/badge/Project-Page-Green'></a>  <a href='https://arxiv.org/pdf/2406.07471'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a> [![Static Badge](https://img.shields.io/badge/HF-yellow?logoColor=violet&label=%F0%9F%A4%97%20Dataset%20)]()


## News
* **[Oct, 2024]** We realeased OphNet2024 ! More information can be found in Data Preparation.
* **[Jul, 2024]** OphNet2024 is in preparation——larger scale, more accurate, and more experimental results!
* **[Jul, 2024]** OphNet was accepted by ECCV2024.
* **[Jun, 2024]** The manuscript can be found on [arXiv](https://arxiv.org/pdf/2406.07471).

<p align="center">
    <img src="./image/logo.gif"/> <br />
</p>

## Introduction
Surgical scene perception via videos is critical for advancing robotic surgery, telesurgery, and AI-assisted surgery, particularly in ophthalmology. However, the scarcity of diverse and richly annotated video datasets has hindered the development of intelligent systems for surgical workflow analysis. Existing datasets face challenges such as small scale, lack of diversity in surgery and phase categories, and absence of time-localized annotations. These limitations impede action understanding and model generalization validation in complex and diverse real-world surgical scenarios. To address this gap, we introduce OphNet, a large-scale, expert-annotated video benchmark for ophthalmic surgical workflow understanding. OphNet features: 1) A diverse collection of 2,278 surgical videos spanning 66 types of cataract, glaucoma, and corneal surgeries, with detailed annotations for 102 unique surgical phases and 150 fine-grained operations. 2) Sequential and hierarchical annotations for each surgery, phase, and operation, enabling comprehensive understanding and improved interpretability. 3) Time-localized annotations, facilitating temporal localization and prediction tasks within surgical workflows. With approximately 205 hours of surgical videos, OphNet is about 20 times larger than the largest existing surgical workflow analysis benchmark.
<p align="center">
    <img src="./image/loca.png"/> <br />
</p>

## Dataset Preparation
### Directory Structure
```
OphNet-benchmark
├── annotation
│   ├── OphNet2024_surgery.csv
│   ├── OphNet2024_all.csv
│   ├── OphNet2024_challenge.csv
├── data_processing
│   ├── clipper.py
├── OphNet2024_all (≈305G, all untrimmed videos)
```
*  **OphNet2024_surgery.csv**: Annotated 1969 untrimmed videos for surgical types, with the first label as the primary surgery. Selected 745 videos for time-boundary annotation.
*  **OphNet2024_all.csv**: Original version.
*  **OphNet2024_challenge.csv**: Map phase and operation labels with fewer than 15 clips to numeric IDs 51 and 106, which can be interpreted as renaming labels with fewer than 15 instances as "Others."

### Download
*  **Video Download Source**: [HuggingFace]() | [Baidu Netdisk]() | [Google Drive]()
*  **Label Description**: The table with Chinese and English versions of surgery, phase, and operation names along with their ID mappings: [OphNet2024_Label](https://docs.google.com/spreadsheets/d/1p5lURkth587-lxYwd6eOSmSxPpvIqvyuOKW-4B49PT0/edit?usp=sharing) 


<!--Accessing the OphNet dataset requires an application. If you wish to access the full dataset, please submit an [access request](https://forms.gle/GhJyQDPUrE74jLy87) and adhere to the licensing agreement. We will send the data to your specified email address.
-->

## Challenge/Workshop
Coming soon...

## Citation
```python
@article{hu2024ophnet,
  title={OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding},
  author={Hu, Ming and Xia, Peng and Wang, Lin and Yan, Siyuan and Tang, Feilong and Xu, Zhongxing and Luo, Yimin and Song, Kaimin and Leitner, Jurgen and Cheng, Xuelian and others},
  journal={arXiv preprint arXiv:2406.07471},
  year={2024}
}
```
