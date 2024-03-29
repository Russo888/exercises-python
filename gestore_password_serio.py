import pyperclip
import random


#funzione per modificare la riga nel file
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

        
#funzione per generare la password
def generaPassword():
    MAIUSCOLE= ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    MINUSCOLE=('abcdefghijklmnopqrstuvwxyz')
    NUMERICHE= ('0123456789')
    speciali= ('._*?!-')

    password=['','','','','','','','','','']

    MaiuMinu=MAIUSCOLE+MINUSCOLE
    tutto=MAIUSCOLE+MINUSCOLE+NUMERICHE+speciali
    password[0]=random.choice(MaiuMinu)

    for i in range (9):
        password[i+1]=random.choice(tutto)

    passwordStr=''.join(password)
    return passwordStr


#funzione per l'inserimento nel file
def inserimentoNelFile(stringa):
    fout = open("sitiepass.txt", "a")
    fout.write(stringa)
    fout.close()

#Funzione per l'inserimento del sito, del nome utente e della password
def inserimento():
    global containserimenti
    scelta2='0'
    sito=str(input("\nInserisci il sito: "))
    nomeutente=str(input("\nInserisci il nome utente: "))

    presenza=False
    ricerca=sito
    if containserimenti != 0:
        with open('sitiepass.txt') as fout:
            datafile = fout.readlines()
        for line in datafile:
            if ricerca in line:
                stringa=''.join(line)
                lista=stringa.split(':')
                if lista[0]==sito:
                    return ("\nIl sito è già presente nel file")

    if presenza==False:
        scelta2=str(input("\n1 per inserire una password \n2 per farla generare: "))
        if (scelta2=='1') | (scelta2=='2'):                     
            if(scelta2=='1'):
                password=str(input("\nInserisci la password: "))
                stringa=sito+": "+password +": "+nomeutente + "\n"
                inserimentoNelFile(stringa)
                containserimenti=containserimenti+1
                    
            if(scelta2=='2'):
                password=generaPassword()
                stringa=sito+": "+password +": "+nomeutente + "\n"
                inserimentoNelFile(stringa)
                containserimenti=containserimenti+1
                return ("\nLa rua nuova password è: ", password)
                
        else:
            return ("\nInserisci 1 o 2: ")


#Funzione per la ricerca
def ricerca():
    controllo=0
    ricerca=str(input("\nInserisci il sito: "))
    with open('sitiepass.txt') as fout:
        datafile = fout.readlines()
        for line in datafile:
            if ricerca in line:
                controllo=1
                stringa=''.join(line)
                lista=stringa.split(': ')
                    
                if lista[0]==ricerca:
                    outputPassword=lista[1]
                    nomeUtente=lista[2].split('/')
                    print("\nLa password per questo sito è: ", outputPassword)
                    print("\nIl nome utente per questo sito è: ", nomeUtente[0])
                    pyperclip.copy(outputPassword)
                    return("Password copiata negli appunti")
                else:
                    return("\nIl sito non è presente")

                    
        if controllo==0:
            return("\nIl sito non è presente")

#Funzione per la modifica
def modifica():
    controllo=0
    cont=0
    ricerca=str(input("\nDi quale sito vuoi cambiare la password?: "))
    with open('sitiepass.txt') as fout:
        datafile = fout.readlines()
        for line in datafile:
            cont=cont+1
            if ricerca in line:
                controllo=1
                stringa=''.join(line)
                lista=stringa.split(': ')
                    
                if lista[0]==ricerca:             
                    scelta3=str(input("\n1 per inserire una password \n2 per farla generare: "))
                    if (scelta3=='1') | (scelta3=='2'):
                        if(scelta3=='1'):
                            password=str(input("\nInserisci la password: "))
                            text=lista[0]+": "+password+": "+lista[2]
                            replace_line('sitiepass.txt', cont-1, text)
                            return ("\nPassword modificata")
                        if(scelta3=='2'):
                            password=generaPassword()                        
                            text=lista[0]+": "+password+": "+lista[2]
                            replace_line('sitiepass.txt', cont-1, text)
                            return ("\nPassword rigenerata")
                    else:
                        return("Inserire 1 o 2")
                else:
                    return("\nIl sito non è presente")

                    
        if controllo==0:
            return("\nIl sito non è presente")



#main
containserimenti=0
scelta=''
while scelta!='*':
    scelta=str(input("""\n---------------------------------------------------
1 per fare un inserimento
2 per fare una ricerca
3 per modificare una password
\"*\" per uscire: """))

    
    if scelta=='*':
        break
   
    if scelta=='1':
        print(inserimento())

    if scelta=='2':
        print(ricerca())

    if scelta=='3':
        print(modifica())
        
        

        
