import pandas as pd
from catboost import CatBoostRegressor
import pickle

# === Загружаем обученную модель ===
catboost_model = CatBoostRegressor()
catboost_model.load_model("catboost_model.cbm")

# === Загружаем сохранённый encoder ===
with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# === Загружаем порядок признаков ===
with open("feature_order.pkl", "rb") as f:
    feature_order = pickle.load(f)

# === Предсказание по пользовательскому вводу ===
def predict_chocolate_rating(model, encoder, feature_order, user_input_dict):
    input_df = pd.DataFrame(user_input_dict)
    input_df['Cocoa Percent'] = input_df['Cocoa Percent'].astype(float)
    input_df_encoded = encoder.transform(input_df)
    input_df_encoded = input_df_encoded[feature_order]
    return model.predict(input_df_encoded)[0]

# === Ввод пользователя ===
user_input = {
    'Cocoa Percent': [70],
    'Company\xa0 (Maker-if known)': ['A. Morin'],
    'Specific Bean Origin or Bar Name': ['Sur del Lago'],
    'Company Location': ['France'],
    'Bean Type': ['Criollo'],
    'Broad Bean Origin': ['Venezuela']
}

# === Предсказание ===
predicted_rating = predict_chocolate_rating(catboost_model, encoder, feature_order, user_input)
print(f"Предсказанный рейтинг шоколада: {predicted_rating:.2f}")
