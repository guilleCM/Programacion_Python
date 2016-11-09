#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Modifica el programa anterior para que en vez de mostrar 
#un mensaje genérico en el caso de que alguno o los dos números sean 
#negativos, escriba una salida diferenciada para cada una de las 
#situaciones que se puedan producir, utilizando los siguientes mensajes:
#No se calcula la suma porque el primer número es negativo.
#No se calcula la suma porque el segundo número es negativo.
#No se calcula la suma porque los dos números son negativos.

numA = int(input("Introduce el primer número: "))
numB = int(input("Introduce el segundo número: "))
if numA >= 0 and numB >= 0:
	print ("La suma de los dos números es: ", numA+numB)
elif numA < 0:
	print ("No se calcula la suma porque el primer número es negativo.")
elif numB < 0:
	print ("No se calcula la suma porque el segundo número es negativo")
else:
	print ("No se calcula la suma porque los dos números son negativos")
	