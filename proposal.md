
# CSC173 Deep Computer Vision Project Proposal
**Student:** Kyla Reambonanza, 2022-1465  
**Date:** December 11, 2025

## 1. Project Title 
Real-Time Visual Clutter & Risk Assessment of Electrical Posts Using Deep Learning

## 2. Problem Statement
Electrical posts in several urban areas of the Philippines often contains clusters of tangled, overloaded, or poorly maintained wiring, which are commonly known as "spaghetti wires". These wires can often be hazardous which can pose risks of electrical fires, electrocution, and service interruptions. Manual inspection by local authorities can be time-consuming, inconsistent, and limited to manpower. 

Therefore, this project aims to develop a deep learning- based system that analysises images of electrical posts and classifying them into multiple risk levels. By leveraging computer vision, the system can offer safety monitoring, early hazard detection, improve maintenance planning, and overall help authorities prioritise which poles to clean up first.


## 3. Objectives
- Develop a deep learning-based classification system and categorising hazardous wire conditions in electrical poles.

- Implement complete training pipeline including data preprocessing, model training, validation, and evaluation.

## 4. Dataset Plan
- Classes and Labels:
1. Safe = 0–25% clutter
2. Slightly risky = 26–50%
3. Dangerous = 51–75%
4. Extremely dangerous = 76–100%

- Acquisition:
1. Google Image (search terms: "Philippines spaghetti wires", "messy electric post PH", "overloaded cables Philippines")
2. Pexel 
3. News Articles (ABS-CBN, GMA, Rappler, Inquirer)
4. Personal Images

## 5. Technical Approach
- Architecture sketch
- Model: ResNet50 (Transfer Learning)
- Framework: PyTorch
- Hardware: Jupyter Notebook

## 6. Expected Challenges & Mitigations
- Challenge: Small dataset
- Solution: Combine two datasets / Data Augmentation

- Challenge: Real-time performance on laptop
- Solution: YOLOv8n or Reduce frame resolution

