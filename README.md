# 💧 Water Quality Anomaly Detection System

## 📌 Overview

This project implements an anomaly detection system for water quality monitoring using the Isolation Forest algorithm. The model learns the normal behavior of water quality parameters from data and identifies unusual patterns without requiring labeled data.

A simple web application is developed using Streamlit to allow users to input water parameters and instantly check whether the values are normal or anomalous.

---

## 🧠 Methodology

The system uses an unsupervised machine learning approach:

* Model: Isolation Forest
* Preprocessing: StandardScaler
* Input: Key water quality parameters
* Output:

  * `1` → Normal
  * `-1` → Anomalous

---

## 📊 Features Used

The model is trained using the following parameters:

* pH
* Dissolved Oxygen
* Temperature
* Salinity
* Turbidity
* Chlorophyll

---

## 🚀 Features

* Manual input of water quality parameters
* Real-time anomaly detection
* Simple and interactive interface
* No labeled data required

---

## 🗂️ Project Structure

```id="z0y91m"
project/
│── app.py
│── if_model.pkl
│── scaler.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Install dependencies

```id="n2iqjo"
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```id="c7nlzb"
streamlit run app.py
```

---

## 📌 How to Use

1. Run the Streamlit app
2. Enter water quality values
3. Click **Check**
4. View result:

   * ✅ Normal
   * 🚨 Anomalous

---

## 📖 Academic Context

This project demonstrates the application of an unsupervised anomaly detection model for environmental monitoring. The system learns normal water quality conditions from data and identifies deviations in real-time.

---

## 👩‍💻 Author

Rida Fatma

---

## 📜 License

This project is developed for academic purposes.
