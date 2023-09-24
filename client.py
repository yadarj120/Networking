import socket
import threading

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'

ADDR = ("172.19.14.105", PORT)

c = socket.socket();
c.connect(ADDR)

msg = "Hello, I am Arjun"
enc_msg_length = len(msg).encode(FORMAT)
enc_msg_lengthkalength = len(enc_msg_length)
c.send(b' ' * (HEADER - enc_msg_lengthkalength) + enc_msg_length)