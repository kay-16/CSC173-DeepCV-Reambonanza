# CSC173 Deep Computer Vision Project Progress Report
**Student:** Kyla Reambonanza, 2022-1465  
**Date:** December 16, 2025  
**Repository:** https://github.com/kay-16/CSC173-DeepCV-Reambonanza.git


## 📊 Current Status
| Milestone | Status | Notes |
|-----------|--------|-------|
| Dataset Preparation | ✅ Done | images downloaded/preprocessed |
| Initial Training | ✅ Done | 15 epochs completed |
| Baseline Evaluation | ✅ Done | Final metrics gathered on unseen test set |
| Model Fine-tuning (Phase 2) | ✅ Done | Completed 40 epochs (Unfrozen Backbone) |
| Final Inference Script | ✅ Done | Deployed two-stage model for local webcam inference |
| Final Metrics (Test Set) | ✅ Done | Test Accuracy achieved: 50.00% |

## 1. Dataset Progress
- **Total images:** 208 images acquired
- **Train/Val/Test split:** 70%/15%/15%
- **Classes implemented:** 
* 4 classes:
    * Safe
    * Slightly 
    * Dangerous
    * Extremely dangerous
    
- **Preprocessing applied:** 
    * Resize(640) 
    * Normalization
    * Augmentation [flip, rotate small angles (e.g. ±15° or ±20°), brightness]
    * Random contrast

**Sample data preview:**

<p><b>Dangerous</b></p>
<img src="/csc173-deepcv-final-proj/dataset/raw/dangerous/image_1.jpeg" width="300">

<p><b>Extremely Dangerous</b></p>
<img src="/csc173-deepcv-final-proj/dataset/raw/extremely_dangerous/image_10.jpeg" width="300">

<p><b>Safe</b></p>
<img src="/csc173-deepcv-final-proj/dataset/raw/safe/image_13.jpg" width="300">

<p><b>Slightly Risky</b></p>
<img src="/csc173-deepcv-final-proj/dataset/raw/slightly_risky/image_17.jpg" width="300">

## 2. Training Progress

**Training Curves (so far)**
<p><b>Initial Training & Validation Loss</b></p>
<img src="/image-1.png" width="300">

<p><b>Initial Training & Validation Accuracy</b></p>
<img src="/image-2.png" width="300">

<p><b>Full Training & Validation Loss & Accuracy (Phase 1 + Phase 2)</b></p>
![Training & Validation Loss & Accuracy](image.png)

**Final Test Set Metrics (EfficientNet-B0 Classifier):**
| Metric | Train | Val |
|--------|-------|-----|
| Loss | 0.88 | 0.80 |
| Accuracy | 50.00% | 60.71% |
| Precision | 41.11% | — |
| Recall | 50% | — |

**Final Test Set Metrics (YOLOv8 Detection Model):**
| Metric | Peak Validation Score | Note |
|--------|-------|-----|
| Precision | 51.82% | Moderate confidence in bounding boxes |
| Recall | 34.60% | The detector missed two-thirds of the total clusters |
| mAP50 | 16.99% | Low detection accuracy, indicating a bottleneck |

## 3. Challenges Encountered & Solutions
| Issue | Status | Resolution |
|-------|--------|------------|
| Small dataset  | ✅ Done | Data augmentation (Added more augmentation to increase variability) |
| Train accuracy is very high, test accuracy is low  | ✅ Done | Freeze most of the backbone layers to avoid overfitting |
| High Initial Learning Rate Destroys Weights | ✅ Done | Implemented Two-Phase Fine-Tuning: Used a low Learning Rate (0.0001) and froze most of the backbone layers (EfficientNet-B0 base) during Phase 1. |
| Small Dataset / Low Variability | ⏳ In Progress | Strategy Change: Replaced basic data augmentation (flip, rotation, jitter) with Aggressive Augmentation (TrivialAugmentWide) to significantly increase data variability and avoid overfitting. |
| Significant Overfitting Gap (Train Acc ~90%, Val Acc ~60%) | ✅ Done | Strategy Change: Unfroze all layers (Phase 2) and used a lower Learning Rate (0.00001) combined with Aggressive Augmentation to force the model to learn more generalizable features. |


## 4. Next Steps (Before Final Submission)
- [x] Complete training (50 more epochs)
- [x] Hyperparameter tuning (learning rate, augmentations)
- [x] Baseline comparison (vs. original pre-trained model)
- [x] Record 5-min demo video
- [ ] Write complete README.md with results