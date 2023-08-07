#Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.




def palindromo(frase):
    frase = frase.replace(" ", "").lower() 
    return frase == frase[::-1]


def principal():
    frase_ing = input("Ingresa una frase: ")

    if palindromo(frase_ing):
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")
principal()