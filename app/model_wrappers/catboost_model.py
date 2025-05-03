# app/model_wrappers/catboost_model.py

import pandas as pd
from catboost import CatBoostRegressor
import pickle
from app.model_wrappers.base import BaseModelWrapper

class CatBoostModelWrapper(BaseModelWrapper):
    def __init__(self):
        self.model = None
        self.encoder = None
        self.feature_order = None

    def load(self, paths: dict):
        """
        Загрузка модели, энкодера и порядка признаков
        """
        self.model = CatBoostRegressor()
        self.model.load_model(paths["model"])
        
        with open(paths["encoder"], "rb") as f:
            self.encoder = pickle.load(f)
        
        with open(paths["feature_order"], "rb") as f:
            self.feature_order = pickle.load(f)

    def predict(self, user_input: dict):
        """
        Обработка и предсказание
        """
        input_df = pd.DataFrame(user_input)
        input_df['Cocoa Percent'] = input_df['Cocoa Percent'].astype(float)

        encoded = self.encoder.transform(input_df)
        ordered = encoded[self.feature_order]

        return self.model.predict(ordered)[0]
