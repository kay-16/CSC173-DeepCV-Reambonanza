
# CSC173 Deep Computer Vision Project Proposal
**Student:** Kyla Reambonanza, 2022-1465  
**Date:** December 11, 2025

## 1. Project Title 
Vision-Based Human Fall Detection Using Deep Learning in Philippine Settings

## 2. Problem Statement
The risk and consequences of potential falls increase significantly with age, with people aged 65 years and above are susceptible to serious fall-related injuries that threaten their independence (CDC, 2024). In the Philippines, data from the Online National Electronic Injury Surveillance System (ONEISS) shows that fall is one of the top five leading causes of injury among Filipinos in 2013, 2015, and 2017. To address this concern, this project focuses on developing a deep learning-based fall detection system catered for common environments in the Philippines such as homes, schools, hospitals, barangay centers, and elderly-care facilities. By leveraging standard webcams and video-based models, the system aims to offer a low-cost, non-intrusive, and accessible solution that is timely and revelant, particularly valuable for communities with limited resources across the Philippines. 

## 3. Objectives
- Develop a real-time fall detection system and train a deep computer vision model achieving target performance metrics

- Implement complete training pipeline including data preprocessing, model training, validation, and evaluation.

## 4. Dataset Plan
**Main Dataset**
- Source: https://github.com/ekramalam/GMDCSA24-A-Dataset-for-Human-Fall-Detection-in-Videos/tree/v2.1
Size: ~70 videos (falls + ADL)

**Supplementary Dataset**
- Source: https://falldataset.com/
Size: ~21000 images spanning falls and non-falls

- Classes:
1. Fall
2. ADL (Activities of Daily Living)
3. Near fall

- Acquisition:
1. Download datasets (videos/images) -> extract frames -> preprocess to desired format

2. Combine datasets -> shuffle

## 5. Technical Approach
- Architecture sketch
- Model: YOLOv8n-Pose / ResNet50 + Fall Classifier ?
- Framework: PyTorch
- Hardware: 

## 6. Expected Challenges & Mitigations
- Challenge: Small dataset
- Solution: Combine two datasets  

- Challenge: Real-time performance on laptop
- Solution: YOLOv8n or Reduce frame resolution

## 7. References 
- U.S. Centers for Disease Control and Prevenetion (CDC), 2024. Available from: https://www.cdc.gov/falls/data-research/

- Department of Health. Online National Electronic Injury Surveillance System (ONEISS) Factsheet Volume 5, Issue 2. 2013 September. Available from: https://oneiss.doh.gov.ph/factsheets/2ndquarter2013.pdf.

- Department of Health. Online National Electronic Injury Surveillance System (ONEISS) Factsheet Volume 7, Issue 2. 2015 November. Available from: https://oneiss.doh.gov.ph/factsheets/2ndquarter2015.pdf.

- Department of Health. Online National Electronic Injury Surveillance System (ONEISS) Factsheet Volume 9, Issue 1. 2017 September. Available from: https://oneiss.doh.gov.ph/factsheets/Final_sep_28_1st_2017_factsheet.pdf.