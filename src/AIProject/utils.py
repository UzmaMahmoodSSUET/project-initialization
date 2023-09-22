import pymysql
import os
import sys
from src.AIProject.exception import CustomException
from src.AIProject.logger import logging 


import pickle
import numpy as np
import pandas as pd

# host="local host",
# user="root"
# password="peloris_100"
# db="mydb_uzma"


def read_sql_data():
    logging.info('Reading SQl database is started')

    try:
        mydb=pymysql.connect(
            host="localhost",
            user="root",
            password="peloris_100",
            db="mydb_uzma"
                        )
        logging.info("Connection Established", mydb)
        df=pd.read_sql_query('SELECT * FROM data', mydb)
       
        return df
    
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
