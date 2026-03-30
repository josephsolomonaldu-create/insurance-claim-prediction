import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessor
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

st.title("Insurance Claim Prediction App")

st.write("Enter building details to predict the probability of an insurance claim.")

# Inputs
insured_period = st.slider("Insured Period", 0.0, 1.0)
geo_code = st.text_input("Geo Code")
building_age = st.number_input("Building Age", min_value=0)
building_dimension = st.number_input("Building Dimension", min_value=0)
residential = st.selectbox("Residential", [0, 1])
building_painted = st.selectbox("Building Painted", ["V", "N"])
building_fenced = st.selectbox("Building Fenced", ["V", "N"])
garden = st.selectbox("Garden", ["V", "N"])
settlement = st.selectbox("Settlement", ["U", "R"])
building_type = st.selectbox("Building Type", ["1", "2", "3", "4"])
number_of_windows = st.selectbox("Number of Windows", [1,2,3,4,5,6,7,8,9,10])

# Create input dataframe
input_data = pd.DataFrame({
    'Insured_Period': [insured_period],
    'Geo_Code': [geo_code],
    'Building_Age': [building_age],
    'Building Dimension': [building_dimension],
    'Residential': [residential],
    'Building_Painted': [building_painted],
    'Building_Fenced': [building_fenced],
    'Garden': [garden],
    'Settlement': [settlement],
    'Building_Type': [building_type],
    'NumberOfWindows': [number_of_windows]
})

# Predict

if st.button("Predict"):
    try:
        input_processed = preprocessor.transform(input_data)

        prediction = model.predict(input_processed)[0]

        if prediction == 1:
            st.success("High Risk of Insurance Claim")
        else:
            st.success("Low Risk of Insurance Claim")

    except Exception as e:
        st.error(f"Error: {e}")
    
    