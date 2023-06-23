import os
import sys
import pandas
from src.logger import logging
from src.utils import load_object
from src.exceptions import CustomException
class PredictionPipeline :
    def predict(self , features) :
        try :
            preprocessor_path = os.path.join('artifacts' , 'preprocessor.pkl')
            model_path = os.path.join('artifacts' , 'model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)
            prediction = model.predict(data_scaled)

            return prediction

        except Exception as e :
            logging.info('Error occured in Predictio Pipeline')
            print(CustomException(e , sys))

class CustomData :
    def __init__(
        self ,
        carat : float ,
        cut : str ,
        color : str ,
        clarity : str ,
        depth : float ,
        table : float
        ) :
        self.carat = carat
        self.cut = cut
        self.color = color
        self.clarity = clarity
        self.depth = depth
        self.table = table

    def to_dataframe(self) :
        try :
            input_data = {
                'carat' : [self.carat] ,
                'cut' : [self.cut] ,
                'color' : [self.color] ,
                'clarity' : [self.clarity] ,
                'depth' : [self.depth ],
                'table' : [self.table]
            }

            df = pandas.DataFrame(input_data)

            return df

        except Exception as e :
            logging.info('Error Occured in to_dataframe method')
            print(CustomException(e, sys))
