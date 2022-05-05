#!/usr/bin/env python
# coding: utf-8

# ## House price calculator software

# In[1]:


import numpy as np
import pandas as pd
import sys
import json
import joblib
import importlib.util  
#sys.path.append('./model')
#sys.path.append('./preprocessing')
sys.path.append('./predict')
#import preprocessing.cleaning_data as cleaning_data
import predict.predict as prediction
#from preprocessing.cleaning_data import checkData
#from preprocessing.cleaning_data import creatingDummies
from predict.predict import user_input
#import preprocessing.cleaning_data as cleaning_data
#import predict.prediction as prediction 

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def alive():
    return '<h1>This is server is alive!</h1>'


@app.route('/predict', methods=['POST','GET'])
def predict():
    """
    This function will be use for the prediction of property
    """
    
    if request.method == 'POST':
            number_rooms = request.form.get('bedrooms')
            living_area =  request.form.get('living_area')
            surface_area =  request.form.get('surface_area') 

            data = {
             'Number of bedrooms':str(bedrooms), 'Living area':str(living_area),'Surface area land':str(surface_area) 
            }
           
            if (validData == False):
                return render_template("result.html", result="Please fill in all fields")
            
            else:
                df = pd.DataFrame(data, index=list(range(len(data))))
                df = clean.creatingDummies(df)
                ##########################
                # passing the file name and path as argument
                spec1 = importlib.util.spec_from_file_location(
                    "prediction", "./predict/predict.py") 

                # importing the module as clean
                predicter = importlib.util.module_from_spec(spec1)       
                spec1.loader.exec_module(predicter)
                # calling predicted price
                predicted_price = predicter.predict_price(df)[0]
            ##################################    
               
               # predicted_price = prediction.predict(df)[0]
                
                result_price = "The price of your property is: "+ str("{:,.2f}".format(predicted_price)) + " EUR"
                return render_template("result.html", result = result_price )

    if request.method == 'GET':
        return render_template("index.html")
    

if __name__ == '__main__':
   app.run(debug=True)


# In[ ]:




