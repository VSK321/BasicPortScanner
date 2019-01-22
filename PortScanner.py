import socket
import time
socket.setdefaulttimeout(0.5)

Target_Server = "192.168.0.3"

start = time.time()
for x in range(1, 65536):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    try:
        sock.connect((Target_Server,x))
        print("Port "+str(x)+" is open")
        sock.close()
        del sock
    except:
        #print("Port "+str(x)+" is closed")
        sock.close()
        del sock
print(time.time()-start)

