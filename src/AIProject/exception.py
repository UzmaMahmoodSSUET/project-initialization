import sys
from src.AIProject.logger import logging 

# from logger import logging 

def error_message_detail(error, error_details:sys):
    _,_, exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in Python Script name [{0}] Line No. [{1}] Error Message [{2}]".format(file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):

    # Constructor or Initializer
    def __init__(self, error_message, error_details:sys):
        super().__init__(self, error_message)
        self.error_message = error_message_detail(error_message, error_details)
    
    # __str__ is to print() the value
    def __str__(self):
        return self.error_message