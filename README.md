# Padang Cuisine Image Classification System

This project is an intelligent web-based system designed to classify traditional Padang cuisine using image recognition powered by deep learning (CNN - MobileNetV2). Users can upload an image of a dish and the system will return its predicted name along with a detailed description, historical background, ingredients, and a trusted source reference.

## 🔍 Features

- **9-Class Image Classification**: Recognizes 9 Padang cuisine categories:
  - Ayam Goreng, Ayam Pop, Rendang, Dendeng Batokok, Gulai Ikan, Gulai Tambusu, Gulai Tunjang, Telur Balado, Telur Dadar.
- **Interactive Web Interface**: Upload images directly and receive classification results with cultural context.
- **Deep Learning Powered**: Uses MobileNetV2, pretrained and fine-tuned for efficient inference.
- **Deployed with Google Cloud Run**: Fully containerized backend and frontend services.

---

## 🧠 Model Overview

- **Architecture**: MobileNetV2
- **Training Platform**: Google Colab (TensorFlow 2.12, Keras 2.12)
- **Dataset**: Custom image dataset of Padang cuisines.
- **Performance**: Validation accuracy up to **90.53%** at epoch 17.

---

## 🖥️ Tech Stack

| Component         | Technology                                          |
|------------------ |-----------------------------------------------------|
| Backend           | Flask + TensorFlow                                  |
| Frontend          | Flask Templates (HTML, Tailwind CSS)                |
| Deployment        | Google Cloud Platform (Cloud Run, Cloud Build, GCR) |
| Containerization  | Docker                                              |
| Data Format       | JSON (for food information metadata)                |
| API Communication | `requests` (Python library)                         |

---

## 🌐 Architecture

The system is divided into two services:
1. **Backend (API)**: Receives images via POST, performs classification, returns a JSON response.
2. **Frontend (Web App)**: Allows users to upload images via a form, forwards to backend, and renders the result page.

📤 **Workflow**:
- Upload → Cloud Run (Frontend) → Forward Image to Cloud Run (Backend) → Prediction → Return JSON → Render Result

---
