import streamlit as st
import pandas as pd
import joblib

# Page title
st.set_page_config(page_title="Water Quality Anomaly Detection", layout="wide")

st.title(" Water Quality Anomaly Detection")
st.write("Upload your dataset to detect anomalies using Isolation Forest.")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("if_model.pkl")

model = load_model()

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Read data
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Data Preview")
        st.dataframe(df.head())

        # Ensure only numeric columns
        df_numeric = df.select_dtypes(include=["number"])

        if df_numeric.shape[1] == 0:
            st.error("❌ No numeric columns found in the dataset.")
        else:
            # Prediction
            predictions = model.predict(df_numeric)
            df["Anomaly"] = predictions

            st.subheader("✅ Detection Results")
            st.dataframe(df)

            # Show anomalies
            anomalies = df[df["Anomaly"] == -1]

            st.subheader("🚨 Detected Anomalies")
            st.write(f"Total anomalies detected: {len(anomalies)}")
            st.dataframe(anomalies)

            # Simple visualization
            if df_numeric.shape[1] >= 1:
                st.subheader("📈 Visualization")
                st.line_chart(df_numeric)

    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")

else:
    st.info("Please upload a CSV file to begin.")
