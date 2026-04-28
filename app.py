import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Water Quality Checker")

st.title("An Isolation Forest-Based Water Quality Anomaly Detection System")

st.write("Enter water parameters to check if it's normal or anomalous.")

# Load model
model = joblib.load("if_model.pkl")

# 👉 INPUT FIELDS (CHANGE names according to YOUR features)
ph = st.number_input("pH", value=7.0)
do = st.number_input("Dissolved Oxygen (DO)", value=5.0)
turbidity = st.number_input("Turbidity", value=10.0)
temp = st.number_input("Temperature", value=25.0)
ec = st.number_input("Electrical Conductivity (EC)", value=300.0)
salinity = st.number_input("Salinity", value=0.5)

# Predict button
if st.button("Check Water Quality"):

    # Must match EXACT training order
    input_data = np.array([[ph, do, turbidity, temp, ec, salinity]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ This is NORMAL water quality")
    else:
        st.error("🚨 This is ANOMALOUS water quality")
