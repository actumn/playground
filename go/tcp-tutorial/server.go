/*
    source code from:
    https://blog.kesuskim.com/2018/08/go-tcp-implementation/
*/

package main

import (
    "io"
    "log"
    "net"
)

func main() {
    l, err := net.Listen("tcp", ":5032")
    if nil != err {
        log.Fatalf("fail to bind address to 5032; err: %v", err)
    }
    defer l.Close()

    for {
        conn, err = l.Accept()
        if nil != err {
            log.Printf("fail to accept; err: %v", err)
            continue
        }
        go ConnHandler(conn)
    }
}

func ConnHandler(conn net.Conn) {
    recvBuf := make([]byte, 4096)
    for {
        n, err := conn.Read(recvBuf)
        if nil != err {
            if io.EOF == err {
                log.Printf("connection is closed from client; %v", conn.RemoteAddr().String())
                return
            }
            log.Printf("fail to receive data; err: %v", err)
            return
        }
        if 0 < n {
            data := recvBuf[:n]
            log.Println(string(data))
        }
    }
}
