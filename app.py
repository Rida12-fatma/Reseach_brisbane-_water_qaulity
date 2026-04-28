import streamlit as st
import numpy as np
import joblib

# Page config
st.set_page_config(
    page_title="Water Quality Anomaly Detection System",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f9f9f9;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}

.result-normal {
    padding: 20px;
    border-radius: 10px;
    background-color: #e6f4ea;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    color: #1b5e20;
}

.result-anomaly {
    padding: 20px;
    border-radius: 10px;
    background-color: #fdecea;
    text-align: center;
    font-size: 20px;
    font-weight: 600;
    color: #b71c1c;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>Water Quality Anomaly Detection System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Enter water quality parameters to evaluate system behavior</div>", unsafe_allow_html=True)

# Load model
model = joblib.load("if_model.pkl")
scaler = joblib.load("scaler.pkl")

# Input section
st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    pH = st.number_input("pH", value=8.1)
    DO = st.number_input("Dissolved Oxygen", value=7.4)
    Temp = st.number_input("Temperature (°C)", value=20.0)

with col2:
    Salinity = st.number_input("Salinity", value=35.2)
    Turbidity = st.number_input("Turbidity", value=2.0)
    Chlorophyll = st.number_input("Chlorophyll", value=1.6)

st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# Button
check = st.button("Check Water Quality", use_container_width=True)

# Result
if check:
    input_data = np.array([[pH, DO, Temp, Salinity, Turbidity, Chlorophyll]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.write("")

    if prediction[0] == 1:
        st.markdown("<div class='result-normal'>Normal Water Quality</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='result-anomaly'>Anomalous Water Quality</div>", unsafe_allow_html=True)

# Footer
st.write("")
st.markdown("<div style='text-align:center; font-size:12px; color:#888;'>Isolation Forest-based anomaly detection for water quality analysis</div>", unsafe_allow_html=True)
