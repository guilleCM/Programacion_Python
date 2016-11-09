# coding=utf-8
#Escribe un programa que calcule el área de una finca rectangular
#en metros cuadrados, así como su perímetro exterior, también en
#metros.
#Autor: GuilleCM

#CASOS TEST#
#para largo_finca = 10 y ancho_finca = 4
#tiene que devolver
#area_finca ==> 40
#perimetro_exterior ==> 28

print("Introduce el largo de la finca en metros:")
largo_finca = float(input())
print("Introduce el ancho de la finca en metros:")
ancho_finca = float(input())
area_finca = largo_finca * ancho_finca
perimetro_exterior = (largo_finca * 2) + (ancho_finca * 2)
print("El área de su finca es de ", area_finca, " metros cuadrados")
print("El perímetro de su finca es de ", perimetro_exterior, " metros")

