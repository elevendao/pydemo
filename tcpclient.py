#!/usr/bin/python
# -*-coding: utf-8 -*-
'''
Created on 2013-12-10

@author: liushuai
'''
import socket

host = '127.0.0.1'  
port = 23456
bufsiz = 1024
ADDR = (host,port)

tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(bufsiz)
    if not data:
        break
    print data

tcpCliSock.close()