import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💻",
    layout="centered"
)

# Load trained model
@st.cache_resource
def load_model():
    model_path = Path(__file__).parent / "salary_model.pkl"
    return joblib.load(model_path)

model = load_model()

# Read the categories directly from the trained model,
# so every option shown to the user is one the model knows.
encoder = (
    model.named_steps["Transformer"]
    .named_transformers_["cat"]
    .named_steps["OneHot"]
)
countries, education_levels = [list(c) for c in encoder.categories_]

# Application Title
st.title("Salary Prediction 💻")
st.write("Predict a programmer's estimated yearly salary (USD)")

# User Inputs
country = st.selectbox("Country", options=countries)

education = st.selectbox("Education Level", options=education_levels)

experience = st.slider(
    "Years of Coding Experience",
    min_value=0,
    max_value=50,
    value=3
)

# Prediction
if st.button("Calculate Salary"):

    x_new = pd.DataFrame({
        "Country": [country],
        "EdLevel": [education],
        "YearsCode": [experience]
    })

    salary = max(0, model.predict(x_new)[0])

    st.success(f"Estimated Salary: ${salary:,.0f}")
    st.caption("This is only a rough estimate based on survey data.")