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
import pickle

# A function that predicts label (price) when user inputs accprding to the parameters of the linear regression model
def predict(user_data):    
    
    LR =  pickle.load(open('predict.sav', 'rb'))

    # Predicting on test set
    y_prediction =  LR.predict(user_data)
    
    
    # Printing accuracy
    #score=r2_score(y_test,y_prediction)
    #print('r2 score is', score)
    #print('mean_sqrd_error is==', mean_squared_error(y_test,y_prediction))
    #print('root_mean_squared error of is==', np.sqrt(mean_squared_error(y_test,y_prediction)))
    
    # Saving the model
    #print('Model saved.')
    return y_prediction

# Calling the prediction of the label (price) in the form of a numpy array
predict(np.array([3,167,370]).reshape(1, -1))

