#Crear un programa que genere una matriz de números y la imprima en pantalla.

def matriz (Fil, Col, Mat):
    for i in range (Col):
        for f in range (Fil):
            num=int(input("Ingrese un numero"))
            Mat [f] [i] = num

def Espacios_Matriz (Fil, Col, Mat):
    for i in range(Fil):
        Mat.append([0]*Col)
    return Mat

def Mostrar_Matriz (Fil, Col, Mat):
    for i in range (Fil):
        for c in range (Col):
            print(Mat[i][c],end="\t")
        print("\n")

def principal():
    Matriz=[]
    Filas=int(input("Ingrese la cantidad de filas "))
    Columnas=int(input("Ingrese la cantidad de columnas "))
    Matriz1=Espacios_Matriz (Filas, Columnas, Matriz)
    matriz (Filas, Columnas, Matriz1)
    Mostrar_Matriz (Filas, Columnas, Matriz1)
principal()