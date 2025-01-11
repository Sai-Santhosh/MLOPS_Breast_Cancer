# Breast Cancer Classification and MLOps Deployment

A machine learning project to classify breast cancer using the Wisconsin Breast Cancer Diagnostic dataset, complete with an end-to-end MLOps deployment on AWS. This project covers the entire lifecycle from data ingestion to model deployment.

---

## 🚀 Features

- **Dataset:** Breast Cancer Wisconsin (Diagnostic) dataset
- **Machine Learning:** Built using Python and Scikit-learn
- **Deployment:** Fully deployed on AWS EC2, AWS ECR and AWS S3
- **MLOps Pipelines:**
  - Data Ingestion
  - Data Validation
  - Data Transformation
  - Model Training
  - Model Deployment
- **Prediction Pipeline:** Real-time predictions on unseen data
- **Logging:** MLflow and Dagshub for model monitoring
- **Database:** MongoDB for ETL
- **Model Selection:** XGBoost, Gradient Boost, AdaBoost, Random Forest, and Hyperparameter tuning using GridSearchCV to identify the best-performing model.

---

## 📂 Dataset Information

| **Characteristics** | **Details**      |
|----------------------|------------------|
| **Dataset Type**     | Multivariate    |
| **Subject Area**     | Health and Medicine |
| **Task**             | Classification  |
| **Features**         | 30              |
| **Instances**        | 569             |
| **Feature Type**     | Real            |

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

### Project Architecture
![Project Structure](https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer/blob/main/Project_Structure.png)

---

## 📜 Pipelines

### **1. Data Ingestion**
![Data Ingestion](https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer/blob/main/data_ingestion.png)

- Extracts raw data from MongoDB.
- Splits data into training and testing datasets.
- Saves processed files to feature stores.

---

### **2. Data Validation**
![Data Validation](https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer/blob/main/data_validation.png)

- Validates schema and checks for missing or erroneous data.
- Generates data drift reports to ensure consistency.

---

### **3. Data Transformation**
![Data Transformation](https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer/blob/main/data_transformation.png)

- Handles missing values with KNN imputation.
- Applies SMOTE for handling class imbalances.
- Saves transformation objects for future predictions.

---

### **4. Model Training**
![Model Trainer](https://github.com/Sai-Santhosh/MLOPS_Breast_Cancer/blob/main/model_trainer.png)

- Trains models using Random Forest, XGBoost, Gradient Boost, and AdaBoost.
- Performs hyperparameter tuning using GridSearchCV.
- Tracks experiments using MLflow for reproducibility.

---

### **5. Model Deployment**
- Pushes the trained model to AWS S3.
- Dockerizes the application for scalability.
- Deploys to AWS ECS via ECR.

---

## 📊 Results

| Metric        | Value   |
|---------------|---------|
| **Accuracy**  | 96%     |
| **Precision** | 95%     |
| **Recall**    | 94%     |
| **F1-Score**  | 94.5%   |

---

## 📜 Implementation Overview

### **Project Timeline**

| Step | Description |
|------|-------------|
| 1    | Project Structure Set up With Environment |
| 2    | GitHub Repository Set Up With VS Code |
| 3    | Packaging the Project With setup.py |
| 4    | Logging And Exception Handling Implementation |
| 5    | Introduction To ETL Pipelines |
| 6    | Setting Up MongoDB Atlas |
| 7    | ETL Pipeline Setup With Python |
| 8    | Data Ingestion Architecture and Implementation |
| 9    | Data Validation Implementation |
| 10   | Data Transformation Architecture and Implementation |
| 11   | Model Trainer Implementation and Evaluation |
| 12   | Model Experiment Tracking With MLflow and Dagshub |
| 13   | Model Deployment on AWS S3, ECR, and EC2 |
| 14   | Continuous Deployment with GitHub Actions |

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

## 🛣️ Contact

**Sai Santhosh Venkatesh Charumathi**  
Houston, TX  
📧 Email: saisanthoshvc@rice.edu  
[GitHub](https://github.com/Sai-Santhosh) | [LinkedIn](https://linkedin.com/in/v-c-sai-santhosh) | [Kaggle](https://www.kaggle.com/vcsaisanthosh) | [HuggingFace](https://huggingface.co/santu24)
