package main

import (
	"log"
	"net"
)

func main() {
	addr, err := net.ResolveTCPAddr("tcp4", "0.0.0.0:9990")
	if err != nil {
		log.Panicln(err)
	}

	server, err := net.ListenTCP("tcp4", addr)
	if err != nil {
		log.Panicln(err)
	}
	defer server.Close()

	conn, err := server.Accept()
	if err != nil {
		log.Panicln(err)
	}
	defer conn.Close()

	buffer := make([]byte, 4096)
	n, err := conn.Read(buffer)
	if err != nil {
		log.Panicln(err)
	}
	data := buffer[:n]
	conn.Write(data)
}
