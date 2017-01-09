# Autor: guilleCM
# coding=utf-8
# Enunciado:
#Crea un tablero de ajedrez (matriz 8 x 8). Los escaques de color negro se
#representan por un 1 y los de color blanco con un 0. Muestra por pantalla 
#el contenido de la matriz simulando un tablero de ajedrez.

def tableroAjedrez():
	linea=[[1],[0]]*4
	print (str(linea) + "\n" + (str(linea[::-1])) + "\n" )*4

tableroAjedrez()