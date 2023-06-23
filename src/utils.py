import os
import sys
import pickle
from src.logger import logging
from sklearn.metrics import r2_score
from src.exceptions import CustomException

def save_object(file_path , obj) :
    try :
        os.makedirs(os.path.dirname(file_path) , exist_ok = True)
        with open(file_path , 'wb') as file :
            pickle.dump(obj, file)

    except Exception as e :
        print(CustomException(e, sys))

def evaluate_model(X_train , y_train , X_test , y_test , models) :
    try :
        model_perfomance = {}
        for i in models :
            model = models[i]
            model.fit(X_train , y_train)
            y_predicted = model.predict(X_test)
            model_perfomance[i] = r2_score(y_test , y_predicted)
        logging.info('Model Evaluation completed')
        return model_perfomance
        

    except Exception as e :
        logging.info('Error Occured in evaluate_model method')
        print(CustomException(e, sys))

def load_object(file_path) :

    try :
        with open(file_path , 'rb') as file :
            return pickle.load(file)

    except Exception as e :
        print(CustomException(e, sys))