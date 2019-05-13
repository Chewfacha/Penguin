#Creamos un archivo nuevo
#Guardamos en la carpeta del repositorio
#Con la extensión .py
#Uso de numeros aleatorios
#Importamos la libreria randint
from random import randint
aleatorio=randint(0,20)  #Creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio)       #Imprimimos el número generado

#EJERCICIO
#Escribir una función sorteo () que reciba una lista de participantes, y elegir a uno de los participantes
#aleatoriamente y retornar esa persona elegida
#DESAFIO
#No volver a retornar una persona ya sorteada

from random import randint

def sorteo (Participantes):
        return sorteo
print("el ganador es ", sorteo)
Participantes=["Gus","Willi","Yumi","Brian","Anastasia"]
Participantes=randint(0,4)










from random import randint       #Importamos la función randint de libreria random
def sorteo_fin_de_año (lista):   #Definimos una función
    cant=len(lista) -1           #Utilizamos len() para saber la cantidad de personas que hay en la lista y
#guardamos en cant, se le resta 1 en la cantidad porque debido al indice sobre 1 (el indice arranca en cero pues)
    indice=randint(0,cant)       #Generamos un indice aleatorio
    ganador=lista[indice]        #Seleccionamos un elemento de la lista y guardamos
    return ganador               #Retornamos ganador
#Creamos la lista de los participantes
participantes=["Kami","Lucas","Vale","Sarita","Fede"]
#Llamamos a la función y guardamos en una variable el resultado retornado por la función
ganar=sorteo_fin_de_año(participantes)
print("El ganador es",ganar)  #Imprimimos el ganador