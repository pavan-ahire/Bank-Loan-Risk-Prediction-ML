# 💳 Bank Loan Risk Prediction using Machine Learning

---

## 🔍 Project Overview
Loan risk prediction is a critical task in the banking and financial sector.  
Banks must evaluate whether a customer is likely to default before approving a loan. This decision depends on multiple factors such as **income, employment length, credit history, loan amount, interest rate, and previous defaults**.

This project focuses on **predicting loan default risk using machine learning** and providing **interactive tools for prediction and data analysis**.

The project includes:
- End-to-end **Machine Learning pipeline**
- **Exploratory Data Analysis (EDA)**
- Multiple ML model training and comparison
- **Live loan risk prediction web app**
- **Interactive EDA dashboard**

---

## 🚀 Live Deployment
The project is deployed using **Streamlit Cloud**, providing both prediction and analytics capabilities.

### 🔗 Live Links
- **Loan Risk Prediction App**  
  👉 https://bank-loan-risk-prediction-ml.streamlit.app/

- **Loan Risk EDA Dashboard**  
  👉 https://bank-loan-eda-dashboard.streamlit.app/

- **GitHub Repository**  
  👉 https://github.com/pavan-ahire/Bank-Loan-Risk-Prediction-ML

---

## 🎯 Objectives
- Analyze factors influencing loan default risk
- Perform in-depth exploratory data analysis
- Train and compare multiple ML models
- Predict loan risk for new customers
- Provide insights through interactive dashboards

---

## 💼 Business Problem & Impact
Banks and financial institutions need reliable methods to evaluate loan applications and minimize financial risk.

This project helps organizations to:
- Identify **high-risk borrowers**
- Reduce **loan default rates**
- Improve **loan approval decision-making**
- Enable **data-driven financial risk assessment**

This solution is useful for:
- Banking analysts  
- Risk analysts  
- Data analysts  
- Financial institutions  

---

## 🔄 End-to-End ML Pipeline
The project follows a **production-oriented ML workflow**:

1. Data collection & understanding  
2. Data cleaning & preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature engineering  
5. Model training  
6. Model comparison & evaluation  
7. Best model selection  
8. Model persistence (`.pkl`)  
9. Deployment using Streamlit  
10. Dashboard development for analysis  

---

## 🧠 Machine Learning Models Used
The following algorithms were implemented and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree Classifier
- Random Forest Classifier

📌 **Random Forest Classifier** was selected for deployment due to:
- Highest accuracy and F1-score
- Robust performance on tabular data
- Ability to handle non-linear relationships
- Better generalization compared to other models

---

## 📊 Exploratory Data Analysis (EDA)
EDA was performed to:
- Understand distribution of loan features
- Analyze relationships between variables
- Identify correlations and patterns
- Detect outliers and skewness
- Understand factors influencing loan default

Visualizations include:
- Distribution plots
- Correlation heatmaps
- Boxplots
- Loan risk comparisons
- Feature relationship analysis

---

## 🧩 Feature Engineering & Preprocessing
Key preprocessing steps:
- Handling missing values
- Removing duplicate records
- Encoding categorical variables
- Feature scaling
- Handling class imbalance using SMOTE
- Saving scaler and model objects for deployment

This ensures **training and prediction pipelines remain consistent**.

---

## 🧪 Model Evaluation Metrics
Models were evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

These metrics help evaluate classification performance and reliability.

---

## 🖥️ Streamlit Prediction App Features
- Modern and interactive UI
- User-friendly input forms
- Real-time loan risk prediction
- Probability and confidence display
- Clean dashboard-style layout

---

## 📈 Streamlit EDA Dashboard Features
- Interactive visualizations
- Univariate and bivariate analysis
- Feature distribution insights
- Risk pattern exploration
- Responsive layout

---

## 🛠️ Technologies Used
- **Language**: Python  
- **Libraries**:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - imbalanced-learn (SMOTE)
  - streamlit
  - joblib
- **Deployment**: Streamlit Cloud  
- **Version Control**: Git & GitHub  

---

## 📂 Project Folder Structure

```text
Bank-Loan-Risk-Prediction-ML/
│
├── app/
│   └── Streamlit app components and UI logic
│
├── dashboard/
│   └── EDA dashboard scripts and visualizations
│
├── data/
│   └── Raw and cleaned datasets
│
├── notebooks/
│   └── EDA and model training notebooks
│
├── model/
│   └── Saved ML model artifacts
│
├── README.md
├── app.py
├── dashboard.py
├── rf_model.pkl
├── scaler_model.pkl
├── requirements.txt
└── dataset.csv
```
---
## 🧠 Key Skills Demonstrated

- Machine Learning model development and evaluation
- Exploratory Data Analysis (EDA)
- Feature engineering and data preprocessing
- Model serialization and reuse (`.pkl` files)
- Deployment of ML models using Streamlit
- Dashboard creation for business insights
- End-to-end project implementation
- Version control using Git & GitHub
---
## 👨‍💻 Author

**Pavan Ahire**


 Aspiring Data Scientist | Machine Learning & Analytics Enthusiast
- [🔗 GitHub](https://github.com/pavan-ahire)
- [🔗 LinkedIn](https://www.linkedin.com/in/pavan-ahire-260940364/)
