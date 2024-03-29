cont=0
lista=[]
appo=''
while appo!='*':
    appo=str(input("Inserisci una parola, \"*\" per uscire: "))
    cont=cont+1
    if appo!='*':
        lista.append(appo)
    else:
        cont=cont-1

lista.clear()

print (lista)
print ("C'erano " , cont , " parole nella lista")

