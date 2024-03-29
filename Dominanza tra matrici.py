#Dominanza tra matrici (esercizio slide 8)

def domina(mA,mB,r,c):
    maggiorimA=0
    maggiorimB=0
    for i in range(r):
        for j in range(c):
            if mA[i][j]>mB[i][j]:
                maggiorimA=maggiorimA+1
            elif mA[i][j]<mB[i][j]:
                maggiorimB=maggiorimB+1
    if maggiorimA>maggiorimB:
        return 1
    elif maggiorimA<maggiorimB:
        return -1
    elif maggiorimA==maggiorimB:
        return 0

r=int(input('Inserire numero righe: '))
c=int(input('Inserire numero colonne: '))
mA=[] 
for i in range(r):
    nA=[]
    for j in range(c):
        x=int(input("Inserire elemento A: "))
        nA.append(x)
    mA.append(nA)
mB=[] 
for i in range(r):
    nB=[]
    for j in range(c):
        x=int(input("Inserire elemento B: "))
        nB.append(x)
    mB.append(nB)

if domina(mA,mB,r,c)==1:
    print(' ')
    print('A domina B')
elif domina(mA,mB,r,c)==-1:
    print(' ')
    print('B domina A')
elif domina(mA,mB,r,c)==0:
    print(' ')
    print('Nessuna dominanza')
