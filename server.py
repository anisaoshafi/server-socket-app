import socket
import threading
import time

from BST import BinarySearchTree
from client_handler import ClientThread

t = None
LOCALHOST = socket.gethostname()
PORT = 4000
pre_unique = 0
pre_duplicate = 0
diff_unique = 0
diff_duplicate = 0

bst = BinarySearchTree()


def run_scheduled():
    global t
    check_status()
    t = threading.Timer(10, run_scheduled)
    t.start()


def check_status():
    # this function checks the number of unique, duplicates, total unique numbers received since last run
    global pre_unique, pre_duplicate, diff_unique, diff_duplicate, bst
    diff_unique = bst.size - pre_unique
    diff_duplicate = bst.duplicates - pre_duplicate
    pre_unique = bst.size
    pre_duplicate = bst.duplicates
    print(
        "Received {} unique numbers, {} duplicates. Unique total: {}\n".format(diff_unique, diff_duplicate, pre_unique))


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server started")
    print("Waiting for client request..")
    while True:
        server.listen(5)
        clientsock, clientAddress = server.accept()
        newthread = ClientThread(clientAddress, clientsock, server, bst)
        newthread.start()
    server.close()
    print("Server closed!")


w1 = threading.Thread(target=run_server)
w1.start()
time.sleep(1)
run_scheduled()
w1.join()
t.cancel()
