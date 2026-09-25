# 🏥 Multiple Disease Prediction System using Machine Learning

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" alt="Python">

  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge&logo=scikit-learn" alt="Machine Learning">

  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit" alt="Streamlit">

  <img src="https://img.shields.io/badge/NumPy-2.0.2-013243?style=for-the-badge&logo=numpy" alt="NumPy">

  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas" alt="Pandas">

</p>

<p align="center">
  <b>🩺 An interactive Machine Learning web application for predicting multiple diseases from medical input parameters.</b>
</p>

---

## 🌟 Project Overview

**Multiple Disease Prediction System** is a Machine Learning based web application that provides predictions for three different diseases:

- 🩸 **Diabetes**
- ❤️ **Heart Disease**
- 🧠 **Parkinson's Disease**

The application provides a simple and interactive interface where users can enter relevant medical parameters and receive a Machine Learning based prediction.

The project combines **Python, Machine Learning, Scikit-learn, Streamlit, NumPy and Pandas** to create an easy-to-use healthcare prediction application.

> ⚠️ **Disclaimer:** This project is developed for educational and demonstration purposes. The predictions should not be considered professional medical advice or a medical diagnosis.

---

# ✨ Features

### 🩸 Diabetes Prediction

Predicts whether a person is likely to have diabetes based on medical parameters such as:

- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

---

### ❤️ Heart Disease Prediction

Predicts the possibility of heart disease using parameters including:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope
- Major Vessels
- Thalassemia

---

### 🧠 Parkinson's Disease Prediction

Uses voice-related biomedical measurements to predict Parkinson's disease.

The model uses **22 numerical features**, including:

- MDVP:Fo(Hz)
- MDVP:Fhi(Hz)
- MDVP:Flo(Hz)
- MDVP:Jitter(%)
- MDVP:Jitter(Abs)
- MDVP:RAP
- MDVP:PPQ
- Jitter:DDP
- MDVP:Shimmer
- MDVP:Shimmer(dB)
- Shimmer:APQ3
- Shimmer:APQ5
- MDVP:APQ
- Shimmer:DDA
- NHR
- HNR
- RPDE
- DFA
- spread1
- spread2
- D2
- PPE

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────────────┐
                    │        👤 User               │
                    │   Enters Medical Parameters  │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │      🌐 Streamlit UI         │
                    │                              │
                    │  Disease Selection Menu      │
                    └──────────────┬───────────────┘
                                   │
                     ┌─────────────┼─────────────┐
                     │             │             │
                     ▼             ▼             ▼
              ┌────────────┐ ┌────────────┐ ┌──────────────┐
              │ 🩸 Diabetes │ │ ❤️ Heart   │ │ 🧠 Parkinson's│
              │    Input    │ │   Input    │ │     Input    │
              └──────┬─────┘ └──────┬─────┘ └───────┬──────┘
                     │              │               │
                     ▼              ▼               ▼
              ┌────────────┐ ┌────────────┐ ┌──────────────┐
              │ Diabetes   │ │   Heart    │ │ Parkinson's  │
              │ ML Model   │ │ Disease ML │ │   ML Model   │
              └──────┬─────┘ └──────┬─────┘ └───────┬──────┘
                     │              │               │
                     └──────────────┼───────────────┘
                                    ▼
                         ┌─────────────────────┐
                         │ 🤖 ML Prediction    │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ 📊 Prediction       │
                         │      Result         │
                         └─────────────────────┘
