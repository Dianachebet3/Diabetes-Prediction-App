# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:18:35 2025

@author: HomePC
"""

import numpy as np
import streamlit 
import pickle
import streamlit as st

#loading saved model
loaded_model = pickle.load(open(r"C:\Users\HomePC\ML FINAL\trained_model (1).sav", 'rb'))

#Create a function for prediction

def diabetes_prediction(input_data):
    
    # changing the input_data to numpy array
    
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    if (prediction[0] == 0):
        
    return('The person is not diabetic')
    
    else:
        
    return('The person is diabetic')

def main():
    
    #giving a title to our UI interface
    st.title('Diabetes Prediction Web App')
  
    #We want to create/get the input data,was gotten from the excel sheet
    Pregnancies.text_input('Number of pregnancies')
    Glucose.text_input('Glucose Level')
    BloodPressure.text_input('BloodPressure Levels')
    SkinThickness.text_input('skin thickness value')
    Insulin.text_input('Insulin Levels')
    BMI.text_input('BMI value')
    DiabetesPedigreeFunction.text_input('Diabetes Pedigree Function value')
    Age_input('Age value')
    
    #Code for prediction-we create an empty string that we will use for prediction
    diagnosis=''
    
    #creating button for prediction
    if st.button('diabetes_test_result'):
        diagnosis=('Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age')
        
        #closing our function
        st.success(diagnosis)
        
if __name__=='__main__':
    main()