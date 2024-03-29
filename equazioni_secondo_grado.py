import math
scelta=input("Vuoi continuare?(s o n):  ")
while scelta == 's':
    a= int(input("Inserisci il primo valore: "))
    b= int(input("Inserisci il secondo valore: "))
    c= int(input("Inserisci il terzo valore: "))
    equazione=print(str(a) + "x^2 + " + str(b) + "x + " + str(c) + "=0")
    delta =b*b - 4*a*c
    if delta < 0 :
        print("Equazione impossibile!!!")
    if delta > 0 :
        x1= ((-b - math.sqrt(delta))/ 2*a)
        x2= ((-b + math.sqrt(delta))/ 2*a)
        print (x1)
        print (x2)
    scelta=input("Vuoi continuare?(s o n):  ")
