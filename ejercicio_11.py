#Crear un programa que genere una lista de números pares entre 1 y 100.


def generar():
    lista = []
    for i in range(2, 101, 2):
        lista.append(i)
    return lista

def principal():
    lista = generar()
    print(lista)
principal()