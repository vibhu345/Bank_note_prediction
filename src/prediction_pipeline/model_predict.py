import pickle,os,sys
import dill
from src.exception import CustomException
from src.logger import logging

class ModelPredict:
    def __init__(self):
        pass
    logging.info("we have entered into model predict class")
    def model_prediction(self,data_frame):
        try:
            model_path=os.path.join("artifacts","trained_model.pkl")
            scaler_path=os.path.join("artifacts","proprocessor_saved.pkl")
            logging.info("we have path to model to model_path and scaler_path")
            with open(model_path,"rb") as model_obj:
                model= dill.load(model_obj)
            with open (scaler_path,"rb") as scaler_obj:
                scaler= dill.load(scaler_obj)
            logging.info("we have imported the model and scaler")
            scaled_features=scaler.transform(data_frame)
            result= model.predict(scaled_features)
            predicted_classes = (result>0.5).astype(int)

            logging.info("we have done with prediction")
            return predicted_classes
        except Exception as e:
            raise CustomException(e,sys)
    