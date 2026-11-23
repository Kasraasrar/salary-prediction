# Salary Prediction

A Machine Learning project that predicts a programmer's annual salary based on their country, education level, and years of coding experience.

## Dataset

This project uses the Stack Overflow Developer Survey 2025 dataset.

**Official Source:** [Stack Overflow Developer Survey 2025](https://survey.stackoverflow.co/2025/)

**Direct Download:** [Download CSV Dataset](https://media.githubusercontent.com/media/StackExchange/Survey/refs/heads/main/packages/archive/2025/results.csv)

The dataset is used for data preprocessing, exploratory data analysis, and salary prediction.

## Project Overview

This project explores salary prediction using real-world data. It includes data preprocessing, exploratory data analysis, model comparison, hyperparameter tuning, and model evaluation.

## Project Structure

- `project-3.ipynb` – Data analysis, preprocessing, model training, and evaluation.
- `app.py` – Interactive web application for salary prediction.
- `salary_model.pkl` – Trained machine learning model.
- `requirements.txt` – Project dependencies.

## How to Run

1. Clone the repository:
   ```bash
git clone https://github.com/Kasraasrar/salary-prediction.git
```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```
