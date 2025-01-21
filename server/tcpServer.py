import socket

server = socket.socket()
print(type(server), server)
laddr = ('127.0.0.1', 9999)
server.bind(laddr)
server.listen(1024) # backlog默认为5，未完成连接和完成连接

print('1' * 30)

while True:
    # netsock是负责和客户端进程通信的座子（服务员），服务员是server端的
    netsock, raddr = server.accept()
    print(netsock, type(netsock))
    print(raddr, netsock.getpeername()) # 拿对端
    print(netsock.getsockname()) # 拿laddr
    print('2' * 30)
    data = netsock.recv(1024) # 1024的倍数，读取缓冲区没有数据呢？
    print(type(data), data)
    print('3' * 30)
    netsock.send(b"www.magedu.com") # bytes

    netsock.close()
server.close()

