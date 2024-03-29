nazioni=['italia', 'francia', 'inghilterra', 'città del vaticano']
capitali=['Roma', 'Parigi', 'Londra', 'città del vaticano']
appo=''
while appo!='*':
    appo=str(input("Inserisci una nazione, \"*\" per uscire: "))
    for i in range(len(nazioni)):
        if appo==nazioni[i]:
            print (capitali[i])
            break
        if i==len(nazioni)-1:
            print ("Messaggio di errore")
