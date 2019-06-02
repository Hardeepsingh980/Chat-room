#------------CLIENT--------------------

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect(('127.0.0.1',5000))
while True:
    try:
    
        rec = str(s.recv(1024))
        l = list(rec)
        l.pop()
            
        l.pop(0)
        l.pop(0)
        p = ''.join(l)
        print(p)
        print('\n')
        s.send(bytes('Client : ' + input('Me : '), encoding ='utf-8'))
        print('\n')

    except:
        print('Connection Lost.........!!')
        print('Please Reconnect....!!')
        break
    



