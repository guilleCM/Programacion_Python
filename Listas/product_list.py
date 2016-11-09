#Autor: guilleCM

#coding=utf-8

#Enunciado:
# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.


def product_list(lista):
    resultado = 1
    for valor in lista:
        resultado = valor * resultado
    return resultado


#CASOS TEST#
print (product_list([9]))
#>>> 9
print (product_list([1, 2, 3, 4]))
#>>> 24
print (product_list([]))
#>>> 1
