import tensorflow  
from src.exception import CustomException
import sys,os
from sklearn.metrics import accuracy_score
from src.logger import logging
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout,Dense
from tensorflow.keras.callbacks import EarlyStopping
import pickle
from sklearn.model_selection import train_test_split
class DataModeling():
    trainined_model_path=os.path.join("artifacts","trained_model.pkl")
class Model_training:
    logging.info("we have entered into model_training file and model trainer class")

    
    def initiate_model_training(self,x_train,x_test,y_train,y_test):
        try:
            model_training_config=DataModeling()
            model=Sequential([
                Dense(units=256,input_shape=(x_train.shape[1],)),
                Dropout(0.3),
                Dense(units=128,activation="relu"),
                Dropout(0.3),
                Dense(units=64,activation="relu"),
                Dropout(0.3),
                Dense(1,activation="sigmoid")
                

            ])
            logging.info("we are now compiling the model")
            model.compile(loss="binary_crossentropy",optimizer="Adam",metrics=["accuracy"])
            model.summary()
            earlystoppng=EarlyStopping(restore_best_weights=True,patience=10,monitor="val_loss",verbose=1)
            logging.info("we are now fitting the model with 30 epochs")
            hsitory=model.fit(x_train,y_train,epochs=10,batch_size=32,validation_data=(x_test,y_test),callbacks=[earlystoppng])
            y_predict=(model.predict(x_test)>0.5).astype(int)
            accuracy=accuracy_score(y_test,y_predict)
            print(accuracy)
            logging.info("saving the model")
            os.makedirs(os.path.dirname(model_training_config.trainined_model_path),exist_ok=True)
            with open(model_training_config.trainined_model_path,"wb") as file_obj:
                pickle.dump(model,file_obj)
            logging.info("exitting the model trainer class")
            
            # test_loss,test_accuracy=model.evaluate(x_test,y_test)

        except Exception as e:
            raise CustomException(e,sys)