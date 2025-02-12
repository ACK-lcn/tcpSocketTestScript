import socket

tcp_client_socket = socket.socket()

# 将tcp_client_socket.connect设置为您要连接TCP Server的IP地址和Port端口
tcp_client_socket.connect(("127.0.0.1", 9888))
send_data = input(str("请输入数据："))

tcp_client_socket.send(send_data.encode("utf-8"))

msg = tcp_client_socket.recv(1024)
print(msg.decode())

tcp_client_socket.close()
