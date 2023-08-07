#Crear una función que invierta el orden de los elementos en una lista dada.


#my_list = [10, 1, 8, 3, 5]

def invertir_lista(lista):
    invertida = lista[::-1] 
    return invertida

def principal():
    list = [1, 2, 3, 4, 5]

    invertida = invertir_lista(list)
    print("Lista:", list)
    print("Lista invertida:", invertida)
principal()