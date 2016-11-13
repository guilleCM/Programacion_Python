#Autor: guilleCM

#coding=utf-8

# Enunciado:
# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric(matriz):
    valorColumna = 0
    filasComprobadas = 0
    for fila in matriz:
        posicionColumna = 0
        check = 0
        for valor in fila:
            if valor == matriz[posicionColumna][valorColumna]:
                check = check + 1
                posicionColumna += 1
            if check == len(fila):
                valorColumna += 1
                filasComprobadas += 1
    if filasComprobadas == len(matriz):
            return True
 
##CASOS TEST##    
print (symmetric([[1, 2, 3],
                  [2, 3, 4],
                  [3, 4, 1]]))
