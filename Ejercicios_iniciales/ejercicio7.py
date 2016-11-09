#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe un programa que pida por teclado un número y 
#que a continuación muestre el mensaje el número leído es 
#positivo o bien el número leído es negativo dependiendo 
#de que el número introducido por teclado sea 
#positivo o negativo. Consideramos al número 0 positivo.

#CASOS TEST#
#para numero = 2
#tiene que devolver ("El número introducido es positivo")
#
#para numero = -3
#tiene que devolver ("El número introducido es negativo")

numero = int(input("Introduce un número: "))

if numero >= 0:
	print ("El número introducido es positivo")
else:
	print ("El número introducido es negativo")