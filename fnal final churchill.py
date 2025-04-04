# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:20:07 2025

@author: HomePC
"""

import numpy as np
import streamlit as st
import pickle


# loading the saved model
loaded_model = pickle.load(open(r"C:\Users\HomePC\ML FINAL\trained_model (1).sav", 'rb'))

##Create a function for prediction
def diabetes_prediction(input_data):
 
 
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
   
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
   
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return('The person is not diabetic')
    else:
        return('The person is diabetic')

def main():
    ##giving a title to our UI interface
    st.title('Diabetes Prediction Web App')
   
    ##We want to get the input data
    Pregnancies=st.text_input('Number of pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('BloodPressure levels')
    SkinThickness=st.text_input('skin thickness value')
    Insulin=st.text_input('Insulin levels')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    Age=st.text_input('Age value')
   
    #code for prediction
    diagnosis=''
   
    #creating a button for prediction
    if st.button('diabetes_test_result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
   
    st.success(diagnosis)
   
if __name__=='__main__':
    main()