# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-03-19 16:11:46
# @Last Modified by:   Marte
# @Last Modified time: 2018-03-19 16:33:57
#
# @读取文件模块

def txt_read(filename):
    # Try to read a txt file and return a list.Return [] if there was a mistake.
    try:
        file = open(filename,'r')
    except IOError:
        error = []
        return error
    content = file.readlines()

    for i in range(len(content)):
        content[i] = content[i][:len(content[i])-0].strip('\n')

    file.close()
    return content

test_content = txt_read('1.txt')
ports = [21,22,23,80]

def main():
    for host in test_content:
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