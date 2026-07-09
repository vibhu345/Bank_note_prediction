import sys
from src.logger import logging
def get_detailed_error(error_message,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_messag="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error_message))
    return error_messag
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_details=get_detailed_error(error_message,error_detail)
    def __str__(self):
        return self.error_details
if __name__=="__main__()":
    logging.info("logging main maza aaya exception mein")




