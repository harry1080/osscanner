
import sys
import os
import socket

f = open('1.txt', 'r')
sourceInLines = f.readlines()
f.close()
hosts = []
for line in sourceInLines:
     temp1 = line.strip('\n')
     temp2 = temp1.split(',')
     hosts.append(temp2)

hosts = [['192.168.0.1'], ['192.168.0.2'], ['192.168.0.3'], ['192.168.0.4']]
print hosts

ports = [21,22,23]

def main():
    for host in hosts:
        for port in ports:
            try:
                print '[+] Connecting to '+ host +':' +str(port)
                s.connect((host, port))
                s.send('Primal Security \n')
                banner = s.recv(1024)
                if banner:
                    print "[+] Port "+str(port)+" open: "+banner
                s.close()
            except:pass

if __name__ == "__main__":
    main()