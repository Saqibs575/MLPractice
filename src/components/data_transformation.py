import os
import numpy
import pandas
from src.logger import logging
from src.utils import save_object
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from src.exceptions import CustomException
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder


@dataclass
class DataTransformationConfig :
    preprocessor_file_path = os.path.join('artifacts' , 'preprocessor.pkl')

class DataTransformation :
    def __init__(self) :
        self.data_transformation_config = DataTransformationConfig()
    
    def data_transformation(self) :
        try :
            logging.info('Data Transformation Started') 

            categorical_columns = ['cut', 'color', 'clarity']
            numerical_columns = ['carat', 'depth', 'table']

            # Arranging Categorical variable in the order.
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

            logging.info('Pipeline Started')

            # Numerical Pipeline
            numerical_pipeline = Pipeline(
                steps = 
                [
                    ('Fill_NA' , SimpleImputer(strategy = 'median')) , 
                    ('feature_scaling' , StandardScaler())
                ]
            )

            # Categorical Pipeline
            categorical_pipeline = Pipeline(
                steps = 
                [
                    ('Fill_NA' , SimpleImputer(strategy = 'most_frequent')) ,
                    ('Encoding' , OrdinalEncoder(categories = [cut_categories , color_categories , clarity_categories])) ,
                    ('feature_scaling' , StandardScaler())
                ]
            )

            # Now Combining Numerical and Categorical Pipeline
            preprocessor = ColumnTransformer(
                [
                    ('numerical_pipeline' , numerical_pipeline , numerical_columns) , 
                    ('categorical_pipeline' , categorical_pipeline , categorical_columns)
                ]
            )
            
            logging.info('Pipeline Completed')
            return preprocessor

        except Exception as e :
            logging.info('Error Occured in Data Transformation')
            CustomException(e , sys)

    def initiate_data_transformation(self , train_path , test_path) :
        try :
            logging.info('initiate_data_transformation mathod started')
            train_df = pandas.read_csv(train_path)
            test_df = pandas.read_csv(test_path)

            train_df = train_df.drop(columns = ['id' , 'x' , 'y' , 'z'])
            test_df = test_df.drop(columns = ['id' , 'x' , 'y' , 'z'])

            input_train = train_df.drop(columns = ['price'])
            target_train = train_df['price']

            input_test = test_df.drop(columns = ['price'])
            target_test = test_df['price']

            logging.info('train and test data read')
            logging.info(f'\nTrain Data : \n{train_df.head()}\nTest Data : \n{test_df.head()}')

            logging.info('Preprocessing Started')
            preprocessor_obj = self.data_transformation()
            input_train_arr = preprocessor_obj.fit_transform(input_train)
            input_test_arr = preprocessor_obj.transform(input_test)

            train_arr = numpy.c_[input_train_arr , numpy.array(target_train)]
            test_arr = numpy.c_[input_test_arr , numpy.array(target_test)]

            save_object(
                self.data_transformation_config.preprocessor_file_path
                , preprocessor_obj)

            logging.info('Preprocessor pickle file saved')

            return (
                train_arr , 
                test_arr ,
                self.data_transformation_config.preprocessor_file_path
            )

        except Exception as e :
            logging.info('Error Occured in initiate_data_transformation method')
            print(CustomException(e, sys))