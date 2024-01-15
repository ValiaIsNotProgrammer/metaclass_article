import logging

from logger.base_logger import BaseLoggingMetaclass


class SetupLoggingMetaclass(BaseLoggingMetaclass):

    def __new__(cls, name, bases, dct):
        cls.logging_method_endswith = {
            "setup": cls._setup,
        }
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _setup(method_name, method):
        def wrapper(*args, **kwargs):
            logging.info(f"{method_name} setup app")
            result = method(*args, **kwargs)
            if result is not None:
                logging.info(f"{method_name} successfully setup")
            else:
                logging.error(f"{method_name} get error: {result}")
            return result
        return wrapper

