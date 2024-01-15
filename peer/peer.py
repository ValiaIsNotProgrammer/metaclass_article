import socket
import threading
from time import sleep

from connection.connection import Connection
from logger.components.peer_logger import PeerLoggingMetaclass



class Peer(metaclass=PeerLoggingMetaclass):
    def __init__(self, host, port):
        self.connections = []
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def setup(self):
        thread_1 = threading.Thread(target=self.__start_server)
        thread_2 = threading.Thread(target=self.__start_accept_connections)
        thread_1.start()
        sleep(1)
        thread_2.start()

    def connect(self, port):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.host, port))
            self.__start_connection(client_socket)
        except Exception as e:
            return e

    def send_peer(self, message, port):
        connection = self.__get_connection_from_port(int(port))
        if connection:
            return connection.send_message(message)
        print("Нет такого соединения")

    def send_all(self, message):
        for connection in self.connections:
            connection.send_message(message)

    def __start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

    def __start_connection(self, client_socket):
        connection = Connection(client_socket)
        self.connections.append(connection)

    def __start_accept_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            connection = Connection(client_socket)
            self.connections.append(connection)

    def __get_connection_from_port(self, port: int):
        for conn in self.connections:
            #TODO: сделать так, чтобы принимающий подключение сокет знал реальный порт другого узла
            if port in conn.address:
                return conn

    def close(self):
        try:
            self.server_socket.close()
        except Exception as e:
            return e


