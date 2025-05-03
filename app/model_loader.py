# app/model_loader.py

import json
import importlib

def load_class_from_path(class_path):
    """
    Динамический импорт класса по строке.
    """
    module_name, class_name = class_path.rsplit(".", 1)
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def load_model_by_id(model_id):
    """
    Загрузка модели по ID из реестра
    """
    with open("models_registry.json", encoding="utf-8") as f:
        registry = json.load(f)

    model_info = registry[model_id]

    class_path = model_info["class_path"]
    model_class = load_class_from_path(class_path)

    paths = {
        "model": model_info["path"],
        "encoder": model_info.get("encoder"),
        "feature_order": model_info.get("feature_order")
    }

    model = model_class()
    model.load(paths)
    return model
