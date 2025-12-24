
# CSC173 Deep Computer Vision Project Proposal
**Student:** Kyla Reambonanza, 2022-1465  
**Date:** December 11, 2025

## 1. Project Title 
Real-Time Visual Clutter & Risk Assessment of Electrical Posts Using Deep Learning

## 2. Problem Statement
Electrical posts in several urban areas of third-world countries like the Philippines, often contains clusters of tangled, overloaded, or poorly maintained wiring, which are commonly known as "spaghetti wires". These wires can often be hazardous which can pose risks of electrical fires, electrocution, and service interruptions. Manual inspection by local authorities can be time-consuming, inconsistent, and limited to manpower. 

Therefore, this project aims to develop a deep learning- based system that analysises images of electrical posts and classifying them into multiple risk levels. By leveraging computer vision, the system can offer safety monitoring, early hazard detection, improve maintenance planning, and overall help authorities prioritise which poles to clean up first. In Philippine context, this project satifies Anti-Obstruction of Power Lines Act or the R.A. 11361, which ensures the smooth and uninterrupted transmission of electricity.

## 3. Objectives
- Develop a deep learning-based classification system and categorising hazardous wire conditions in electrical poles.
- Implement complete training pipeline including data preprocessing, model training, validation, and evaluation.

## 4. Dataset Plan
- Classes:
    * Safe - Minimal wiring, no apparent risk, clean environment.
    * Slightly risky - Some excess/tangled wiring, but no immediate hazard.
    * Dangerous - Significant spaghetti wiring, noticeable overloading, structural issues.
    * Extremely dangerous - Severe clutter, fire hazards, potential for imminent failure.

- Acquisition:
    * Google Image (search terms: "Philippines spaghetti wires", "messy electric post, "overloaded cables")
    * Google Maps
    * Pexels (free stock images of "clean electric pole lines")
    * News Articles (ABS-CBN, GMA, Rappler, Inquirer)
    * Personal Images

- Expected size: 
    * 52 images per class
    * 208 images in total

## 5. Technical Approach
- Architecture sketch

| Step | Action | Description |
|------|-----------|-------|
| 1 | Input Stream | Capture real-time video frames from device webcam |
| 2 | PreProcessing | Resize frame and normalises pixel values |
| 3 | Stage 1: Detection (YOLOv8nY) | YOLOv8n (nano) determines and produces (output) the precise bounding box coordinates of the wire cluster |
| 4 | Cropping | Original frame is cropped to include only the wire clusters bounding box |
| 5 | Stage 2: Classification (EfficientNet-B0) | EfficientNet-B0 model processes the cropped image and classifies it (4 output neurons) |
| 6 | Decision Engine | Uses Softmax/Argmax to select one of the 4 classes |
| 7 | Final Output | Real-time display of the output class (e.g. Dangerous) |

- Model: EfficientNet-B0 + YOLOv8n
- Framework: PyTorch
- Hardware: Jupyter Notebook

## 6. Expected Challenges & Mitigations
- Challenge: Small dataset
    * Solution: Combine two or more datasets / Data Augmentation

- Challenge: Real-time performance on laptop
    * Solution: YOLOv8n or Reduce frame resolution

