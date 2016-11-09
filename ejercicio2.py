# coding=utf-8
#Enunciado ejercicio: Escribe un programa que 
#pida por teclado el radio de una circunferencia,
#y que a continuación calcule y escriba en pantalla
#la longitud de la circunferencia y del área del círculo.
#
# Autor: guilleCM
#
# Casos test:
# para radio = 2
# ==> 12.56 (longitud)
# ==> 12.56 (area)
#
# para radio = 4
# ==> 25.12 (longitud)
# ==> 50.24 (area)

radio = float(input("Escribe el radio de la circunferencia: "))
diametro = radio * 2
numero_pi = 3.14
longitud = diametro * numero_pi
area = radio * radio * numero_pi
print(longitud)
print(area)
