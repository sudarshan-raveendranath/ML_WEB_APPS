# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 11:41:25 2025

@author: user
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/user/Desktop/learning/MY ML WEB APPS/diabetes prediction deploy/trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    prediction  = loaded_model.predict(input_data_reshaped) #using the loaded model to predict the input data
    
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    
def main():
    
    st.title('Diabetes Prediction Web App')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Level')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    
    diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()