# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 13:57:49 2025

@author: user
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/user/Desktop/learning/MY ML WEB APPS/multiple disease prediction web app/models and data/diabetes/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/user/Desktop/learning/MY ML WEB APPS/multiple disease prediction web app/models and data/heart disease/heart_disease_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           
                           icons=['activity', 'heart'],
                           
                           default_index = 0)
    
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancvies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
    diabetes_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if(diabetes_prediction[0] == 1 ):
            diabetes_diagnosis = 'The person is Diabetic'
            
        else:
            diabetes_diagnosis = 'The person is not Diabetic'
        
    st.success(diabetes_diagnosis)
    
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain Types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dL')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dL')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
        
    with col2:
        slope = st.text_input('Slope of The Peak Exercise ST Segment')
        
    with col3:
        ca = st.text_input('Major Vessels Colored by Flourosopy')
        
    with col1:
        thal = st.text_input('Thal: 0 = noraml; 1 = fixed defect; 2 = reversable defect')
        
    
    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        try:
            age = float(age)
            sex = int(sex)
            cp = int(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = float(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
            

            input_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            

            heart_prediction = heart_disease_model.predict(input_data)
            

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        
        except ValueError:
            heart_diagnosis = "Please enter valid numeric values for all fields."
            
    st.success(heart_diagnosis)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        