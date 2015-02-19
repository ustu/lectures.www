import socket

# TCP/IP socket
sock_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock_obj.connect(('httpbin.org', 80))
sock_obj.send("GET /ip HTTP/1.0\n\n")

while True:
    resp = sock_obj.recv(1024)
    if resp == "":
        break
    print resp

# Close the connection when completed
sock_obj.close()
