# import socket module

from socket import *

# In order to terminate the program
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket

# Fill in start
serverPort = 1111  # sets port

serverSocket.bind(('', serverPort))  # associates socket with this port

serverSocket.listen(1)  # tells socket to listen for requests
# Fill in end

while True:

    # Establish the connection

    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()  # Fill in start # Fill in end

    print('addr:\n', addr)

    try:
        message = connectionSocket.recv(1024)  # Fill in start # Fill in end

        filename = message.split()[1]

        f = open(filename[1:])

        outputdata = f.read()  # Fill in start # Fill in end

        # Send one HTTP header line into socket

        # Fill in start
        connectionSocket.send(bytes('HTTP/1.1 200 OK\r\n\r\n','UTF-8'))  # sends a 200 OK header line
        # Fill in end

        # Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found

        # Fill in start
        connectionSocket.send(bytes('404 File Not Found\r\n\r\n','UTF-8'))  # sends an error message to be printed on the page
        # Fill in end

        # Close client socket

        # Fill in start
        connectionSocket.close()  # closes the socket for the client
        # Fill in end

serverSocket.close()

sys.exit()  # Terminate the program after sending the corresponding data