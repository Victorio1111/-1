# model.py
from app.model_loader import load_model_by_id

# Здесь можно выбрать модель по умолчанию:
DEFAULT_MODEL_ID = "model_catboost_v1"

model = load_model_by_id(DEFAULT_MODEL_ID)

def predict_chocolate_rating(user_input_dict):
    return model.predict(user_input_dict)
