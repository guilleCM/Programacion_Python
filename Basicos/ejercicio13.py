#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Diseña un programa que calcule el importe final de una venta 
#considerando que sobre el valor bruto se hace un descuento según
#la siguiente tabla:
##a) Valores <=20 implican un descuento del 0%
##b) Valores >20 y <=100 implican un descuento descuento del 5%
##c) Valores >100 implican un descuento 10%

valor = float(input("Introduce el precio bruto: "))

if valor<=20:
	print (valor)
elif valor>20 and valor<=100:
	print (valor*0.95)
else:
	print (valor*0.90)


#CASOS TEST#
#Caso 1: Para valor=20
# Importe final ==> 20

#Caso 2: Para valor=100
# Importe final ==> 95

#Caso 3: Para valor=200
# Importe final ==> 180