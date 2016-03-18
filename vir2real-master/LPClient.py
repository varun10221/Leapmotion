import socket   
import sys
import json
import tornado.websocket
from tornado import gen 

class LeapMotionClient(object):
    def __init__(self, host, port):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Failed to create socket')
            sys.exit()
        print('Socket Created')
        #To allow you to immediately reuse the same port after 
        #killing your server:
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #host = 'localhost';
        #port = 8124;
        self.sock.connect((host , port))
        print('Socket Connected to ' + host + ' on port ', port)

    def send(self, data):
        #Send some data to server
        #message = "GET / HTTP/1.1\r\n\r\n"
        try :
            #Send the whole string(sendall() handles the looping for you)
            self.sock.sendall(data.encode('utf8') )
        except socket.error:
            print('Send failed')
            sys.exit()
        print('Message sent successfully')

class LeapMotionWSClient(object):
    def __init__(self, host, port):
        try:
            tornado.ioloop.IOLoop.instance().run_sync(lambda: self.create_client(host, port))
        except socket.error:
            print('Failed to create socket')
            sys.exit()

    @gen.coroutine
    def create_client(self, host, port):
        self.sock = yield tornado.websocket.websocket_connect("ws://{0}:{1}/".format(host, port))

    @gen.coroutine
    def send(self, data):
        self.sock.write_message(data)



#Now receive data
#data = [] 

#while True:
#    chunk = s.recv(4096)  #blocks while waiting for data
#    if chunk: data.append(chunk.decode("utf8"))
    #If the recv() returns a blank string, then the other side
    #closed the socket, and no more data will be sent:
#    else: break  

#print("".join(data))

#client = LeapMotionWSClient('localhost', 8888)
#data = {1:2,3:4}
#send_data = json.dumps(data)
#while(1):    
#    client.send(send_data)
#    sys.stdin.readline()
