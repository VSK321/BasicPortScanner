import socket
import time
socket.setdefaulttimeout(0.5) #This decides how long the socket will wait for a response from the server

Target_Server = "" #Enter the target server's IPv4 address here eg. 192.168.0.3

start = time.time() #Begins to record the current time and stores it in the variable start
for x in range(1, 65536): #Loops through all sockets except port zero
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) #creates a socket with a port number that is assigned by the device
    try:
        sock.connect((Target_Server,x)) #Attempts to connect to the server
        print("Port "+str(x)+" is open")
        sock.close()
        del sock
    except: #If the connection fails then the following code is run
        #print("Port "+str(x)+" is closed")
        sock.close()
        del sock
print(time.time()-start) #When all the ports have been checked, the time taken in seconds is printed out

