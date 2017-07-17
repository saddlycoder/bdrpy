import vk_api, os, time, datetime
from socket import *

from urllib2 import urlopen
ip = urlopen('http://ip.42.pl/raw').read()

print ip

host = '127.0.0.1'
port = 25565
addr = (host,port)


tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(addr)

tcp_socket.listen(5)
# loop
while True:
    print('wait connection..')

    conn, addr = tcp_socket.accept()
    #print('client addr: ', addr)

    # reciving answer
    data = conn.recv(2048)

    if not data:
        conn.close()
        break
    else:
        if '#exec' in data:
            data = data.replace('#exec', '') # clear key
            print('[GET_EVAL] '+ data)
            exec(data)
        elif '#os' in data:
            data = data.replace('#os', '') # clear key
            print('[GET_OS] ' + data)
            os.system(data)
        # send TCP msg
        conn.send(b'return 1')
        # socket closing
        conn.close()

tcp_socket.close()
