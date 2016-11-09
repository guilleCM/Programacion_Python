#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Crea una función que transfigura las columnas de una matriz en una nueva
#lista de filas, es decir las filas de la nueva lista creada deben 
#corresponderse a los valores de las columnas de la matriz dada.

#CASOS TEST#
#Para la siguiente lista:
#print (columnasMatriz ([[1, 2, 3],
#                        [4, 5, 6],
#                        [7, 8, 9]]))
                        
## Tiene que devolver  [[1, 4, 7],
##                      [2, 5, 8],
##                      [3, 6, 9]]

def columnasMatriz (matriz):
    matrizDeColumnas = []
    posicionParaTransformar = 0
    while len(matrizDeColumnas) < len(matriz):
        resultadoColumna = []
        for fila in matriz:
            resultadoColumna.append(fila[posicionParaTransformar])
            if len(resultadoColumna) == len(fila):
                posicionParaTransformar += 1
                matrizDeColumnas.append(resultadoColumna)
    return matrizDeColumnas