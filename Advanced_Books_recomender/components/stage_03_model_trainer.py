import os
import sys
import pickle
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from Advanced_Books_recomender.logger.log import logging
from Advanced_Books_recomender.config.configuration import AppConfiguration
from Advanced_Books_recomender.exception.exception_handler import AppException


class ModelTrainer:
    def __init__(self, app_config = AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e, sys) from e # type: ignore

    
    def train(self):
        try:
            #loading pivot data
            book_pivot = pickle.load(open(self.model_trainer_config.transformed_data_file_dir,'rb'))
            book_sparse = csr_matrix(book_pivot)
            #Training model
            model = NearestNeighbors(algorithm= 'brute')
            model.fit(book_sparse)

            #Saving model object for recommendations
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
            file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(model,open(file_name,'wb'))
            logging.info(f"Saving final model to {file_name}")

        except Exception as e:
            raise AppException(e, sys) from e # type: ignore

    

    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.train()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e # type: ignore