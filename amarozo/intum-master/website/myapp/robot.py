import socket

class Robot:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        try:
            self.sock.connect((self.ip_address, self.port))
            self.connected = True
            data = self.sock.recv(100)
            print('received "%s"' % data)

        except:
            pass

    def send_command(self, command):
        try:
            message = command + '\n'
            print('sending "%s"' % message)
            self.sock.sendto(message.encode(), (self.ip_address, self.port))
            data = self.sock.recv(100)
            print('received "%s"' % data)

        except:
            pass

    def disconnect(self):
        self.sock.close()
        self.connected = False
