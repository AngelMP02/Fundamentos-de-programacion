import random
def seleccionar_nivel():
    print("seleccione el nivel de difultad del 1 al 4:")
    print("\n 1:simple"+"\n 2:intermedio"+"\n 3:Avanzado"+"\n 4:experto")
    nivel_elegido=int(input())
    nivel=nivel_elegido
    if nivel>0 and nivel<=4:
        if nivel==1:
            print("Has elegido el nivel Simple")

        elif nivel==2:
            print("Has elegido el nivel Intermedio")
        
        elif nivel==3:
            print("has elegido el nivel Dificil")
        elif nivel==4:
            print("Has elegido el nivel Experto")

        else:
            print("el nivel que ha puesto no existe")
    
seleccionar_nivel()

def selecciondeljugador():
    print("Escriba 1 si quiere jugar con ayuda de la IA")
    print("Escriba 2 si quiere jugar usted")
    seleccionjugador=int(input())
    seleccion=seleccionjugador
    if  seleccion>0 and seleccion <=2:
        if seleccion == 1:
            print("Has elegido que juegue la IA")
        elif seleccion== 2:
            print("Has elegido jugar tu")
    else:
        print("has puesto un numero que no correspoinde a ninguna opcion")
selecciondeljugador()
if seleccionar_nivel==1 and selecciondeljugador==1:
    numero_a_adivinar=random.randint (0,101)
    print("Adivina el numero del numero del 1 al 100 en el menor numero de intentos posible")
    num_IA=random.randint (0,101)
    print(num_IA)
    numero_intentos=1
    numero_intentos_max=10
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    while num_IA != numero_a_adivinar and numero_intentos < numero_intentos_max:
        print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
        if numero_a_adivinar < num_IA:
            print("El numero que ha salido es menor")
            numIA= random.randint (numero_a_adivinar,numIA)
            print(num_IA)
            numero_intentos= numero_intentos +1
        elif numero_a_adivinar > num_IA:
            print("El  numero es mayor")
            numIA= random.randint (numIA,numero_a_adivinar)
            print(num_IA)
    if numero_intentos >= numero_intentos_max:
        print("Se han acabado los intentos")
    elif numero_a_adivinar==num_IA:
        print("Has ganado, has acertado el numero en", numero_intentos ,"intentos")

if seleccionar_nivel==1 and selecciondeljugador==2:
    numero_intentos=random.randint(0,101)
    print("Digite un número:")
    num=int(input())
    print(numIA)
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    numero_intentos=1
    numero_intentos_max=10
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    while numIA != numero_a_adivinar and numero_intentos<numero_intentos_max:
         print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
         if numero_a_adivinar<num:
              print("El numero que ha salido es menor")  
              num=int(input())
              print(num)
              numero_intentos= numero_intentos +1
         elif num <numero_a_adivinar:
             print("el numero que hay que encontrar es mayor que el introducido")
             num=int(input())
             print(num)
             numero_intentos= numero_intentos +1

    if numero_intentos >= numero_intentos_max:
            print("Se te han acabado los intentos")
    elif numero_a_adivinar==num:
        print("Has ganado, has acertado el numero en", numero_intentos ,"intentos")     

    if seleccionar_nivel==2 and seleccionar_nivel==1:
        print("Has seleccionado el nivel intermedio, adivina el numero del 1 al 1000 en 25 intentos")
        num_IA=random.randint(0,1001)  
        numero_intentos=1
        numero_intentos_max=25   
        numero_intentos_restantes=numero_intentos_max-numero_intentos
        while num_IA!= numero_a_adivinar and numero_intentos<numero_intentos_max:
            print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
            if numero_a_adivinar<num_IA:
                print("Selecciona un numero menor")
                num_IA=random.randit(numero_a_adivinar,num_IA)
                print(num_IA)
                numero_intentos=numero_intentos+1
            elif numero_a_adivinar>num_IA:
                print("selecciona un numero mayor")
                num_IA=random.randit(num_IA,numero_a_adivinar)
                print(num_IA)
                numero_intentos=numero_intentos+1
            if numero_intentos<=numero_intentos_max:
                print("Se te han acabado los intentos")
            if numero_a_adivinar==num_IA:
                print("¡has acertado el numero en", numero_intentos,"intentos!")
    if seleccionar_nivel==2 and selecciondeljugador==2:
       print("Has seleccionado el nivel intermedio, adivina el numero del 1 al 1000 en 25 intentos")
       numero_a_adivinar=random.randint(0,1001) 
       print("Digite un número:")
       num=int(input()) 
       numero_intentos=1
       numero_intentos_max=25   
       numero_intentos_restantes=numero_intentos_max-numero_intentos
       while num!=numero_a_adivinar and numero_intentos<numero_intentos_max:
            print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
            if num<numero_a_adivinar:
                print("Introduce un numero mayor")
                num=int(input())
                numero_intentos=numero_intentos+1
            elif  num<numero_a_adivinar:
                print("introduce un numero menor:")
                num=int(input())
                numero_intentos=numero_intentos+1

            if numero_intentos>=numero_intentos_max:
                print("Te has quedado sin intentos, fin de el juego")
            if numero_a_adivinar==num:
                print("Has ganado, has acertado el numero en", numero_intentos ,"intentos")
        
