#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Compile for windows
#define PLATFORM_WIN

#ifdef PLATFORM_WIN

#include<winsock2.h>
#pragma comment(lib,"ws2_32.lib")

#endif

#ifdef PLATFORM_LINUX

#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#endif




int main(int argc, char *argv[])
{

    #ifdef PLATFORM_WIN
      WSADATA wsa;
      WSAStartup(MAKEWORD(2,2),&wsa);
      SOCKET sockethandle;
    #endif

    #ifdef PLATFORM_LINUX
      int sockethandle = 0;
    #endif

    char recvBuff[1024];
    struct sockaddr_in serv_addr;

    memset(recvBuff, '0',sizeof(recvBuff));
    sockethandle = socket(AF_INET, SOCK_STREAM, 0);
    memset(&serv_addr, '0', sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(80);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

    connect(sockethandle, (struct sockaddr *)&serv_addr, sizeof(serv_addr))

    #ifdef PLATFORM_WIN
      n = read(sockethandle, recvBuff, sizeof(recvBuff)-1);
    #endif

    #ifdef PLATFORM_WIN
      n = recv(sockethandle , recvBuff , 2000 ,  sizeof(recvBuff)-1);
    #endif

    return 0;
}
