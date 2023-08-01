# -*- coding: utf-8 -*-
"""iris_app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ur83UmePKpqyP6x1zudi3OWgyBObJjWr
"""

import streamlit as st
import numpy as np
import joblib

#Interface

st.markdown ('## Iris Species Prediction')
sepal_length= st.number_input('sepal length (cm)')
sepal_width = st.number_input('sepal width (cm)')
petal_length = st.number_input('petal length (cm)')
petal_width = st.number_input('petal width (cm)')

 #Predict button
if st.button( 'Predict'):
    model = joblib.load('iris_model.pk1')
    X = np.array([sepal_length, sepal_width, petal_length, petal_width])
    if any (X <= 0):
         st.markdown('### Inputs must be greater than 0')
    else:
         st.markdown (f'### Prediction is{model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]}')