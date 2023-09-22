import sys
from src.AIProject.logger import logging
from src.AIProject.exception   import CustomException

if __name__ == '__main__':
    logging.info("The execution has started")

    try:
        #data_ingestion=data_Ingestion.
        a=10

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)

from src.AIProject import utils
df=utils.read_sql_data()
print(df)