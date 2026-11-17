
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Calories Burnt Predictor",
    page_icon="🔥",
    layout="centered"
)

package = joblib.load("calories_model.pkl")

model = package['model']

st.title("🔥 Calories Burnt Prediction")
st.write("Predict calories burnt during exercise using Machine Learning.")

st.divider()

st.subheader("Enter Exercise Details")

gender = st.selectbox("Gender", ["Female", "Male"])
age = st.number_input("Age", 10, 100, 21)
height = st.number_input("Height (cm)", 100, 230, 165)
weight = st.number_input("Weight (kg)", 30, 200, 60)
duration = st.number_input("Exercise Duration (minutes)", 1, 120, 30)
heart_rate = st.number_input("Heart Rate", 50, 200, 110)
body_temp = st.number_input("Body Temperature (°C)", 35.0, 43.0, 40.0)

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

    prediction = model.predict(user_data)[0]

    st.success(f"Predicted Calories Burnt: {prediction:.2f} kcal")
