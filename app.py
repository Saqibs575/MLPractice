import sys
from flask import Flask
from flask import request
from flask import render_template
from src.exceptions import CustomException
from src.pipeline.prediction_pipeline import CustomData
from src.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)
@app.route('/') 
def home_page() :
    return render_template('home_page.html')

@app.route('/prediction' , methods = ['GET' ,'POST']) 
def predict() :
    if request.method == 'GET' :
        return render_template('index.html')

    try :
        input_data = CustomData(
            carat = float(request.form.get('carat')),
            cut = str(request.form.get('cut')), 
            color = str(request.form.get('color')),
            clarity = str(request.form.get('clarity')), 
            depth = float(request.form.get('depth')), 
            table = float(request.form.get('table'))
            )

        input_df = input_data.to_dataframe()
        predicted = PredictionPipeline().predict(input_df)

        return render_template('index.html' , result = round(predicted[0][0] , 2))
    except Exception as e :
        print(CustomException(e, sys))
        return render_template('index.html')

if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5000)