#TCP_server.py
#１导入socket模块
from socket import *
#创建套接字
# sockfd = socket(AF_INET, SOCK_STREAM)


sockfd = socket(AF_INET, SOCK_STREAM)

#２绑定服务端地址
sockfd.bind(("0.0.0.0", 8889))

#３设置监听
sockfd.listen(5)


#4. 等待处理客户端连接请求
while True:
    print("waiting for connect...")
    confd, addr = sockfd.accept()


    print("Connect from", addr)



    while True:
    #收消息
        data = confd.recv(5)
        if not data:
            break
        print(data.decode())

        #发消息
        n = confd.send(b'recieve your message')
        print("发送了%d字节"%n)

    confd.close()
sockfd.close()












