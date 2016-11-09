# Autor: guilleCM

# coding=utf-8
# Enunciado:
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


def greatest(lista):
    resultado = 0
    for valor in lista:
        if valor > resultado:
            resultado = valor
    return resultado


#CASOS TEST#
print (greatest([4,23,1]))
#>>> 23
print (greatest([]))
#>>> 0
