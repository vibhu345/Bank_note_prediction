import logging
from datetime import datetime
import os
log_file_path= f"{datetime.now().strftime("_%d_%Y_%H_%M")}.log"
# defining the directry
log_dir=os.path.join(os.getcwd(),"MereLogs")
os.makedirs(log_dir,exist_ok=True)
log_file=os.path.join(log_dir,log_file_path)


logging.basicConfig(
level=logging.INFO,
format=" [ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s - %(message)s",
filename=log_file
)
# logging.info("logging started")
# if __name__ =="__main__()":
#     pass
