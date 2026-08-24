import os
import sys
import pickle
import pandas as pd
from src.exception import CustomException

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, feature1: float, feature2: float):
        self.feature1 = feature1
        self.feature2 = feature2

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "feature1": [self.feature1],
                "feature2": [self.feature2],
            }
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)