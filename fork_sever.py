from socket import *
import os,sys
import signal

#客户端处理函数
def client_handler(c):
    print('处理子进程的请求:',c.getpeername())
    try:
        while True:
            data = c.recv(1024)
            if not data:
                break
            print(data)
            c.send('收到客户端请求'.encode())
    except (KeyboardInterrupt,SystemError):
        sys.exit('客户端退出')
    except Exception as e:
        print(e)
    c.close()
    sys.exit()

#创建套接子
HOST =''
PORT = 8888
ADDR = (HOST,PORT)

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(ADDR)
s.listen(5)

print('进程%d等待客户连接'%os.getpid())
#在父进程忽视字进程状态，子进程状态发生改变，子进程退出自动由系统处理

while True:
    try:
        c,addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print("Error:",e)
        continue
    #为客户端创建新的进程来处理请求
    pid = os.fork()
    #子进程处理具体请求
    if pid == 0:
        s.close()
        client_handler(c)

    #父进程或者创建失败都继续等待下一个客户端的连接
    else:
        c.close()
        continue

if __name__ == '__main__':
    main()