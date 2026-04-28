import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Water Quality Anomaly Detection System")

st.title("💧 Water Quality Anomaly Detection System")
st.write("Enter water quality parameters to check if they are normal or anomalous.")

# Load model and scaler
model = joblib.load("if_model.pkl")
scaler = joblib.load("scaler.pkl")

st.subheader("Input Parameters")

# Input fields (same order as training)
pH = st.number_input("pH", value=8.1)
DO = st.number_input("Dissolved Oxygen", value=7.4)
Temp = st.number_input("Temperature", value=20.0)
Salinity = st.number_input("Salinity", value=35.2)
Turbidity = st.number_input("Turbidity", value=2.0)
Chlorophyll = st.number_input("Chlorophyll", value=1.6)

if st.button("Check Water Quality"):

    # Arrange input in correct order
    input_data = np.array([[pH, DO, Temp, Salinity, Turbidity, Chlorophyll]])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.success("✅ Normal Water Quality")
    else:
        st.error("🚨 Anomalous Water Quality")
