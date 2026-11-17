
import streamlit as st
import pandas as pd
import gzip
import joblib

st.set_page_config(
    page_title="Calories Burnt Predictor",
    page_icon="🔥",
    layout="centered"
)

# Load the compressed machine learning model
with gzip.open("calories_model.pkl.gz", "rb") as f:
    package = joblib.load(f)

model = package['model']
scaler = package['scaler']
scale_required = package['scale_required']
features = package['features']

# Application title
st.title("🔥 Calories Burnt Prediction")
st.write("Predict calories burnt during exercise using Machine Learning.")

st.divider()

# User input section
st.subheader("Enter Exercise Details")

gender = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", 10, 100, 21)
height = st.number_input("Height (cm)", 100, 230, 165)
weight = st.number_input("Weight (kg)", 30, 200, 60)
duration = st.number_input("Exercise Duration (minutes)", 1, 120, 30)
heart_rate = st.number_input("Heart Rate", 50, 200, 110)
body_temp = st.number_input("Body Temperature (°C)", 35.0, 43.0, 40.0)

# Prediction
if st.button("Predict Calories", type="primary"):

    user_data = pd.DataFrame([{
        "Gender": 1 if gender == "Female" else 0,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "Duration": duration,
        "Heart_Rate": heart_rate,
        "Body_Temp": body_temp
    }])

    # Maintain the original training feature order
    user_data = user_data[features]

    # Apply scaling only if required
    if scale_required:
        user_data = scaler.transform(user_data)

    prediction = model.predict(user_data)[0]

    st.success(f"Predicted Calories Burnt: {prediction:.2f} kcal")
