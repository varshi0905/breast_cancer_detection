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
* Test Accuracy: 89%
* Test F1 Score: 0.7626
* Test ROC-AUC: 0.8394

### Classification Report

| Class   | Precision | Recall | F1 Score |
| ------- | --------- | ------ | -------- |
| Healthy | 0.92      | 0.94   | 0.93     |
| Cancer  | 0.79      | 0.74   | 0.76     |


### Plots
<img width="2400" height="500" alt="cnn_results_breast_cancer" src="https://github.com/user-attachments/assets/53833c1b-bff6-4cb2-bc3a-39e1ae9cda70" />

---

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

### Plots
<img width="2400" height="500" alt="resultsresnet18_results" src="https://github.com/user-attachments/assets/05c64719-d1c5-4f75-a083-cb4fa2f3664d" />

---

## Key Learnings

* Implemented residual learning and skip connections from scratch.
* Debugged architecture-related issues affecting model convergence.
* Explored class imbalance handling and evaluation metrics.
* Learned practical model validation and performance analysis techniques.
* 
---
### Training Considerations

Deeper architectures such as ResNet18 often require more training time and may benefit from additional epochs compared to simpler CNNs. Their larger capacity allows them to learn more complex feature representations, but convergence depends on factors such as dataset size, learning rate, regularization, and model implementation.

In this project, both models were trained for 20 epochs. Despite the limited training duration, ResNet18 achieved better performance than the custom CNN.

---
## Future Improvements

* U-Net based tumor segmentation
* Grad-CAM visualization for model explainability
* Transfer learning with pretrained ResNet variants
* Dockerized deployment
* Web-based inference application


## Author

Lasya Varshini Buddhavarapu

LinkedIn: https://www.linkedin.com/in/lasya-varshini-buddhavarapu-77a016319/

GitHub: github.com/varshi0905/
