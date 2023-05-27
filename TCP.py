import threading
import requestHandler
def threading_socket(connectionSocket):
    try:
        request = connectionSocket.recv(1024).decode()
        print(request)
        header = request.split('\n')
        print(header)
        print(header[0])
        print(header[0].split()[1])
        response = requestHandler.requestHandler(filename=header[0].split()[1])
        connectionSocket.send(response.encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("File Not Found".encode())
        connectionSocket.close()

from socket import *
import sys
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 8080
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#prepare server socket
while True:
    print('Ready to serve ...')
    print('Server is running on port', serverPort)
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=threading_socket, args=(connectionSocket,)).start()
    

serverSocket.close()
sys.exit()