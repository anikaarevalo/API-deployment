#!/usr/bin/env python
# coding: utf-8

# ## House price calculator software

# In[1]:



import pandas as pd
import sys
import json
import joblib 
from predict.predict import predict

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
             'Number of bedrooms':str(number_rooms), 'Living area':str(living_area),'Surface area land':str(surface_area) 
            }
            
            
            df = pd.DataFrame(data, index=list(range(len(data))))
            result_price = predict(df)
            return render_template("result.html", result = result_price )

    if request.method == 'GET':
        return render_template("index.html")
    

if __name__ == '__main__':
   app.run(debug=True, port=8000)


# In[ ]:




