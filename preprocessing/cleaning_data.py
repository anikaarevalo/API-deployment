#!/usr/bin/env python
# coding: utf-8

# ## **I. DATA PREPARATION PIPELINE**

# ## Data tools and file handling

# In[ ]:


# Importing python data analysis tools and a library to access & load relevant data set
# Choosing plot style as well 
from sklearn import datasets
import pandas as pd
import numpy as np
import seaborn as sns
sns.set(color_codes=True)

import matplotlib.pyplot as plt
plt.style.use('ggplot')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[58]:


# Accessing the cleaned data set (originally web scraped from immoweb.be) of house listings from a csv file 
# and passing it into a pandas dataframe
# Printing all the field names of all the columns in the data.
with open('/Users/anix/GNT-Arai-3/content/00.projects/2ndindproj/preprocessing/baseline.csv', 'r') as csvfile:
    df = pd.read_csv(csvfile, index_col=[0])
print(df.columns.values) 


# In[34]:


# Getting a glimpse of the raw data set through a pandas data frame
df.head()


# In[35]:


# Determining the number of rows and columns
df.shape


# ## Exploratory Data Analysis (EDA)

# ### NUMERICAL EDA

# ### Count of unique values in each numerical variable

# In[73]:


# 'Price', 'Number of bedrooms', 'Living area', and 'Surface area land'
for i in df.columns[1:]:
    print (df[i].value_counts())
    print("\n")


# ### Discovering correlations

# To find out which features are strongly or weakly correlated, we can implement the pandas .corr() method.
# This will guide us particularly when we get to the the maching learning modelling pipeline. 

# In[36]:


# Looking at possible correlations among the numerical variables
# In the next step, we shall visualise the features that have stong positive correlations
print(df.corr())


# **KEY INSIGHTS:**
# 
# All numerical variables that will be treated as features and are weakly-to-moderately correlated with one another 
# which is a good for an upcoming predictive model.
#  
# In a coefficient-based feature selection, the goal is to find **a feature subset with low feature-feature correlation**, to avoid redundancy, and **high feature-class correlation** to maintain or increase predictive power.
# It would be good to take note of these points when we proceed to the **II. MODELLING PIPELINE.***

# ### Statistical information about the price

# In[74]:


# Determining the mean, median, and mode of the values of 'Price' via pandas functions
print(df['Price'].mean())
print(df['Price'].median())
print(df['Price'].mode())


# ### VISUAL EDA

# ### Distribution of data under each numerical variable 

# In[37]:


#Visualising the distribution of numerical attributes 'Price', 'Number of bedrooms', Living area', 
# and 'Surface area land'
for i in df.columns[1:]:
    plt.hist(df[i])
    plt.title(i)
    plt.show()


# **INSIGHT:**
# **The distribution of numerical attributes 'Price', 'Number of bedrooms', Living area', 
# and 'Surface area land'are all normal. 

# ### Correlation plot among numerical variables

# In[28]:


# Using python data visualisation libeary, Seaborn, to plot and show the correlation among the numerical variables
print(df.corr())
sns.heatmap(df.corr())


# ### Visualising 'Price' in terms of mean, median and mode

# In[59]:


# Taking a loser look at the distribution by plotting a simple histogram with 10 bins.

plt.figure(figsize=(20,10));  
plt.hist(df['Price'], color='r');  
plt.axvline(df['Price'].mean(), color='m', linewidth=3,label='Mean') 
plt.axvline(df['Price'].median(), color='b', linestyle='dashed', linewidth=3,label='Median') 
plt.axvline(df['Price'].mode()[0], color='g', linestyle='dashed', linewidth=3,label='Mode') 

plt.title('Sale price for houses in Belgium')
plt.xlabel('Price')   
plt.ylabel('Number of houses')  
plt.legend()      

mean=round(df['Price'].mean())
median=round(df['Price'].median())
mode=round(df['Price'].mode())


# **Observation:**
# 
# - In the above histogram we can see that the third bin with the price of 300,00 has the most number of observations.
# - The majority of the observations lie within the second to fourth bin.
# - The **mean is 319,597 euros (almost 320,000 euros)** while the **median and mode are 299,000 euros (almost 300,000 euros)**.

# ## Function cleaning new data based on the parameters applied to baseline df

# In[ ]:


# The purpose of this function is to take a new house's data as input and return those data preprocessed as output.
# This is a nested function having underlying functions that would be executed in order to output a new data frame
# based on the original baseline data frame but with the new data that is cleaned first before appending to said copy
# of the data frame.
def preprocess(df):
    new_df = df.copy()
    """
    There is a need to create a copy of the original data frame before any data cleaning can be implemented
    on data received via a web form that satisfies and conforms to all the fields in the original data frame
    """
    # Implementing subfunction that converts strings values to integer
    new_df['Number of bedrooms'] = new_df['Number of bedrooms'].apply(StringtoInt)
    new_df['Living area'] = new_df['Living area'].apply(StringtoInt)
    new_df['Surface area land'] = new_df['Surface area land'].apply(StringtoInt)
    
    # Implementing subfunction that drops undesired columns in accordance with baseline data frame fields
    new_df = DropColumns(new_df)

    # Implementing subfunction that returns new data frame after discarding unkown or empty fields from some columns
    # and replacing mean values on other columns 
    new_df = imputeAndClean(new_df)
    
    return new_df


# In[ ]:


def StringtToInt(X : int):
    """
    This function receives a value X and converts it to an integer
    while 'unknown' or NaN values to 0
    """    
    if not X:
         return 0
    else: 
        return 1


# In[ ]:


# This function returns a data frame only with the columns I retained and used in creating and training a machine
# learning model
def DropColumns(df):
    """
    This function receives a df and returns a new df without certain columns and with only residential_sale as Type of Sale 
    """
    new_df = df.copy()
    new_df = new_df.drop(columns = ['Unnamed: 0', 'Location', 'Property subtype', 'Type of sale', 'Kitchen' 'Furnished' 'Open fireplace', 'Terrace' 'Terrace orientation' 'Garden' 'Garden orientation', 'Number of facades' 'Pool' 'Condition' ], axis = 1)
    
    return new_df


# In[ ]:


def CleanandImpute(df):
    """
    This function cleans and imputes on baseline data frame; That is, it returns a new df 
    after eliminating unknown and missing fields from some columns and 
    imputing median values on 'Living area' and 'Surface area land'
    """
    new_df = df.copy()
    # Dropping properties with a blank price
    new_df = new_df.dropna(subset=['Price'])
    # Imputing missing values on 'Living area' and 'Surface area land' by mean
    mean_areas = new_df['Living area', 'Surface area land'].mean()
    # Printing(str(int(mean_areas)))
    new_df['Living area', 'Surface area land'] = new_df['Living area', 'Surface area land'].fillna(int(mean_areas))

    return new_df

