# API Deployment: Immo Eliza house price calculator🏠🔢💶

## Description
**Immo Eliza**, a Belgian-based real esate company, wants to optimise their house pricing scheme. When a new property enters the market, they want
their staff to have a straightforward tool, **a web application**, where they can simply **enter a set of attributes** and the said software would 
**output a recommended sale price of a new property listing**. 

As a data scientist contracted for the job, my task is to build and deploy **three central pipelines** with the goal of delivering to my client a
a **usable and reliable predictive house pricing calculator**. 

<img width="668" alt="pipeline 2022-04-21 at 15 49 28" src="https://github.com/anikaarevalo/GNT-Arai-3/blob/962385ab35cfcac06c8381d028553eacc343f2b7/content/00.projects/2ndindproj/assets/Screenshot%202022-05-01%20at%2010.28.19.png">

**Pipeline 1:** 
DATA PREPARATION  

With the dataset that was previously scraped, the aim of the first pipeline is to **preprocess the data resulting to improved data quality**. 
Problemmatic/unsuitable data were eliminated so that the ***legitimate observations were captured***; the ***possible features (attributes) 
extracted***; and the ***label, extrapolated***.

**Piperline 2:** 
PREDICTIVE MODELLING

Using quality data, I initialised a **machine learning workflow** to create and train a **linear regression predictive model**.
Additionally, I subjected the model under evaluation, with the aim of configuring metrics that allowed the model to achieve the highest level
of reliability. 

**Pipeline 3:** 
WEB API DEPLOYMENT

Lastly, I created an **Application Programming Interface (API)** so that Immo Eliza's web-developers could create a website around the software.
The API, in particular, asks a user to provide certain information about a new property (features) and returns the estimated price using the 
embedded linear regression model.

## Installation
The following software and tools were utilised in this project:
1. **Data analysis**
- Python 3.9 or higher
- Pandas and Numpy
- Matplotlib and Seaborn

2. **Machine learning**
- Scitkit Learn

3. **Web application deployment**
- Flask 2.1.2
- Git Hub CLI
- Heroku CLI 7.60.2

## Usage
This is a plug-and-play web-based app that lets Immo Eliza listing agents help sellers price their property before any new listing can be released 
and properly staged in the market. 

**For this project, I have private individual (ordinary) sellers in mind who are likely to sell single property homes.** 

## Visuals

**(Pipeline 1)** Visual EDA, a heat map, showing the correlations among the numerical variables forming the baseline data frame
<img width="400" src="https://github.com/anikaarevalo/GNT-Arai-3/blob/bf5041f64dfe9cf7ce45dbc060a06f7c0b74e4f1/content/00.projects/2ndindproj/assets/heatmap.png">
  
 **(Piperline 2)** Multiple regression model: RSquared performance metric score at 22%
 ![This is a screenshot](https://github.com/anikaarevalo/API-deployment/blob/d26d04dd381e280b38217da79f59ba71bc1109e0/assets/r2score.png)
 
**(Pipeline 3)** Immo Eliza house price calculator interface 
<img width="800" src="https://github.com/anikaarevalo/API-deployment/blob/ddab2155ea791127385772410308572c59bf274c/assets/Immo%20Eliza%20UI.png">
                                                                                              
## Contributor
Anika Arevalo, Junior Data Scientist⚛️ (BeCode, Ghent)

## Timeline
6 days

28/04/2022 - 05/05/2022

## Personal Situation
BeCode, in partnership with a fictitious client Immo Eliza, assigned this project to me, an AI data ops learner, 
in order to apply methods and strategies in data perparation, machine learning modelling, and web application deployment. 

The main goal and focus of this project is to deploy software using web application tools such as Flask and Heroku. **In another opportunity,
I would love to have the chance to improve this prototype** by optimising the machine learning model that I had implemented (i.e. **including categorical
variables in combination with numerical variables** in training and testing the model and **improving its performance metrics**). 

The interface of the house price calculator could also be improved.

Suggestions are welcome. Thank you!✌️ 
