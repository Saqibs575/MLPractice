from datetime import datetime
import logging
import os

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_file_directory = os.path.join(os.getcwd() , 'logs')
os.makedirs(logs_file_directory , exist_ok = True)
log_file_path = os.path.join(logs_file_directory , LOG_FILE_NAME)

logging.basicConfig(
    filename = log_file_path,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

