#include<bits/stdc++.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<unistd.h>

using namespace std;

int main(){
    sockaddr_in server_address, client_address;
    int server_socket, accept_socket;

    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    server_address.sin_family = AF_INET;
    server_address.sin_port = htons(5050);
    server_address.sin_addr.s_addr = INADDR_ANY;

    bind(server_socket, (struct sockaddr*)&server_address, sizeof(server_address));

    listen(server_socket, 5);
    cout << "[LISTENING] Server Listening on port " << server_address.sin_port << "\n";


    socklen_t client_size = sizeof(client_address);
    accept_socket = accept(server_socket, (struct sockaddr*)&client_address, &client_size);

    char buffer[1024] = {0};
    read()
    read(accept_socket, buffer, sizeof(buffer));
    cout << "[RECIEVED] Server Recieved: " << buffer << "\n";


    send(accept_socket, buffer, strlen(buffer), 0);

    close(accept_socket);
    close(server_socket);
    
    return 0;
}