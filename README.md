 # End-to-End Machine Learning Production Pipeline

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green) ![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen) ![Docker](https://img.shields.io/badge/Docker-Containerization-blue) [![Python Application CI](https://github.com/abdulghaffark2425/my_industry_project/actions/workflows/main.yaml/badge.svg)](https://github.com/abdulghaffark2425/my_industry_project/actions/workflows/main.yaml)

An end-to-end production-ready Machine Learning system integrated with Flask web interface and MongoDB for logging dynamic predictions.

---

## 🏗️ System Architecture

1. **Data Ingestion:** Fetches raw data, splits into Train/Test subsets.
2. **Data Transformation:** Handles imputation, scaling, and categorical encoding via Scikit-Learn Pipelines.
3. **Model Trainer:** Evaluates algorithms (Random Forest, Decision Tree, Gradient Boosting) and serializes the best performing model (model.pkl).
4. **Prediction Pipeline:** Serves real-time inference requests via Flask API and stores record histories in **MongoDB**.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Flask
* **Database:** MongoDB (PyMongo)
* **ML Libraries:** Scikit-Learn, Pandas, NumPy, XGBoost, CatBoost
* **DevOps:** Docker

---

## ⚙️ Local Setup Instructions

1. **Clone Repository:**
   git clone https://github.com/abdulghaffark2425/my_industry_project.git
   cd my_industry_project

2. **Virtual Environment Setup:**
   python -m venv .venv
   .venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Start Application:**
   python app.py 
