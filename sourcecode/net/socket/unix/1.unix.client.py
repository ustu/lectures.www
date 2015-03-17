#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Unix socket client
"""
import socket
import os
import os.path

SOCKET_FILE = './echo.socket'

print("Подключение...")
if os.path.exists(SOCKET_FILE):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(SOCKET_FILE)
    print("Выполнено.")
    print("Ctrl-C что бы выйти.")
    print("Отправьте 'DONE' что бы выключить сервер.")
    while True:
        try:
            x = input("> ")  # for py2 use raw_input
            if "" != x:
                print("ОТПРАВЛЕНО: %s" % x)
                client.send(x.encode('utf-8'))
                if "DONE" == x:
                    print("Выключение.")
                    break
        except KeyboardInterrupt as k:
            print("Выключение.")
            break
    client.close()
else:
    print("Не могу соединиться!")
print("Выполнено")
