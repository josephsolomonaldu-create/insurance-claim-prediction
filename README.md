# Insurance Claim Prediction

## Project Overview
This project aims to build a machine learning model that predicts whether a building will have at least one insured claim during the insured period based on building characteristics.

## Dataset
- The dataset contains building-level features
- Target variable: 'Claim'
  - 1 At least one claim occurred
  - 0 No claim occurred
 
## Project Sructure
- '01_data_understanding.ipynb' - Data loading and inspection
- '02_EDA.ipynb' - Exploratory Data Analysis and insights
- '03_Preprocessing.ipynb' -
  - Data cleaning and feature engineering
  - Train-test split
  - Model trainig (Logistic Regression & Random Forest)
  - Hyperparameter tuning
  - Model evaluation and comparison

## Models Used
- Logistic Regression (baseline and tuned)
- Random Forest (baseline and tuned)

> All modeling, tuning, and evaluation steps were performed within the preprocessing notebook.

## Evaluation Metrics
- Accuracy
- ROC-AUC
- Confusion Matrix

## Results
- Best ROC-AUC achieved: ~0.69
- Best Accuracy achieved: ~0.78

## Tools & Libraries
- Python
- Pandas, Numpy
- Scikit-learn
- Matplotlib, Seaborn

## Author
Joseph Solomon Aldu