
lista=[]
cont=0

cicli= int(input("Quanti alunni ci sono in classe?"))

for i in range (cicli):
    paese=str(input("Inserisci il paese\n"))
    lista.append(paese)

print (lista)

cercaPaese=str(input("Che paese vuoi cercare?\n"))
for i in range (cicli):
    if cercaPaese==lista[i]:
        cont=cont+1

print ("Il paese compare ", cont, " volte nella lista")
