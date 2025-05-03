# app/model_wrappers/base.py

class BaseModelWrapper:
    """
    Базовый интерфейс для всех моделей: CatBoost, sklearn, нейросети и др.
    """
    def load(self, paths: dict):
        """
        Загрузка модели и её вспомогательных файлов.
        :param paths: словарь путей: model, encoder, feature_order и т.д.
        """
        raise NotImplementedError

    def predict(self, user_input: dict):
        """
        Предсказание по словарю user_input.
        :param user_input: данные от пользователя
        :return: float — оценка шоколадки
        """
        raise NotImplementedError
