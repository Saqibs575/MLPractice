## Introduction :
The Purpose of the project is to prdict the price of the Diamond Based on various features like Carat , Depth , Table , Color etc. Since the price is continuos value, hence we will use Regression to solve this. We will use Supervised Machine Learning Teachnique like Linear Regression , Lasso Regression etc. First we will collect the dataset from kaggle and then will do preprocessing. That is Exploratory Data Analysis (EDA) , Feature Engineering that is Feature selection and Feature Scaling and Imputation in case of missing values. After Preprocessing (Data Cleaning) we will use the cleaned data for the model training and then after model evaluation we will select best out of these.
## Gemstone Data Set
[CLICK HERE FOR KAGGLE DATA SET LINK](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

## About Data Set
* **price** : Price of the Diamond

 * **carat** : Weight of the Diamond

 * **cut** : Quality of the cut ( Fair , Good , Very Good , Premium , Ideal ) --> Ordinal Classification Worst to Best

 * **color** : Diamond Colour, from J ( worst ) to D ( best )

 * **clarity** : A measurement of how clear the Diamond is ( I1,SI2 ,SI1 ,VS2 ,VS1 ,VVS2 ,VVS1 ,IF ) --> Ordinal Categories Worst to Best.

 * **x** : Diamond Length in mm

 * **y** : Diamond Width in mm ( 0 - 58.9 )

 * **z** : Diamond Depth in mm ( 0 - 31.8 )

 * **depth** : Total depth in percentage 

 * **table** : Width of top of Diamond relative to widest point

# Requirements
- [sklearn](https://scikit-learn.org/stable/)
- [pandas](https://www.w3schools.com/python/pandas/default.asp)
- [flask](https://flask.palletsprojects.com/en/2.3.x/)
- [seaborn](https://seaborn.pydata.org/)
- [python](https://www.python.org/)

# Installation and Usage

To install webApp, follow these steps:

Environment Setup
```
conda create -p venv python==3.8
```
```
conda activate venv/
```

1. Clone the repository:
```
git clone https://github.com/Saqibs575/DiamondPricePrediction.git
```

2. Navigate to the project directory:
```
cd DiamondPricePrediction
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Set up :
```
python application.py
```
5. Start the server:
```
http://127.0.0.1:5000/
```




# Home Page UI
![image](https://github.com/Saqibs575/MLPractice/assets/111361057/09168b8f-4542-4ca5-9ca0-54bf6341e8ac)
# Prediction Page UI
![image](https://github.com/Saqibs575/MLPractice/assets/111361057/9ab05ef6-ce86-411f-a6c7-818872b01d83)
