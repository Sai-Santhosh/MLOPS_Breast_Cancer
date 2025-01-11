# Breast Cancer Classification and MLOps Deployment

![Project Banner](https://via.placeholder.com/1200x300.png?text=Breast+Cancer+Classification+and+MLOps+Deployment)

A machine learning project to classify breast cancer using the Wisconsin Breast Cancer Diagnostic dataset, complete with an end-to-end MLOps deployment on AWS.

---

## 🚀 Features

- **Dataset:** Breast Cancer Wisconsin (Diagnostic) dataset
- **Machine Learning:** Built using Python and Scikit-learn
- **Deployment:** Fully deployed on AWS EC2 and AWS ECR
- **MLOps Pipelines:**
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
  - Model Deployment
- **Prediction Pipeline:** Real-time predictions on unseen data
- **Logging:** MLflow and Dagshub for model monitoring
- **Database:** MongoDB for ETL

---

## 📂 Dataset Information

| **Characteristics** | **Details** |
|----------------------|-------------|
| **Dataset Type**     | Multivariate |
| **Subject Area**     | Health and Medicine |
| **Task**             | Classification |
| **Features**         | 30 |
| **Instances**        | 569 |
| **Feature Type**     | Real |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-Services-orange?logo=amazonaws&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-Containers-blue?logo=docker&logoColor=white)

- **Backend Framework:** FastAPI
- **Model Deployment:** Docker + AWS (ECS, ECR, S3, EC2)
- **CI/CD:** GitHub Actions
- **Database:** MongoDB
- **Monitoring:** MLflow, Dagshub

---

## 🌟 Key Visuals

### **Training Pipeline Execution**
![Training Pipeline](https://via.placeholder.com/1200x600.png?text=Training+Pipeline+Execution)

### **Prediction Pipeline Execution**
![Prediction Pipeline](https://via.placeholder.com/1200x600.png?text=Prediction+Pipeline+Execution)

### **AWS S3 Outputs**
![AWS S3](https://via.placeholder.com/1200x600.png?text=AWS+S3+Outputs)

---

## 📜 Project Workflow

### **1. MLOps Pipelines**
- **Data Ingestion:** Extracts, transforms, and loads data from MongoDB.
- **Data Validation:** Ensures the quality of the dataset.
- **Data Transformation:** Preprocesses data using standard scalers and encoders.
- **Model Training:** Trains a classification model.
- **Model Deployment:** Deploys the model for real-time predictions.

### **2. Deployment Setup**
- **AWS EC2 & S3**
- **AWS Elastic Container Registry (ECR)**
- **Dockerized Application**

### **3. CI/CD Workflows**
- **Continuous Integration:** Linting and unit testing.
- **Continuous Delivery:** Builds and pushes Docker images to ECR.
- **Continuous Deployment:** Runs the application on ECS.

---

## 📊 Results

| Metric        | Value   |
|---------------|---------|
| **Accuracy**  | 96%     |
| **Precision** | 95%     |
| **Recall**    | 94%     |
| **F1-Score**  | 94.5%   |

---

## 💻 Installation

```bash
# Clone the repository
$ git clone https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer.git

# Navigate to the project directory
$ cd MLOPS_Breast_Cancer

# Build and run Docker container
$ docker build -t breastcancer:latest .
$ docker run -p 8000:8000 breastcancer:latest
```

---

## 🖥️ Usage

1. Access the FastAPI interface at: `http://localhost:8000`
2. Use the `/train` endpoint to execute the training pipeline.
3. Use the `/predict` endpoint to predict outcomes on unseen data.

---

## 🌐 URLs

- **Dagshub MLflow:** [Link](https://dagshub.com/Sai-Santhosh/MLOPS_Breast_Cancer)
- **GitHub Repository:** [Link](https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer)

---

## 📬 Contact

**Sai Santhosh Venkatesh Charumathi**  
Houston, TX  
📧 Email: saisanthoshvc@rice.edu  
[GitHub](https://github.com/Sai-Santhosh) | [LinkedIn](https://linkedin.com/in/sai-santhosh)

---

## 🎯 Acknowledgments

This project was developed as part of a Machine Learning and MLOps initiative. Special thanks to the community and resources that made this possible.
