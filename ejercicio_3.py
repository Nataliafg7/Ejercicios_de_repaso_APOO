#Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.
import random

def lista():
    lista_aleatoria = [random.randint(1, 20) for i in range(10)] 
    print(lista_aleatoria)

lista()