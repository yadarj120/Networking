#include<bits/stdc++.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<unistd.h>

using namespace std;

int main(){
    int client_socket = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in server_address;
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(5050);
    server_address.sin_addr.s_addr = INADDR_ANY;

    connect(client_socket, (struct sockaddr*)&server_address, sizeof(server_address));

    char msg[1024] = "Hello Server!";
    send(client_socket, msg, strlen(msg), 0);

    char buffer[1024] = {0};
    read(client_socket, buffer, sizeof(buffer));
    cout << "[CLIENT] Server Replied: " << buffer << "\n";

    close(client_socket);
    return 0;
}