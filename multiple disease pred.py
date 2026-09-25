# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 02:11:37 2026

@author: Divya
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(
    open("diabetes_model.sav", "rb")
)

parkinsons_model = pickle.load(
    open("parkinsons_model.sav", "rb")
)

heart_disease_model = pickle.load(
    open("heart_disease_model.sav", "rb")
)

# Sidebar for navigation

with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System using ML',
        ['Diabetes Prediction',
         'Heart Disease Prediction',
         'Parkinsons Prediction'],
        
        icons = ['activity','heart','person'],
        default_index=0
    )
    
    

# Diabetes prediction page

if selected == 'Diabetes Prediction':
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    
    #getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    
    if st.button('diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is not Diabetic'
    st.success(diab_diagnosis)        
    
 

# Heart Disease prediction page

if selected == 'Heart Disease Prediction':
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age= st.text_input("Age")
        
    with col2:
        sex = st.text_input('sex')
    with col3:
        cp = st.text_input('chest pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dL')
        
    with col3:
        fbs = st.text_input('Fasting Blood sugar > 120 mg/Dl')
        
    with col1:
        restacg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thelach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression Induced Angina ')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca =st.text_input('Major vesels colored by flourosopy')
    with col1:
        tha1 = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
    #code for prediction
    heart_diagnosis = ''
    #creating a button for prediction
    if st.button('Heart Disease Tet Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restacg, thelach, exang, oldpeak, slope, ca, tha1]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    st.success(heart_diagnosis)         

# Parkinsons prediction page

if selected == 'Parkinsons Prediction':
    
    # page title
    st.title('Parkinsons Prediction using ML')
    
    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
        
    with col1:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')
        
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
        
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
        
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
        
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col1:
        spread1 = st.text_input('spread1')
        
    with col2:
        spread2 = st.text_input('spread2')
        
    with col3:
        D2 = st.text_input('D2')
        
    with col1:
        PPE = st.text_input('PPE')
    
    
    # code for prediction
    parkinsons_diagnosis = ''
    
    # creating a button for prediction
    if st.button('Parkinsons Test Result'):
        
        parkinsons_prediction = parkinsons_model.predict([[
            MDVP_Fo,
            MDVP_Fhi,
            MDVP_Flo,
            MDVP_Jitter,
            MDVP_Jitter_Abs,
            MDVP_RAP,
            MDVP_PPQ,
            Jitter_DDP,
            MDVP_Shimmer,
            MDVP_Shimmer_dB,
            Shimmer_APQ3,
            Shimmer_APQ5,
            MDVP_APQ,
            Shimmer_DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE
        ]])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person is having Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons disease'
    
    st.success(parkinsons_diagnosis)
