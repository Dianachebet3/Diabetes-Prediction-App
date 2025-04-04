# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import streamlit 
import pickle

loaded_model = pickle.load(open(r"C:\Users\HomePC\ML FINAL\trained_model (1).sav", 'rb'))
#Create a function for prediction
def diabetes_prediction(input_data):



# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The person is not diabetic')
else:
  return('The person is diabetic')