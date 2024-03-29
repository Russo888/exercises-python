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

print ("Ci sono " , cont , " parole nella lista")
print (lista)

lista.sort()
print ("Lista ordinata in ordine alfabetico crescente: /n")
print (lista)

lista.reverse()
print ("Lista ordinata in ordine alfabetico decrescente: /n")
print (lista)
