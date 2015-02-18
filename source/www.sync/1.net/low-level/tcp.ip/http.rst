HTTP
====

open http://www.binarytides.com/python-socket-programming-tutorial/

.. code:: python

    import socket

    tcpsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsoc.bind(('72.14.192.58', 80)) #bind to googles ip
    tcpsoc.send('HTTP REQUEST')
    response = tcpsoc.recv()
