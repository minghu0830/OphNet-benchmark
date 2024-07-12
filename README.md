# OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding
<a href=''><img src='https://img.shields.io/badge/Project-Page-Green'></a>  <a href='https://arxiv.org/pdf/2406.07471'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a> [![YouTube](https://badges.aleen42.com/src/youtube.svg)]()

## News
* **[Jul, 2024]** OphNet was accepted by ECCV2024.
* **[Jun, 2024]** The manuscript can be found on [arXiv](https://arxiv.org/pdf/2406.07471).

## Introduction
Surgical scene perception via videos are critical for advancing robotic surgery, telesurgery, and AI-assisted surgery, particularly in ophthalmology. However, the scarcity of diverse and richly annotated video datasets has hindered the development of intelligent systems for surgical workflow analysis. Existing datasets for surgical workflow analysis, which typically face challenges such as small scale, a lack of diversity in surgery and phase categories, and the absence of time-localized annotations, limit the requirements for action understanding and model generalization validation in complex and diverse real-world surgical scenarios. To address this gap, we introduce OphNet, a large-scale, expert-annotated video benchmark for ophthalmic surgical workflow understanding. OphNet features: 1) A diverse collection of 2,278 surgical videos spanning 66 types of cataract, glaucoma, and corneal surgeries, with detailed annotations for 102 unique surgical phases and 150 fine-grained operations; 2) It offers sequential and hierarchical annotations for each surgery, phase, and operation, enabling comprehensive understanding and improved interpretability; 3) Moreover, OphNet provides time-localized annotations, facilitating temporal localization and prediction tasks within surgical workflows. With approximately 205 hours of surgical videos, OphNet is about 20 times larger than the largest existing surgical workflow analysis benchmark.

## Dataset Download
```
OphNet
├── Annotation Files
│   ├── all
│   ├── task1_primary_surgery_recognition
│   ├── task2_phase_recognition
│   ├── task3_operation_recognition
│   ├── task4_phase_localization
│   ├── task5_phase_anticipation
├── Original Video Files (≈300G)
├── Processed Video Files (Res.: 256 X 256, FPS: 25, ≈100)
├── Trimmed Video Files (Res.: 256 X 256, FPS: 25, ≈300G)
```

## Dataset and Code Release Progress
- [ ] Add videos and annotation files
- [ ] Add code and checkpoint


## Citation
```python
@article{hu2024ophnetlargescalevideobenchmark,
      title={OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding}, 
      author={Ming Hu and Peng Xia and Lin Wang and Siyuan Yan and Feilong Tang and Zhongxing Xu and Yimin Luo and Kaimin Song and Jurgen Leitner and Xuelian Cheng and Jun Cheng and Chi Liu and Kaijing Zhou and Zongyuan Ge},
      year={2024},
      eprint={2406.07471},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2406.07471}, 
}
```
