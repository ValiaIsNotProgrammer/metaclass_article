import argparse

from peer import Peer
from session import Session


class CMDLine:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="P2P Network Command Line Interface")
        self.__add_arguments()

    def setup(self):
        commands = self.__extract_command()
        peer = Peer("localhost", commands["port"])
        session = Session(peer)
        session.setup()
        peer.setup()

    def __add_arguments(self):
        self.parser.add_argument("-p", "--port", type=int, help="Set port for your peer")

    def __extract_command(self):
        args = self.parser.parse_args()
        return args.__dict__




if __name__ == "__main__":
    cmdline = CMDLine()
    cmdline.setup()