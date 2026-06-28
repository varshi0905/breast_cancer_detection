# 🩺 Breast Cancer Detection using Deep Learning

A production-ready Breast Cancer Histopathology Image Classification web application built using **PyTorch**, **FastAPI**, **Docker**, and **HTML/CSS/JavaScript**.

The application allows users to upload a histopathology image patch and predicts whether the tissue is **IDC Positive** or **IDC Negative** using a custom-built ResNet-18 model trained from scratch.

---

## 🚀 Live Demo

🔗 https://breast-cancer-detection-61e3.onrender.com

---

## 📸 Application Preview

<p align="center">
<img src="breast_cancer_webpage.jpg
        " width="700">
</p>

---

# Project Overview

Breast cancer is one of the leading causes of cancer-related deaths worldwide. Early diagnosis through histopathology image analysis significantly improves treatment outcomes.

This project automates the classification of breast cancer histopathology image patches into:

- IDC Positive
- IDC Negative

using Deep Learning.

The project demonstrates the complete Machine Learning lifecycle:

- Data preprocessing
- Model training
- Model evaluation
- Model deployment
- REST API development
- Docker containerization
- Cloud deployment

---

# Features

- Upload histopathology image patches
- Deep Learning inference using a custom ResNet-18
- FastAPI REST API backend
- Responsive HTML/CSS frontend
- Dockerized application
- Cloud deployment using Render
- Production-ready project structure

---

# Tech Stack

### Deep Learning

- PyTorch
- Torchvision
- NumPy
- PIL

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Deployment

- Docker
- Render

---

# Project Structure

```
breast_cancer_api/
│
├── app/
│   ├── main.py              # FastAPI application
│   ├── model.py             # ResNet18 architecture
│   ├── utils.py             # Image preprocessing & prediction
│   └── __init__.py
│
├── models/
│   └── best_resnet18_model.pth
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Model

Architecture:

- Custom ResNet-18 (implemented from scratch)

Framework:

- PyTorch

Task:

Binary Image Classification

Classes:

- IDC Positive
- IDC Negative

---

# Deployment Pipeline

```
User

        │

Upload Image

        │

HTML Frontend

        │

POST Request

        │

FastAPI

        │

Image Preprocessing

        │

ResNet18 Model

        │

Prediction

        │

JSON Response

        │

Frontend

        │

Prediction Display
```

---

# Running Locally

Clone the repository

```bash
git clone https://github.com/yourusername/breast_cancer_api.git

cd breast_cancer_api
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000
```

---

# Running with Docker

Build Docker image

```bash
docker build -t breast-cancer-api .
```

Run container

```bash
docker run -p 8000:8000 breast-cancer-api
```

Open

```
http://localhost:8000
```

---

# Future Improvements

- Confidence score visualization
- Grad-CAM explainability
- Batch image prediction
- Mobile-friendly UI
- Model versioning
- CI/CD pipeline using GitHub Actions
- ONNX optimization for faster inference

---

# Skills Demonstrated

- Deep Learning
- Computer Vision
- PyTorch
- FastAPI
- REST APIs
- Docker
- HTML/CSS
- JavaScript
- Model Deployment
- Cloud Deployment
- Production ML Pipeline

---

# Author

**Lasya Varshini Buddhavarapu**

GitHub:
https://github.com/varshi0905
