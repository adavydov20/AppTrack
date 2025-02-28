# AppTrack

## Overview

This project builds a machine learning model to predict the success of mobile apps based on various characteristics. It includes:

- **Web Scraping**: Collecting app data from Google Play Store.
- **Data Cleaning & Feature Engineering**: Processing scraped data.
- **Model Training**: Using Random Forest Classifier to predict app success.
- **API Deployment**: A Flask API for making predictions.
- **Web Dashboard**: A Streamlit app for interactive predictions.

---

## Project Structure

```
/app_success_prediction/
│── app_success_prediction.ipynb   # Jupyter Notebook (exploration & training)
│── models/                        
│   ├── app_success_model.pkl      # Trained model
│── data/                          
│   ├── finance_app_apps.csv        # Scraped dataset
│── api/                           
│   ├── app.py                     # API
│── dashboard/                     
│   ├── dashboard.py                # Dashboard
│── requirements.txt                # Dependencies
│── README.md                       # Project documentation
```

---

## 🚀 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Running the Jupyter Notebook
```bash
jupyter notebook app_success_prediction.ipynb
```

### 3. Running the Flask API
```bash
cd api
python app.py
```
The API will be available at: **http://127.0.0.1:5000/predict**

#### Example POST request:
```python
import requests

url = "http://127.0.0.1:5000/predict"
data = {"features": [5000, 100000, 4.5, 1200, 0]}  # Example input
response = requests.post(url, json=data)
print(response.json())  # Output: {"success_prediction": 1 or 0}
```

### 4. Running the Streamlit Dashboard
```bash
cd dashboard
streamlit run dashboard.py
```
The dashboard will be available at **http://localhost:8501/**

Users can enter app features and receive a success prediction.

---

## Features & Technologies Used

- **Python** (pandas, scikit-learn, numpy, matplotlib, seaborn)
- **Google Play Scraper** for data collection
- **Flask API** for serving the model
- **Streamlit Dashboard** for visualization
