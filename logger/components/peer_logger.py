import logging

from logger.base_logger import BaseLoggingMetaclass


class PeerLoggingMetaclass(BaseLoggingMetaclass):

    def __new__(cls, name, bases, dct):
        cls.logging_method_endswith = {
            "connection": cls._listen_to_connection,
        }
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _listen_to_connection(method_name, method):
        def wrapper(*args, **kwargs):
            logging.info(f"fuck you")
            result = method(*args, **kwargs)
            logging.info(f"no, fuck you: {result}")
            return result
        return wrapper


