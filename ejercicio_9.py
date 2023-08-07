#Crear un programa que genere una matriz de números y la imprima en pantalla.

def Crear_Matriz (Fil, Col, Mat):
    for i in range (Col):
        for f in range (Fil):
            Dato=int(input("Ingrese un dato numérico"))
            Mat [f] [i] = Dato

def Espacios_Matriz (Fil, Col, Mat):
    for i in range(Fil):
        Mat.append([0]*Col)
    return Mat

def Mostrar_Matriz (Fil, Col, Mat):
    for i in range (Fil):
        for c in range (Col):
            print(Mat[i][c],end="\t")
        print("\n")

def main():
    Matriz=[]
    Filas=int(input("Ingrese la cantidad de filas "))
    Columnas=int(input("Ingrese la cantidad de columnas "))
    Matriz1=Espacios_Matriz (Filas, Columnas, Matriz)
    Crear_Matriz (Filas, Columnas, Matriz1)
    Mostrar_Matriz (Filas, Columnas, Matriz1)
main()