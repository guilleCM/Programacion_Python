#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe    un programa que pida por teclado dos números y que
# muestre en pantalla uno de los dos mensajes siguientes en 
#función de los números leídos: 
#a) el primer número (valor) es mayor que el 
#segundo (valor)(introduciendo el valor de los números
# en el mensaje); 
#b) el primer número (valor) es menor que el segundo (valor;
#c) los dos números son iguales (valor).

#CASOS TEST#
#para numA = 7 y numB = 1 ; La solucion es la a)
#para numB = 1 y numB = 7 ; La solucion es la b)
#para numA = 1 y numB = 1 ; La solucion es la c)
numA = int(input("Introduce el número A: "))
numB = int(input("Introduce el número B: "))
if numA > numB:
	print ("El número ", numA, "es mayor que ",numB)
elif numA < numB:
	print ("El número ", numA, "es menor que ", numB)
else: 
	print ("El número ", numA, "es igual a ", numB)