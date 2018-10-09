#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/stat.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define MAXLINE 1024


int main(int argc, char **argv)
{
    if (argc < 2)
    {
        fprintf(stderr, "Usage : %s <port>", argv[0]));
        return 1;
    }

    struct sockaddr_in serveraddr;
    int client_sockfd;
    int client_len;
    char buf[MAXLINE];

    if ((client_sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
    {
        perror("error : ");
        return 1;
    }

    // 연결 요청할 서버의 주소와 포트번호 프로토콜
    serveraddr.sin_family = AF_INET;
    serveraddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    serveraddr.sin_port = htons(atoi(argv[1]));

    client_len = sizeof(serveraddr);

    // 서버에 연결 시도
    if (connect(client_sockfd, (struct sockaddr *)&serveraddr, client_len) == -1)
    {
        perror("connect error :");
        return 1;
    }
    printf("client_sockfd: %d\n", client_sockfd);

    // fd가 0이면 stdin.
    // stdin 입력데이터를 서버로 전송
    memset(buf, 0x00, MAXLINE);
    read(0, buf, MAXLINE);
    if (write(client_sockfd, buf, MAXLINE) <= 0)
    {
        perror("write error : ");
        return 1;
    }

    memset(buf, 0x00, MAXLINE);
    if (read(client_sockfd, buf, MAXLINE) <= 0)
    {
        perror("read error : ");
        return 1;
    }
    close(client_sockfd);
    printf("read : %s", buf);
    return 0;
}
