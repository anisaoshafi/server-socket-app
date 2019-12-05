import sys
import threading


class ClientThread(threading.Thread):

    def __init__(self, clientAddress, clientsocket, server, bst):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        self.server = server
        self.bst = bst

    def run(self):
        print("Connection from : ", self.clientAddress)

        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()

            if msg == 'terminate':
                try:
                    print("Server socket communication needs closing")
                    self.csocket.close()
                    sys.exit()
                    break
                except OSError:
                    print("OS error thrown")

            if len(msg) == 9:
                try:
                    num = int(msg)
                    print("The 9-digit number {} was sent".format(num))
                    self.bst.insert(num)
                except:
                    break
            else:
                print("Invalid input")
                self.csocket.close()
                break

            self.csocket.send(bytes(msg, 'UTF-8'))

        print("Client at ", self.clientAddress, " disconnected...")
