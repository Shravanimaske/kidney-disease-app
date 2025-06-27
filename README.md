# Kidney-Disease-Prediction

Kidney disease is a growing health concern worldwide, especially with increasing rates of diabetes and hypertension. Early detection and intervention are crucial to managing and potentially reversing kidney damage. This project uses a machine learning model to predict the presence of kidney disease based on a few simple patient parameters. It is deployed as an interactive web application using Streamlit.

---

## Objective

Given basic patient input such as age, white blood cell count, and medical history (hypertension and diabetes), the model predicts whether the patient is likely to have kidney disease.

The goal is to support healthcare professionals with a quick, accessible decision-support tool that can help prioritize further clinical investigation.

---

##  Input

The following inputs are required:
- Age of the patient
- White cell count (WC)
- Hypertension status (`yes` / `no`)
- Diabetes mellitus status (`yes` / `no`)

---

##  Output

The model provides a binary prediction based on clinical input data:

 - Kidney disease found

 - Kidney disease is not detected

The prediction result is displayed in a user-friendly message through the Streamlit interface, making it accessible even to non-technical users.
---

##  Model Performance
The model used is a trained classification model built with scikit-learn, and evaluated using standard classification metrics such as Accuracy, Precision, Recall, and F1 Score. Among various algorithms tested, the Random Forest Classifier demonstrated the best performance on the test data.
- Accuracy	99.11%
- Precision	99.33%
- Recall	99.33%
- F1 Score	99.31%

The goal is to minimize false negatives — ensuring patients with kidney disease are flagged for follow-up.

---
## Project Structure
├── app.py # Streamlit frontend
├── classifier.pkl # Trained machine learning model
├── requirements.txt # Required Python packages
└── README.md # Project overview


## Dataset
The dataset used for this project contains anonymized patient records with various clinical parameters related to kidney function. It includes features such as:
- Age
- Blood pressure
- White cell count (WC)
- Hypertension status
- Diabetes mellitus status
Other clinical indicators (not all used in final model)

This dataset was sourced from UCI Machine Learning Repository. Source = https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease  A publicly available collection of chronic kidney disease data. It contains 400 records and 24 attributes, including the target classification.
