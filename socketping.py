import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for n in range(50, 52):
    server_ip="192.168.1.{0}".format(n)
    rep = os.system('ping ' + server_ip)
    if rep == 0:
        print ("server is up" ,server_ip)
    else:
        print ("server is down" ,server_ip)
