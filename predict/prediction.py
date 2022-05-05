#!/usr/bin/env python
# coding: utf-8

# ## A FUNCTION TO PREDICT A NEW HOUSE'S PRICE

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pickle


# In[ ]:

def predict_price():

    def train():
        # Importing data
        model_df = pd.read_csv('/Users/anix/API-deployment/preprocessing/baseline.csv', index_col=0)

        # Splitting dataset into X and y
        X = model_df.iloc[:, 2:5].values
        y = model_df.iloc[:,1].values

        # Splitting the data for cross validation
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

        # Creating model
        LR = LinearRegression()

        # Fitting model
        LR.fit(X_train,y_train)

    def test():
        # Predicting on test set
        y_prediction =  LR.predict(X_test)
        y_prediction
    
        # Printing accuracy
        score=r2_score(y_test,y_prediction)
        print('r2 score is', score)
        print('mean_sqrd_error is==', mean_squared_error(y_test,y_prediction))
        print('root_mean_squared error of is==', np.sqrt(mean_squared_error(y_test,y_prediction)))
    
        # Saving the model
        pickle.dump(LR, open('predict/prediction.pickle', 'wb'))
        print('Model saved.')
    

