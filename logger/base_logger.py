import logging
from abc import ABC, abstractmethod


class BaseLoggingMetaclass(type, ABC):

    logging_method_endswith = {}

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
    def _get_log_decorator(cls, method_name):
        #TODO: сделать вложение. Если method_name есть в ключе, то вернуть ключ
        matching_key = cls.__get_key_from_method_name(method_name)
        return cls.logging_method_endswith.get(matching_key, cls.base_logging)

    @classmethod
    def __get_key_from_method_name(cls, method_name):
        for k in cls.logging_method_endswith.keys():
            if k in method_name:
                return k
        return method_name


