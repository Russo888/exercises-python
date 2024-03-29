nazioni=['italia', 'francia', 'inghilterra', 'città del vaticano']
capitali=['Roma', 'Parigi', 'Londra', 'città del vaticano']
appo=''
dizionario={}

for i in range(len(nazioni)):
    dizionario[nazioni[i]]=capitali[i]

print(dizionario)
    
while appo!='*':
    appo=str(input("Inserisci una nazione, \"*\" per uscire: "))
    booleano=appo in dizionario
    if booleano==True:
        print(dizionario[appo])
    else:
        print("Errore")

