
import random
cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 
lista=[1,2,3,4,5,6,7,8,9,10,10,10,10]
numero1=random.randint(1,11)
numero2=random.randint(1,11)
primeracarta=lista[numero1]
segundacarta=lista[numero2]
sumacartas=primeracarta+segundacarta

print("tu primera carta es,",primeracarta)
print("tu segunda carta es;",segundacarta)
print("la suma de sus cartas es:", sumacartas)

numerobanca1=random.randint(1,11)
numerobanca2=random.randint(1,11)
carta1banca=lista[numerobanca1]
carta2banca=lista[numerobanca2]

bancatotal=carta1banca+carta2banca
print("el valor de la banca es de:",bancatotal)
if sumacartas>bancatotal:
    print("Ha ganado, su suma es mayor que la de la banca")
else:
    print("Ha perdido, la suma de sus cartas no es superior a la de la banca")