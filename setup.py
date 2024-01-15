import argparse

from logger.components.setup_logger import SetupLoggingMetaclass
from peer.peer import Peer
from session.session import Session

import logging
import sys

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)


class CMDLine(metaclass=SetupLoggingMetaclass):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="P2P Network Command Line Interface")
        self.__add_arguments()

    def setup(self):
        commands = self.__parse_command()
        peer = Peer("localhost", commands["port"])
        session = Session(peer)
        session.setup()
        peer.setup()

    def __add_arguments(self):
        self.parser.add_argument("-p", "--port", type=int, help="Set port for your peer")

    def __parse_command(self):
        args = self.parser.parse_args()
        return args.__dict__


if __name__ == "__main__":
    cmdline = CMDLine()
    cmdline.setup()