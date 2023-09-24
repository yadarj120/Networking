import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
PORT = 7070
SERVER_IP = "172.19.14.170"
ADDR = (SERVER_IP, PORT)

def send(msg):
    message = msg.encode(FORMAT)
    len_msg = str(len(message))
    len_msg_enc = len_msg.encode(FORMAT)
    len_msg_enc += b' ' * (HEADER - len(len_msg_enc))
    c.send(len_msg_enc)
    c.send(message)

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(ADDR)
send("Hello server")

send(DISCONNECT_MESSAGE)