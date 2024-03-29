from socket import *
import random

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))

num=random.randint(0, 9)
message=""
print (num)
vite=5

while message!="BYE":
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode('utf-8')
    print (message)

    if message!=str(num)and(message!="INDIZIO"):
        print (message)
        risposta="Numero sbagliato"
        serverSocket.sendto(risposta.encode("utf-8"),clientAddress)
        vite=vite-1
    
    if message=="INDIZIO":
        if num>4:
            risposta="Il numero è maggione o uguale a 5"
        else:
            risposta="Il numero è minore di 5"
        serverSocket.sendto(risposta.encode("utf-8"),clientAddress)

    if str(num)==message:
        print (message)
        risposta="Numero indovinato, e tu sei il numero 1"
        serverSocket.sendto(risposta.encode("utf-8"),clientAddress)
        break

    if vite==0:
        break
    
risposta="ADDIOS"
serverSocket.sendto(risposta.encode("utf-8"),clientAddress)
