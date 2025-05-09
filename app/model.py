# библиотека model.py, на основе лабораторной 4. Модель линейной регрессии
import pandas as pd
from catboost import CatBoostRegressor
import pickle

# === Загружаем обученную модель и вспомогательные данные ===
catboost_model = CatBoostRegressor()
catboost_model.load_model("Модель2.0/catboost_model2.0.cbm")

with open("Модель2.0/encoder2.0.pkl", "rb") as f:
    encoder = pickle.load(f)

with open("Модель2.0/feature_order2.0.pkl", "rb") as f:
    feature_order = pickle.load(f)

# === Предсказание ===
def predict_chocolate_rating(user_input_dict):
    input_df = pd.DataFrame(user_input_dict)
    input_df['Cocoa Percent'] = input_df['Cocoa Percent'].astype(float)
    input_df_encoded = encoder.transform(input_df)
    input_df_encoded = input_df_encoded[feature_order]
    prediction = catboost_model.predict(input_df_encoded)[0]
    return prediction
