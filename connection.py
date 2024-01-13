import threading


class Connection:
    def __init__(self, socket):
        self.socket = socket
        self.address = socket.getpeername()
        self.thread = threading.Thread(target=self.listen_to_connection)
        self.thread.start()

    def listen_to_connection(self):
        while True:
            try:
                message = self.socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Message from {self.address}: {message}")
                    pass
            except Exception as e:
                print(e)
                print(f"Connection with {self.address} lost")
                self.socket.close()
                break

    def send_message(self, message):
        # message = Message(self.socket, message)
        self.socket.send(message.encode('utf-8'))
