#Juego de adivinar el número, todos juntos
#Adivinar un número generado aleatoriamente
#Ir introduciendo por teclado el dato a adivinar

from random import randint
generado=randint(0,10)      #Generamos el número aleatorio
print(generado)   #trampa
condicion=True
intento=10
while condicion:
    if intento>0:
        numero=input("Dame un número del 0 al 10: ")
        intento=intento-1
        if generado==int (numero):   #Comparamos el número introducido
            print ("Lore te regala una anvorgesa")
            condicion=False
        else:
            print("Le debes una pizza a Lore")
            print("Te quedan", intento, "intentos")
    else:
        condicion=False
        print("¡PERDISTE!")