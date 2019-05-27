"""Name: Kayling Wong
    PID: 5964595
    Credits: Stack overflow; https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python"""
import time
import socket

#For pings in the range of 10
for pings in range(10):
    #Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Set timeout value to 1 second
    client_socket.settimeout(1.0)
    #Ping to server.
    message ='Ping!'
    addr = ("127.0.0.1", 12000)
    #Ping is sent here
    start = time.time()
    client_socket.sendto(message, addr)
    #Print if data is received from the server.
    try:
        data, server = client_socket.recvfrom(2048)
        end = time.time()
        #Elapsed: Time took to receive minus the Time that it was sent
        elapsed = end - start
        #Print the data, pings and the time elapsed.
        print(f'{data} {pings} {elapsed}')
        #If it takes more than one second, print REQUEST TIMED OUT.
    except socket.timeout:
        print('REQUEST TIMED OUT')

#Allow the client to give up if no response has been received within 1 second.