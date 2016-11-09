#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe un programa que pida por teclado dos valores de tipo 
#numérico que se han de guardar en sendas variables.
#¿Qué instrucciones habría que utilizar para intercambiar 
#su contenido? (es necesario utilizar una variable auxiliar). 
#Para comprobar que el algoritmo ideado es correcto,
#muestra en pantalla el contenido de las variables 
#una vez leídas, y vuelve a mostrar su contenido una 
#vez hayas intercambiado sus valores.
#
##CASO TEST##
#para numA = 1 y numB = 7
#tiene que devolver numA = 7 y numB = 1

numA = int(input("Introduce el número A: "))
numB = int(input("Introduce el número B: "))
variable_aux = numA
numA = numB
numB = variable_aux
print ("El numero A intercanviado es: ", numA)
print ("El numero B intercanviado es: ", numB)
