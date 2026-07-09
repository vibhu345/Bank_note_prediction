# the aim of this file is to provide the path to train data ,test data and raw data
import os
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
import sys
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import Model_training
from sklearn.utils import resample
class DataIngestionConfig:
    train_data_path=os.path.join("artifacts","train_data_path")
    test_data_path=os.path.join("artifacts","test_data_path")
    raw_data_path=os.path.join("artifacts","raw_data_path")



class DataIngestion:
    def initiate_data_ingestion(self):
        try:
            data_ingestion_config=DataIngestionConfig()
            logging.info("starting with DataIngestion class and obtaining the raw data from data folder")
            df=pd.read_csv("data/train.csv")
            os.makedirs(os.path.dirname(data_ingestion_config.raw_data_path),exist_ok=True)
            logging.info("saved the raw data into the artifacts folder")
            df=df.drop_duplicates()
            # resampling the dataset
            # print(df.Class.value_counts())
            logging.info("resampling the data")
            df_minority=df[df["Class"]==1]
            df_majority=df[df["Class"]==0]
            df_minority_upsampled=resample(df_minority,n_samples=len(df_majority),replace=True,random_state=1)
            df=pd.concat([df_majority,df_minority_upsampled])
            df=pd.DataFrame(df)
            df.to_csv(data_ingestion_config.raw_data_path,index=False,header=True)
            train_data,test_data=train_test_split(df,test_size=0.2,random_state=1)
            train_data.to_csv(data_ingestion_config.train_data_path,index=False,header=True)
            test_data.to_csv(data_ingestion_config.test_data_path,index=False,header=True)
            logging.info("Done with saving the train data and test data in the form of data frame and now exiting from DataIngestion class")
            return (data_ingestion_config.train_data_path,data_ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException (e,sys)
if __name__=="__main__":
    try:
        obj=DataIngestion()
        train_data_path,test_data_path=obj.initiate_data_ingestion()
        obj1=DataTransformation()
        x_train_dataframe,x_test_dataframe,y_train_dataframe,y_test_dataframe,preprocessor_obj=obj1.initiate_data_transformation(train_data_path,test_data_path)
        obj2=Model_training()
        obj2.initiate_model_training(x_train_dataframe,x_test_dataframe,y_train_dataframe,y_test_dataframe)
    except Exception as e :
        raise CustomException(e,sys)



    



