# -------------SERVER--------------------

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.bind(('127.0.0.1',5000))
s.listen(5)
conn,addr = s.accept()
while True:
    try:
        conn.send(bytes('server : ' + input('Me : '), encoding ='utf-8'))
        print('\n')
        rec = str(conn.recv(1024))
        l = list(rec)
        l.pop()

        
        l.pop(0)
        l.pop(0)
        p = ''.join(l)
        print(p)
        print('\n')
    except:
        print('Connection Lost.......!!')
        print('Client Have Left The Chat')
        

