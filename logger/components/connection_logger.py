import logging

from logger.base_logger import BaseLoggingMetaclass


class ConnectionLoggingMetaclass(BaseLoggingMetaclass):
    @staticmethod
    def _listen_to_connection(method_name, method):
        print(method_name)
        def wrapper(*args, **kwargs):
            logging.info(f"fuck you")
            result = method(*args, **kwargs)
            logging.info(f"no, fuck you: {result}")
            return result
        return wrapper

    @classmethod
    def _get_log_decorator(cls, method_name):
        print("adsf")
        if method_name.endswith("connection"):
            return cls._listen_to_connection
        return cls.base_logging

