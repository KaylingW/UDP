"""Name: Kayling Wong
    PID: 5964595
    Credits: Stack overflow; https://stackoverflow.com/questions/27893804/udp-client-server-socket-in-python"""

# UDPServer.py
# UDP (SOCK_DGRAM) is a datagram-based protocol. You send one
# datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET
import random

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
# AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Waiting for connections")
while True:
    # Generate a random integer between 0 to 10.
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
   # Capitalize message from client
    message = message.upper()
    # If random integer is greater or equal to 3, send the message and its address to the socket.
    if rand >= 3:
        serverSocket.sendto(message, address)
serverSocket.close()


# Configure the server so that it randomly drops packets.
# Include information about how long each response took. This will be the RTT.
