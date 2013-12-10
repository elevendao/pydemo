#!/usr/bin/python
# -*-coding: utf-8 -*-
'''
Created on 2013-12-10

@author: liushuai
'''
import sys
reload(sys)
import socket
from time import ctime

'''
host为空表示bind可以绑定到所有有效地址上
port 必须要大于1024
bufsiz为缓冲区 我们设置为1K
'''
host = '127.0.0.1'  
port = 23456
bufsiz = 1024
ADDR = (host,port)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)   #参数表示允许多少连接同时连进来

try:
    while True:
        '''
        进入服务器的无限循环中，等待连接到来
        有链接时，进入对话循环，等待客户发送数据，如果消息为空，表示客户端已经退出，等待下一个客户端连接
        得到客户端消息后在消息前加一个时间戳后返回
        '''
        print 'waiting for connection...'
        tcpSerSock,addr = tcpSerSock.accept()
        print '...connected from ',addr

        while True:
            data = tcpSerSock.recv(bufsiz)
            if not data:
                break
            tcpSerSock.send('[%s] %s' %(ctime(),data))
except BaseException, e:
    tcpSerSock.close()  #记住在服务器退出时记得关闭
