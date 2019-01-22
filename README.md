# BasicPortScanner
A basic port scanner that uses TCP connections to check if the port on the target server is open.
The program creates a socket that is assigned a port number by the device and attempts to connect with one of the 65535 ports and once it has connected, or failed to connect, the socket is deleted. 
If the socket connects then it prints the port that it has connected to as being open else nothing is printed unless the hashed out line is used.
The program could be made faster by using threading as it would allow for multiple sockets to be made and to connect with multiple ports simultaneously. 
