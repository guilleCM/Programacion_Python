# Autor: guilleCM
# coding=utf-8
# Enunciado:
#Crea un tablero de ajedrez (matriz 8 x 8). Los escaques de color negro se
#representan por un 1 y los de color blanco con un 0. Muestra por pantalla 
#el contenido de la matriz simulando un tablero de ajedrez.

def tableroAjedrez(numero):
	assert isinstance(numero, int), "La función solo admite números enteros"
	dimensiones=numero/2
	linea=[[1],[0]]*dimensiones
	print (str(linea) + "\n" + (str(linea[::-1])) + "\n" )*dimensiones

#CASOS TEST
tableroAjedrez(4)
#==>[[1], [0], [1], [0]]
#	[[0], [1], [0], [1]]
#	[[1], [0], [1], [0]]
#	[[0], [1], [0], [1]]

tableroAjedrez(8)
#==>[[1], [0], [1], [0], [1], [0], [1], [0]]
#	[[0], [1], [0], [1], [0], [1], [0], [1]]
#	[[1], [0], [1], [0], [1], [0], [1], [0]]
#	[[0], [1], [0], [1], [0], [1], [0], [1]]
#	[[1], [0], [1], [0], [1], [0], [1], [0]]
#	[[0], [1], [0], [1], [0], [1], [0], [1]]
#	[[1], [0], [1], [0], [1], [0], [1], [0]]
#	[[0], [1], [0], [1], [0], [1], [0], [1]]