if seleccionar_nivel==3 and selecciondeljugador==1:
    print("Has elegido que juegue la IA el nivel avanzado,tienes que adivinar un número del 0 al 1.000.000 . tienes 100 intentos")
    numero_a_adivinar=random.randint(0,1000001)
    numIA=random.randint (0,1000000)
    numero_intentos=1
    numero_intentos_max=100
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    while numIA!=numero_a_adivinar and numero_intentos<numero_intentos_max:
        print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
        if num_IA<numero_a_adivinar:
            print("El numero introducido es menor")
            numIA= random.randint (numero_a_adivinar,numIA)
            print(numIA)
            numero_intentos=numero_intentos+1
        elif num_IA>numero_a_adivinar:
            print("El numero introducido es mayor")
            numIA= random.randint (numIA,numero_a_adivinar)
            print(numIA)
            numero_intentos=numero_intentos+1
    if numero_intentos>=numero_intentos_max:
        print("Has alcanzado el limite de intentos")
    if numero_a_adivinar==numIA:
        print("Has ganado, has acertado el numero en", numero_intentos ,"intentos")
    
if seleccionar_nivel and selecciondeljugador==2:
    print("Has seleccionado jugar tu el nivel avanzado,tienes que adivinar un número del 0 al 1.000.000 . tienes 100 intentos")
    print("digite un numero")
    numero_a_adivinar=random.randint (0,1000001)
    num=int(input())
    numero_intentos=1
    numero_intentos_max=100
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    while num!=numero_a_adivinar and numero_intentos<numero_intentos_max:
        print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
        if num<numero_a_adivinar:
            print("el numero introducido es menor")
            num=int(input())
            numero_intentos==numero_intentos+1
        if num>numero_a_adivinar:
            print("el numero introducido es mayor")
            num=int(input())
            numero_intentos==numero_intentos+1
    if numero_intentos>=numero_intentos_max:
        print("Has alcanzado el limite de intentos")
    if num==numero_a_adivinar:
        print("Has ganado, has acertado el numero en", numero_intentos ,"intentos")

if seleccionar_nivel==4 and selecciondeljugador==1:
    numero_a_adivinar=random.randint (0,10000000001)
    print("Has seleccionado el nivel Experto, tienes que adivinar un número del 0 al 100.000.000 . Tienes 150 intentos")
    numero_intentos=1
    numero_intentos_max=150
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    num_IA=random.randint (0,10000000001)
    while num_IA!=numero_a_adivinar and numero_intentos<numero_intentos_max:
        print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
        if numero_a_adivinar<num_IA:
            print("introduzca un numero menor")
            num_IA=random.randint (numero_a_adivinar,num_IA)
            print(num_IA)
            numero_intentos=numero_intentos+1
        if numero_a_adivinar>num_IA:
            print("Introduzca un numero mayor:")
            num_IA=random.randint (num_IA,numero_a_adivinar)
            print(num_IA)
            numero_intentos=numero_intentos+1
    if numero_intentos>=numero_intentos_max:
        print("te has quedado sin intentos")
    if numIA==numero_a_adivinar:
        print("Has ganado, has acertado el numero en", numero_intentos ,"intentos")
    
    if seleccionar_nivel==4 and selecciondeljugador==2:
        print("Has seleccionado jugar tu el nivel experto,tienes que adivinar un número del 0 al 100.000.000 en menos de 150 intentos") 
    print("Digite un numero")
    num=int(input()) 
    numero_intentos=1
    numero_intentos_max=150
    numero_intentos_restantes=numero_intentos_max-numero_intentos
    numero_a_adivinar=random.randint (0,10000000001)
    while num!=numero_a_adivinar and numero_intentos<numero_intentos_max:
        print("llevas", numero_intentos,"intentos, te quedan", numero_intentos_restantes,"intentos")
        if numero_a_adivinar<num:
            print("introduzca un numero mejor:")
            num=int(input())
            numero_intentos= numero_intentos+1
        elif numero_a_adivinar>num:
            print("Introduzca un numero mayor:")
            num=int(input())
            numero_intentos= numero_intentos+1
    if numero_intentos>=numero_intentos_max:
        print("te has quedado sin intentos")
    if numero_a_adivinar==num:
        print(("Has ganado, has acertado el numero en", numero_intentos ,"intentos"))

        


      

 
        

        


 









    
             







    

            



