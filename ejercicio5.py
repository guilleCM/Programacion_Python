#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe un programa que calcule lo que tiene que cobrar un empleado 
#sabiendo que se le tiene que aplicar al sueldo una retención del 20%.

#CASOS TEST#
#si el sueldo bruto es de 1000 euros
##El sueldo neto debe ser 800 euros

sueldo_bruto = float(input("Introduce el sueldo bruto: "))
sueldo_neto = sueldo_bruto * 0.8
print ("El sueldo neto es de ", sueldo_neto, " €")
