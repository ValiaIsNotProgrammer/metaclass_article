import threading

from logger.components.session_logger import SessionLoggingMetaclass
from peer.peer import Peer


class Session(metaclass=SessionLoggingMetaclass):

    def __init__(self, peer: Peer):
        self.peer: Peer = peer
        self.commands = {
                        "send": self.send_peer,
                        "sendall": self.send_all,
                        "connect": self.connect,
                        "address": self.address,
                        # "disconnect",
                        "close": self.close,
                        "show": self.show,
                    }

    def setup(self):
        thread = threading.Thread(target=self.run)
        thread.start()

    def login(self, username, password):
        pass

    def run(self):
        while True:
            input_ = input("Enter command: ")
            self.to_command(input_)

    def to_command(self, input_) -> None:
        if self.is_command(input_):
            return self.__parse_command(input_)

    def is_command(self, command):
        return command.split()[0] in self.commands

    def __parse_command(self, input_):
        split_input = input_.split()
        command = split_input[0]
        if len(split_input) > 1:
            args = input_.split()[1:]
            return self.commands[command](args)
        return self.commands[command]()

    def send_peer(self, args) -> None:
        port = args[-1]
        message = " ".join(args[:-1])
        self.peer.send_peer(message, port)

    def send_all(self, args) -> None:
        message = " ".join(args)
        self.peer.send_all(message)

    def connect(self, args):
        port = args[0]
        print(f"try to connect to {port}")
        self.peer.connect(int(port))

    def close(self):
        self.peer.close()

    def show(self):
        for connection in self.peer.connections:
            print(f"Your connection: {connection.address}")

    def address(self):
        print(f"Your address: {self.peer.host}:{self.peer.port}")

