# CSC173 Deep Computer Vision Project Progress Report
**Student:** Kyla Reambonanza, 2022-1465  
**Date:** December 16, 2025  
**Repository:** https://github.com/kay-16/CSC173-DeepCV-Reambonanza.git


## 📊 Current Status
| Milestone | Status | Notes |
|-----------|--------|-------|
| Dataset Preparation | ✅ Done | images downloaded/preprocessed |
| Initial Training | ✅ Done | 15 epochs completed |
| Baseline Evaluation | ⏳ Pending | Training ongoing |
| Model Fine-tuning | ⏳ Not Started | Planned for tomorrow |

## 1. Dataset Progress
- **Total images:** 208 images acquired
- **Train/Val/Test split:** 70%/15%/15%
- **Classes implemented:** 
* 4 classes and labels:
    * Safe = 0–25% clutter
    * Slightly risky = 26–50%
    * Dangerous = 51–75%
    * Extremely dangerous = 76–100%
    
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
![Training and Validation Loss](image-1.png)
![Accuracy Curve](image-2.png)

**Current Metrics (Epoch 15):**
| Metric | Train | Val |
|--------|-------|-----|
| Loss | 0.88 | 0.80 |
| Accuracy | 62.24% | 60.71% |
| Precision | — | — |
| Recall | — | — |

## 3. Challenges Encountered & Solutions
| Issue | Status | Resolution |
|-------|--------|------------|
| Small dataset  | ✅ Done | Data augmentation (Added more augmentation to increase variability) |
| Train accuracy is very high, test accuracy is low  | ⏳ In Progress | Freeze most of the backbone layers to avoid overfitting |
| CUDA out of memory | ⏳ Planned | Reduced batch_size from 32→16 |
| Class imbalance | ⏳ Planned | Added class weights to loss function |
| Slow validation | ⏳ Planned | Implement early stopping |

## 4. Next Steps (Before Final Submission)
- [ ] Complete training (50 more epochs)
- [ ] Hyperparameter tuning (learning rate, augmentations)
- [ ] Baseline comparison (vs. original pre-trained model)
- [ ] Record 5-min demo video
- [ ] Write complete README.md with results