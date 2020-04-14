#Source code from: https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
#!/usr/bin/env python3

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import signal, sys

clients = {}
addresses = {}

BUFSIZ = 1024
serverAddress = ('localhost', 9999)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(serverAddress)

def signal_handler(sig, frame):
    SERVER.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#indefinite loop waiting for incoming connections
def accept_incoming_connections():
    #handles incoming connection
    while True:
        client, client_address = SERVER.accept()
        #server log for who connected
        print("%s:%s has connected." % client_address)
        client.send(bytes("Welcome to Clean Messenger, please enter your name to proceed!", "utf8"))
        #stores client address
        addresses[client] = client_address
        #start handling thread
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    # handle connection with client (thread is allocated for each)

    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(msg)
    clients[client] = name

    while True:
        #store new client name
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            msg = msg.decode("utf8")
            broadcast(msg, name+": ")
        #else remove client from client list
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast("%s has left the chat." % name)
            break

#function to broadcast message to all connected clients
def broadcast(msg, prefix=""): 
    # sends message to all connected clients
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+bytes(msg, "utf8"))

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for client to join")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
