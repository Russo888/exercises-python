coda = []

continua=True
while continua==True:
    scelta=int(input("Inserisci la scelta: \n 1 per inserire una canzone\n 2 per ascoltare una canzone con il titolo\n 3 per ascoltare la prima canzone\n 4 per vedere la lista delle canzoni\n 5 per chiudere\n"))
    
    if scelta==1:
        scelta2=int(input("1 per inserire una canzone all'inizio della playlist\n 2 per inserire una canzone alla fine della playlist\n"))
        if scelta2==1:
            canzone=str(input("Inserisci il titolo della canzone\n"))
            coda.insert(0, canzone)
            
        if scelta2==2:
            canzone=str(input("Inserisci il titolo della canzone\n"))
            coda.append(canzone)
            
    if scelta==2:
        cercaCanzone=str(input("Inserisci il titolo della canzone\n"))
        for i in range (len (coda) ):
            esecuzione = coda [i]
            if cercaCanzone==esecuzione:
               print("avvio canzone: ", esecuzione)
            
    if scelta==3:
        if len(coda)==0:
           print("Playlist vuota")
        else:
           esecuzione=coda.pop(0)
           print("avvio canzone: ", esecuzione)
           
    if scelta==4:
        print("Coda delle lavorazioni")
        for i in range (len (coda) ):
            esecuzione = coda [i]
            print("Canzoone: ", esecuzione)
           
    if scelta==5:
        continua=False;
         

