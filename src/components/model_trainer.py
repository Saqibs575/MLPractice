import os
import sys
import numpy
import pandas
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass
from src.utils import evaluate_model
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from src.exceptions import CustomException
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import LinearRegression


@dataclass
class ModelTrainerConfig :
    model_trainer_file_path = os.path.join('artifacts' , 'model.pkl')

class ModelTrainer :
    def __init__(self) :
        self.model_trainer_config = ModelTrainerConfig() 

    def initiate_model_training(self , train_arr , test_arr) :
        try :
            logging.info('Train Test Split Starts ')
            X_train , y_train , X_test , y_test = (
                train_arr[ : ,   :-1],
                train_arr[ : , -1:  ],
                test_arr[ : , : -1] ,
                test_arr[ : , -1: ] ,
            ) 

            models = {
                'LinearRegression' : LinearRegression() ,
                'ElasticNet' : ElasticNet() ,
                'Ridge' : Ridge() ,
                'Lasso' : Lasso()

            }

            model_perfomance : dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            logging.info(f'Model_perfomance : {model_perfomance}')

            best_score = max(model_perfomance.values())
            idx = list(model_perfomance.values()).index(best_score)
            best_model_name = list(model_perfomance.keys())[idx]
            best_model = models[best_model_name]

            save_object(
                self.model_trainer_config.model_trainer_file_path,
                best_model
                )
            logging.info(f'Best Model : {best_model} , R2 Score : {best_score}')

        except Exception as e :
            logging.info('Exception Occured in initiate_model training method')
            print(CustomException(e, sys))
