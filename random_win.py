import random
x=0
for i in range(100):
    att=random.randint(1, 6)
    dif=random.randint(1, 6)
    if(att>dif):
        print("l'attaccante ha vinto")
        x=x+1
    else:
        print("il difensore ha vinto")
print("la percentuale di vittoria è del ",x,"%")
