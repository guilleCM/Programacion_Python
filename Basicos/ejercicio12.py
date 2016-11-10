#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe    un programa que pida por teclado dos números 
#y que calcule y muestre su suma solamente si:
#los dos son pares 
#el primero es menor que cincuenta 
#y el segundo está dentro del intervalo cerrado 100-500. 
#En el caso de que no se cumplan las condiciones, 
#en vez de la suma ha de visualizarse un mensaje de error.

N1 = int(input("Introduce el primer numero: "))
N2 = int(input("Introduce el segundo numero: "))
resultado = N1+N2
mensajeError = "Los numeros no cumplen las condiciones"
if N1%2==0 and N2%2==0:
	print(resultado)
elif N1<50:
	print(resultado)
elif N2>100 and N2<500:
	print(resultado)
else:
	print (mensajeError)


#CASOS TEST#
#Caso 1: los numeros son pares
#para N1=10 y N2=20
#resultado ==> 30

#Caso 2: el primero es menor que 50
#para N1=11 y N2=63
#resultado ==> 74

#Caso 3: el segundo esta entre 100 y 500
#para N1=80 y N2=101
#resultado ==> 181

#Caso 4: no se cumplen las condiciones
#para N1=51 y N2=13
#resultado ==> Los numeros no cumplen las condiciones