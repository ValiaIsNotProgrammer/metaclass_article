import logging

from logger.base_logger import BaseLoggingMetaclass
# from connection.connection import Connection


class ConnectionLoggingMetaclass(BaseLoggingMetaclass):

    def __new__(cls, name, bases, dct):
        cls.logging_method_endswith = {
            "start_connection": cls._start_connection,
            "handle_connection": cls._handle_connection,
            "message": cls._handle_message,
        }
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _start_connection(method_name, method):
        def wrapper(conn):
            logging.info(f"try connection {method_name} started with {conn.address}")
            result = method(conn)
            if result is not None:
                logging.error(f"error: {result}")
            else:
                logging.info(f"starting connection method {method_name} with {conn.address}")
            return result
        return wrapper


    @staticmethod
    def _handle_connection(method_name, method):
        def wrapper(conn):
            logging.info(f"connection {method_name} recv message from {conn.address}")
            result = method(conn)
            logging.info(f"{method_name} get message from {conn.address}")
            return result
        return wrapper

    @staticmethod
    def _handle_message(method_name, method):
        def wrapper(conn, message: str):
            logging.info(f"method {method_name} start handle message from {conn.address}")
            result = method(conn, message)
            logging.info(f"method {method_name} end handle message {message} from {conn.address}")
            return result
        return wrapper





