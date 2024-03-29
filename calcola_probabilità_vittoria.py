import random

cont=0
attaccoGiocatore=random.randint(1, 6)
difesaGiocatore=random.randint(1, 6)
for appo in range(100):
    attaccoGiocatore=random.randint(1, 6)
    difesaGiocatore=random.randint(1, 6)
    if(attaccoGiocatore>difesaGiocatore):
        cont=cont+1

print("Hai una probabilità di vittoria del",cont,"%")
