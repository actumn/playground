/*
    source code from:
    https://blog.kesuskim.com/2018/08/go-tcp-implementation/
*/
package main

import (
    "log"
    "net"
    "time"
)

func main() {
    conn, err := net.Dial("tcp", "server0:5032")
    if nil != err {
        log.Fatalf("failed to connect to server")
    }

    // some event happens

    for {
        // heartbeat
        conn.Write([]byte("ping"))
        time.Sleep(time.Duration(3) * time.Second)
    }
}
