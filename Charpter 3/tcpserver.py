import socket

ip_port = ('127.0.0.1', 1080)

sk = socket.socket()            # 创建套接字
sk.bind(ip_port)                # 绑定服务地址
sk.listen(5)                    # 监听连接请求

print('Start socket service，wait for client to connect...')

conn, address = sk.accept()     # 等待连接，此处自动阻塞

while True:     # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接
    client_data = conn.recv(1024).decode()      # 接收信息
    if client_data == "exit":       # 判断是否退出连接
        exit("Communication over.")
    print("Client from %s sends u a message:%s" % (address, client_data))
    conn.sendall('Server has received your message:'.encode())    # 回馈信息给客户端

conn.close()    # 关闭连接