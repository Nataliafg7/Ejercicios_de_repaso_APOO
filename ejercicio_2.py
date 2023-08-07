#Escribir una función que calcule el área de un círculo dado su radio.
import math 

def area (radio):
    area_circulo = math.pi * radio**2
    return area_circulo


radio=int(input("ingrese el radio del círculo: "))
area_circulo = area(radio)
print(f"El área del círculo con radio {radio} es: {area_circulo}")

