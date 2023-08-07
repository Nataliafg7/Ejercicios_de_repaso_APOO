#. Escribir una función que calcule la media aritmética de una lista de números


def cal_media(lista):
    suma = sum(lista)
    elementos = len(lista)
    media = suma / elementos
    return media

def main():
    lista_num = [8, 50, 30, 40, 50]
    media = cal_media(lista_num)
    print(f"La media aritmética de la lista {lista_num} es: {media}")
main()