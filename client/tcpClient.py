import socket

tcp_client_socket = socket.socket()

tcp_client_socket.connect(("127.0.0.1", 9999))
send_data = input(str("请输入数据："))

tcp_client_socket.send(send_data.encode("utf-8"))

msg = tcp_client_socket.recv(1024)
print(msg.decode())

tcp_client_socket.close()