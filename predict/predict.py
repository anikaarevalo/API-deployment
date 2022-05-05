#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing python data analysis tools and relevant machine-learning libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import joblib

# A function that predicts label (price) when user inputs according to the parameters of the linear regression model
def predict(user_data):    
    
    LR =  joblib.load('./predict/predict.sav')

    # Predicting on test set
    y_prediction =  LR.predict(user_data)
    
    # Returning prediction of label (price)
    return y_prediction

# Calling the prediction of the label (price) after user data is put in in the form of a numpy array
predict(np.array([3,167,370]).reshape(1, -1))

