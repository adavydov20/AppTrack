import os
import streamlit as st
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "../models/app_success_model.pkl")

model = joblib.load(model_path)

st.title("AppTrack: App Success Prediction")

reviews = st.number_input("Number of Reviews", min_value=0, step=100)
installs = st.number_input("Number of Installs", min_value=0, step=1000)
rating = st.slider("App Rating", 0.0, 5.0, 4.0)
desc_length = st.number_input("Description Length", min_value=0, step=10)
is_paid = st.selectbox("Is Paid App?", [0, 1])

if st.button("Predict Success"):
    features = np.array([reviews, installs, rating, desc_length, is_paid]).reshape(1, -1)
    prediction = model.predict(features)[0]

    st.write("**Predicted Success:**", "Likely Successful" if prediction else "Likely Unsuccessful")
