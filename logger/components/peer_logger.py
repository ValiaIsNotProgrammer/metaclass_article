import logging

from logger.base_logger import BaseLoggingMetaclass


class PeerLoggingMetaclass(BaseLoggingMetaclass):

    def __new__(cls, name, bases, dct):
        cls.logging_method_endswith = {
            "close": cls._close,
            "accept_connection": cls._start_accept_connection,
            "connect": cls._connect,
        }
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def _connect(method_name, method):
        def wrapper(peer, port):
            print(f"{method_name} connected to server {port}")
            result = method(peer, port)
            if result is not None:
                logging.info(f"{method_name} successfully connected to localhost:{port}")
            else:
                logging.error(f"error: {result}")
            return result
        return wrapper

    @staticmethod
    def _close(method_name, method):
        def wrapper(peer):
            logging.info(f"{method_name} try off peer")
            result = method(peer)
            if result is not None:
                logging.info(f"{method_name} successfully closed peer")
            else:
                logging.error(f"error: {result}")
            return result
        return wrapper

    @staticmethod
    def _start_accept_connection(method_name, method):
        def wrapper(peer):
            logging.info(f"{method_name} waiting for connection")
            result = method(peer)
            #TODO: сделать так, чтобы я имел доступ к порту узла, который подключается
            logging.info(f"{method_name} successfully accepted connection from ")
            return result
        return wrapper


