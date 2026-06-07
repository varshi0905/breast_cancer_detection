# Breast Cancer Detection using CNN and ResNet18

## Overview

This project implements and compares a custom Convolutional Neural Network (CNN) and a ResNet18 architecture for binary classification of breast histopathology image patches. The objective is to identify Invasive Ductal Carcinoma (IDC) from microscopic tissue images.

The project covers the complete deep learning workflow, including data preprocessing, augmentation, model development, training, evaluation, and performance comparison.

---

## Dataset

**Dataset:** IDC Regular Histopathology Dataset

* 277,524 RGB image patches
* Image size: 50 × 50 pixels
* Binary classification:

  * 0 → Healthy tissue
  * 1 → Cancerous tissue (IDC)

Dataset source: Kaggle Breast Histopathology Images

---

## Features

* Custom CNN implemented from scratch
* ResNet18 implemented from scratch in PyTorch
* Data augmentation using Albumentations
* Custom PyTorch Dataset and DataLoader
* Training and validation pipelines
* Model checkpointing
* Performance evaluation using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * ROC-AUC
  * Confusion Matrix

---

## Technologies Used

* Python
* PyTorch
* OpenCV
* Albumentations
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Kaggle

---

## Results

### CNN

* Best Validation Loss: 0.2963

### ResNet18

* Best Validation Loss: 0.2778
* Test Accuracy: 90%
* Test F1 Score: 0.779
* Test ROC-AUC: 0.9432

### Classification Report

| Class   | Precision | Recall | F1 Score |
| ------- | --------- | ------ | -------- |
| Healthy | 0.93      | 0.93   | 0.93     |
| Cancer  | 0.78      | 0.77   | 0.78     |

---

## Key Learnings

* Implemented residual learning and skip connections from scratch.
* Debugged architecture-related issues affecting model convergence.
* Explored class imbalance handling and evaluation metrics.
* Learned practical model validation and performance analysis techniques.

---

## Future Improvements

* U-Net based tumor segmentation
* Grad-CAM visualization for model explainability
* Transfer learning with pretrained ResNet variants
* Dockerized deployment
* Web-based inference application


## Author

Lasya Varshini Buddhavarapu

Computer Vision & AI/ML Engineer

LinkedIn: [Your LinkedIn]
GitHub: [Your GitHub]
