# Insurance Claim Prediction App

This project is an end-to-end machine learning application designed to predict the probability of an insurance claim based on building-related attributes.

The solution covers the full data science workflow, from data understanding and preprocessing to model deployment using Streamlit.

---

## 📌 Project Overview

Insurance companies need to assess the likelihood of claims in order to manage risk and make informed decisions.

This project uses machine learning models to predict whether a building is likely to result in an insurance claim based on structural and environmental features.

The final solution is deployed as an interactive **Streamlit web application**.

---

## 🎯 Objective

The objective of this project is to build a predictive model that estimates the likelihood of an insurance claim using historical building data.

---

## 🛠 Workflow

The project was completed in the following stages:

1. **Data Understanding**
   - explored dataset structure
   - checked missing values
   - reviewed feature descriptions

2. **Exploratory Data Analysis (EDA)**
   - analyzed distributions
   - checked target imbalance
   - identified important patterns

3. **Preprocessing & Feature Engineering**
   - handled missing values
   - encoded categorical variables
   - scaled numerical features
   - built preprocessing pipeline

4. **Modeling & Evaluation**
   - Logistic Regression
   - Tuned Logistic Regression
   - Random Forest

5. **Deployment**
   - saved model using `joblib`
   - built interactive app with Streamlit
   - deployed online

---

## 🤖 Models Used

The following models were trained and evaluated:

- Logistic Regression
- Tuned Logistic Regression
- Random Forest

### Final Model Selected
**Random Forest**

Random Forest was selected for deployment because it achieved better recall for actual insurance claim cases, making it more aligned with the business objective.

---

## 📊 Model Performance Summary

| Model | Accuracy | Claim Recall |
|---|---:|---:|
| Logistic Regression | 78.1% | 16% |
| Tuned Logistic Regression | 78.3% | 13% |
| Random Forest | 76.5% | 25% |

---

## 🚀 Deployment

The final model was deployed using **Streamlit** to provide real-time predictions through a user-friendly web interface.

Users can enter building details such as:

- insured period
- geo code
- building age
- building dimension
- residential status
- building type
- number of windows
- garden
- settlement

and receive instant prediction results.

---

## 🧰 Tools & Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git / GitHub

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone <josephsolomonaldu-create># Insurance Claim Prediction App

This project is an end-to-end machine learning application designed to predict the probability of an insurance claim based on building-related attributes.

The solution covers the full data science workflow, from data understanding and preprocessing to model deployment using Streamlit.

---

## 📌 Project Overview

Insurance companies need to assess the likelihood of claims in order to manage risk and make informed decisions.

This project uses machine learning models to predict whether a building is likely to result in an insurance claim based on structural and environmental features.

The final solution is deployed as an interactive **Streamlit web application**.

---

## 🎯 Objective

The objective of this project is to build a predictive model that estimates the likelihood of an insurance claim using historical building data.

---

## 🛠 Workflow

The project was completed in the following stages:

1. **Data Understanding**
   - explored dataset structure
   - checked missing values
   - reviewed feature descriptions

2. **Exploratory Data Analysis (EDA)**
   - analyzed distributions
   - checked target imbalance
   - identified important patterns

3. **Preprocessing & Feature Engineering**
   - handled missing values
   - encoded categorical variables
   - scaled numerical features
   - built preprocessing pipeline

4. **Modeling & Evaluation**
   - Logistic Regression
   - Tuned Logistic Regression
   - Random Forest

5. **Deployment**
   - saved model using `joblib`
   - built interactive app with Streamlit
   - deployed online

---

## 🤖 Models Used

The following models were trained and evaluated:

- Logistic Regression
- Tuned Logistic Regression
- Random Forest

### Final Model Selected
**Random Forest**

Random Forest was selected for deployment because it achieved better recall for actual insurance claim cases, making it more aligned with the business objective.

---

## 📊 Model Performance Summary

| Model | Accuracy | Claim Recall |
|---|---:|---:|
| Logistic Regression | 78.1% | 16% |
| Tuned Logistic Regression | 78.3% | 13% |
| Random Forest | 76.5% | 25% |

---

## 🚀 Deployment

The final model was deployed using **Streamlit** to provide real-time predictions through a user-friendly web interface.

Users can enter building details such as:

- insured period
- geo code
- building age
- building dimension
- residential status
- building type
- number of windows
- garden
- settlement

and receive instant prediction results.

---

## 🧰 Tools & Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git / GitHub

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone <josephsolomonaldu-create>
cd insurance-claim-prediction

## Author
Joseph Solomon Aldu