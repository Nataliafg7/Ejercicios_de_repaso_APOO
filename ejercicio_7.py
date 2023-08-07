#Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.


def n_menor(lista):
    menor = min(lista)
    return menor

def n_mayor(lista):
    mayor = max(lista)
    return mayor



def principal():
    lista_num = [5, 10, 15, 17, 20, 23, 25, 28, 30, 33]
    num_mayor = n_mayor(lista_num)
    num_menor = n_menor(lista_num)

    print("El número más grande en la lista es:", num_mayor)
    print("El número más pequeño en la lista es:", num_menor)
principal()