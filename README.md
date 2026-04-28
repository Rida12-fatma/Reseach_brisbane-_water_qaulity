# 💧 Water Quality Anomaly Detection using Isolation Forest

## 📌 Overview

This project implements an anomaly detection system for water quality data using the Isolation Forest algorithm. The model identifies unusual or abnormal patterns in environmental parameters without requiring labeled data.

A simple web application is built using Streamlit to allow users to upload new datasets and detect anomalies in real time.

---

## 🧠 Model

The anomaly detection is performed using:

* Isolation Forest (Unsupervised Machine Learning)
* Detects anomalies based on data isolation rather than labels

Output:

* `-1` → Anomaly
* `1` → Normal data

---

## 🚀 Features

* Upload water quality dataset (CSV format)
* Automatic anomaly detection
* Displays full dataset with anomaly labels
* Highlights anomalous observations
* Simple and interactive UI

---

## 🗂️ Project Structure

```
project/
│── app.py                # Streamlit application
│── if_model.pkl          # Trained Isolation Forest model
│── requirements.txt      # Dependencies
│── README.md             # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

The app will open in your browser.

---

## 📊 How to Use

1. Launch the Streamlit app
2. Upload a CSV file containing water quality data
3. View:

   * Data preview
   * Anomaly detection results
   * Rows flagged as anomalies

---

## ⚠️ Important Notes

* Input data must match the format used during model training
* Only numerical features should be included
* Preprocessing (if any) should be consistent with training

---

## 🌐 Deployment

The application can be deployed using:

* GitHub (for version control)
* Streamlit Cloud (for online hosting)

---

## 📖 Academic Context

This project was developed as part of a research study on unsupervised anomaly detection in water quality monitoring systems. The deployment demonstrates the practical applicability of the model on unseen data.

---

## 👩‍💻 Author

Rida Fatma

---

## 📜 License

This project is for academic and research purposes.
