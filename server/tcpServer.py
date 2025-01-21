import socket

server = socket.socket()
print(type(server), server)
laddr = ('127.0.0.1', 9888) # laddr为您的TCP Server的IP地址和监听端口 
server.bind(laddr)
server.listen(1024) # backlog默认为5

while True:
    # netsock是负责和客户端进程通信的socket
    netsock, raddr = server.accept()
    print(netsock, type(netsock))
    print(raddr, netsock.getpeername())
    print(netsock.getsockname())
    data = netsock.recv(1024) # 1024的倍数
    print(type(data), data)
    netsock.send(b"Hello Tcp Server") # bytes

    netsock.close()
server.close()

