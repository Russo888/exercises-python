from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message=""
print("indovina il numero compreso tra 0 e 9, BYE per fermare")

contindizi=0
vite=5

while message!="BYE":

    
    if contindizi==0:
        print("""Inserisci il numero, se vuoi un indizio digita \"INDIZIO\",
Digita \"BYE\" per arrenderti. """, vite, """ tentativi: """)
        message=input("")
        
    if contindizi==1:
         print("""Inserisci il numero,
Digita \"BYE\" per arrenderti. """, vite, """ tentativi: """)
         message=input("")
         
    if message=="INDIZIO":
        contindizi=1;

        
    clientSocket.sendto(message.encode("utf-8"), (serverName, serverPort))
    risposta,serverAddress=clientSocket.recvfrom(2048)
    risposta=risposta.decode("utf-8")
    print(risposta)
    if risposta=="Numero indovinato, e tu sei il numero 1":
        break
    if risposta=="Numero sbagliato":
        vite=vite-1;
