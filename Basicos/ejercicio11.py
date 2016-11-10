#Autor: guilleCM

#coding=utf-8

#Enunciado:
#Escribe un programa que pida por teclado tres valores de tipo entero, y que 
#calcule si se cumple que la suma de dos de ellos es igual al tercero. 
#La salida del programa tiene que tener el formato:
#Números introducidos: N1	N2	 N3 (tabulador)
#Y una de las cuatro líneas de salida siguientes:
#Se cumple que N1 = N2 + N3
#Se cumple que N2 = N1 + N3
#Se cumple que N3 = N1 + N2
#Los números no cumplen la condición

N1=int(input("Introduce el primer numero entero: "))
N2=int(input("Introduce el segundo numero entero: "))
N3=int(input("Introduce el tercer numero entero: "))
numerosIntroducidos = "Números introducidos:",N1,"\t",N2,"\t",N3
print (numerosIntroducidos)
if N1 == N2+N3:
    print ("Se cumple que", N1, "=", N2, "+", N3)
elif N2 == N1+N3:
    print ("Se cumple que", N2, "=", N1, "+", N3)
elif N3 == N1+N2:
    print ("Se cumple que", N3, "=", N1, "+", N2)
else:
    print ("Los numeros no cumplen la condicion")

#CASOS TEST#
#Caso 1
#para N1=6	N2=3	N3=3
# ==> Numeros introducidos: 6	3	 3
# ==> Se cumple que 6 = 3 + 3

#Caso 2
#para N1=5	N2=10	N3=5
# ==> Numeros introducidos: 5	10	 5
# ==> Se cumple que 10 = 5 + 5

#Caso 3
#para N1=6	N2=6	N3=12
# ==> Numeros introducidos: 6	6	 12
# ==> Se cumple que 12 = 6 + 6

#Caso 4
#para N1=1	N2=7	N3=3
# ==> Numeros introducidos: 1	7	 3
# ==> Los numeros no cumplen la condicion