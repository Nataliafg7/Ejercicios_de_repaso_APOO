#Crear una función que convierta grados Fahrenheit a grados Celsius.



def conversion(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def grados():
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = conversion(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit es {celsius} grados Celsius.")
grados()
