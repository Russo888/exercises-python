vet = []
prod=1
for aggiunto in range(10):
    nuovo= int(input("Aggiunti un numero all'array: "))
    vet.append(nuovo)
for numero in range (10):
        prod=prod*vet[numero]

print("il prodotto è ", prod)
