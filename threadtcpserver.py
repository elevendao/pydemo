'''
Created on 2013-12-10

@author: liushuai
'''
import sys
reload(sys)
import SocketServer
from time import ctime

host = '127.0.0.1'  
port = 23456
bufsiz = 1024
ADDR = (host,port)

class MyRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        print '...connected from ',self.client_address
        while True:
            self.request.sendall('[%s] %s' %(ctime(),self.request.recv(bufsiz)))

tcpSer = SocketServer.ThreadingTCPServer(ADDR, MyRequestHandler)

print 'waiting connect...'

tcpSer.serve_forever()