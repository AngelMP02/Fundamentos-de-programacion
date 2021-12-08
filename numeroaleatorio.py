import random
numero_elegido=int(input("por favor digite un numero:"))
contador= 1
aleatorio= random.randint(0,99)
while(numero_elegido!=aleatorio) :
    contador=contador+1
    numero_elegido=int(input("por favor digite un numero:"))
    if(numero_elegido<aleatorio):
        print("introduce un numero mayor")
    elif(numero_elegido>aleatorio):
        print("Introduce un numero menor")
print("has acertado el numero en:", contador,"intentos.")

