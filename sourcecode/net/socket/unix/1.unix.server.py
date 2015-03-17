#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Unix socket server
"""
import os
import os.path
import socket

SOCKET_FILE = './echo.socket'

if os.path.exists(SOCKET_FILE):
    os.remove(SOCKET_FILE)

print("Открываем UNIX сокет...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(SOCKET_FILE)

print("Слушаем...")
while True:
    datagram = server.recv(1024)
    if not datagram:
        break
    else:
        print("-" * 20)
    print(datagram)
    if "DONE" == datagram:
        break
print("-" * 20)
print("Выключение...")
server.close()
os.remove(SOCKET_FILE)
print("Выполнено")
