#autor: guilleCM

# coding=utf-8

#Enunciado:
#Define un programa que recoge una lista desordenada de numeros enteros en un
#rango de 1 a "x" y la pone en orden de modo que el 1 es el primero de la lista
#y "x" debe ser el último.

def ordenarLista(lista):
    numeroLista=1
    listaOrdenada=[]
    while len(listaOrdenada) != len(lista):
        for numero in lista:
            if numero==numeroLista:
                listaOrdenada.append(numero)
                numeroLista+=1
    return listaOrdenada
    
    
##CASOS TEST##
###Caso1######
testLista1 = [12, 10, 11, 9, 8, 7, 4, 6, 5, 2, 1, 3]
print (ordenarLista(testLista1))
###===> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]