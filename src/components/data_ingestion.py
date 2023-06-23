import os
import sys
import pandas
from src.logger import logging
from dataclasses import dataclass
from src.exceptions import CustomException
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig :
    train_data_path : str = os.path.join('artifacts' , 'train.csv')
    test_data_path  : str = os.path.join('artifacts' , 'test.csv' )
    raw_data_path   : str = os.path.join('artifacts' , 'raw.csv'  )

class DataIngestion :
    def __init__(self) :
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self) :
        logging.info('Data Ingestion Started')

        try :
            df = pandas.read_csv(os.path.join('notebooks' , 'data' , 'Diamond.csv'))
            logging.info('Dataset readed by Pandas')
            logging.info(f'\n{df.head()}')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path) , exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path , index = False)
            logging.info('Raw data is created')

            train_data , test_data = train_test_split(df , test_size = 0.3 , random_state = 61)
            train_data.to_csv(self.ingestion_config.train_data_path , index = False)
            test_data.to_csv(self.ingestion_config.test_data_path , index = False)

            logging.info('Data Ingestion Finished')

            return(
                self.ingestion_config.train_data_path , 
                self.ingestion_config.test_data_path
            )
        except Exception as e :
            logging.info('Error Occured in reading Dataset as Pandas')
            print(CustomException(e, sys))
