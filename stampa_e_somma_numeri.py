x=0
somma=0
for aggiunto in range(10):
    nuovo= int(input("Digita un numero: "))
    x=x+1
    somma= somma+nuovo
    if somma >= 100: break
print ("I numeri stampati sono: " + str(x) + "  La somma è: " + str(somma))
