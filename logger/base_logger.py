import logging
from abc import abstractmethod


class BaseLoggingMetaclass(type):

    def __new__(cls, name, bases, dct):
        for method_name, method in dct.items():
            if callable(method):
                log_decorator = cls._get_log_decorator(method_name)
                dct[method_name] = log_decorator(method_name, method)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def base_logging(method_name, method):
        def wrapper(*args, **kwargs):
            logging.info(f"Вызов метода: {method_name}")
            result = method(*args, **kwargs)
            logging.info(f"Метод {method_name} завершился с результатом: {result}")
            return result
        return wrapper

    @classmethod
    @abstractmethod
    def _get_log_decorator(cls, method_name):
        return cls.base_logging


class BaseLoggingMethodMixin:
    def __init__(self):
        pass


