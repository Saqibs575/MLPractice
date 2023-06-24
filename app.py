import sys
from flask import Flask
from flask import request
from flask import render_template
from src.exceptions import CustomException
from src.pipeline.prediction_pipeline import CustomData
from src.pipeline.prediction_pipeline import PredictionPipeline

def convert(num) :
    if '.' in num :
        return float(num)
    return int(num)

app = Flask(__name__)
@app.route('/') 
def home_page() :
    return render_template('home_page.html')

print(int(float('2.00001')) == float('2.0'))
@app.route('/prediction' , methods = ['GET' ,'POST']) 
def predict() :
    if request.method == 'GET' :
        return render_template('index.html')

    try :
        input_data = CustomData(
            carat = convert(request.form.get('carat')),
            cut = request.form.get('cut'), 
            color = request.form.get('color'),
            clarity = request.form.get('clarity'), 
            depth = convert(request.form.get('depth')), 
            table = convert(request.form.get('table'))
            )

        input_df = input_data.to_dataframe()
        predicted = PredictionPipeline().predict(input_df)

        return render_template(
            'index.html' , 
            result = round(predicted[0][0] , 2) , 
            carat = input_data.carat ,
            depth = input_data.depth ,
            table = input_data.table ,
            clarity = input_data.clarity ,
            color = input_data.color ,
            cut = input_data.cut
            )
    except Exception as e :
        print(CustomException(e, sys))
        return render_template('index.html')

if __name__ == '__main__' :
    app.run(host = '0.0.0.0' , port = 5000)