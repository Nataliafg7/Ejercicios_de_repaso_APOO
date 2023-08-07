#Crear un programa que calcule la suma de los números en una lista dada



def suma(lista):
    suma = sum(lista)
    return suma

def principal():
    lista_num = [50, 15, 30, 8, 80, 71, 10]
    suma_lista = suma(lista_num)
    print(f"La suma de los números en la lista {lista_num} es:", suma_lista)
principal()