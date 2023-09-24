import socket
import threading

PORT = 7070
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
server_addr = "172.19.14.170"

ADDR = (server_addr, PORT)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
server_sock.bind(ADDR);

def handle_client(client_sock, client_addr):
    print(f'[Connection]: connection established with {client_addr}')
    connected = True
    while connected:
        enc_msg_length = client_sock.recv(HEADER).decode(FORMAT)
        if enc_msg_length:
            enc_msg_length = int(enc_msg_length)
            msg = client_sock.recv(enc_msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{client_addr}] {msg}")
    
    client_sock.close()


def start():
    server_sock.listen()
    while True:
        client_sock, client_addr = server_sock.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
        client_thread.start();
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")

print("[STARTING] server is starting ...")  
start()




