from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print("IL server è pronto a ricevere")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)
