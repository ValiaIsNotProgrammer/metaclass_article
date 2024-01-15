import logging

from logger.base_logger import BaseLoggingMetaclass


class SessionLoggingMetaclass(BaseLoggingMetaclass):

    def __new__(cls, name, bases, dct):
        cls.logging_method_endswith = {
            "run": cls._run,
            "to_command": cls._to_command,
        }
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _run(method_name, method):
        def wrapper(*args, **kwargs):
            logging.info(f"{method_name} running session")
            result = method(*args, **kwargs)
            logging.info(f"{method_name} session end: {result}")
            return result
        return wrapper

    @staticmethod
    def _to_command(method_name, method):
        def wrapper(session, command):
            logging.info(f"{method_name} getting command {command}")
            result = method(session, command)
            if result:
                logging.info(f"{method_name} get correct command {command}")
            else:
                logging.warning(f"{method_name} get wrong command {command}")
            return result
        return wrapper

