##autor: guilleCM
# coding=utf-8

##Enunciado:
##Crear una matriz de matrices en la que se recogan los objetos de un inventario
##aparece en el archivo de texto "stdout.gr". La estructura de este documento es 
##la siguiente: 
#-------- day 0 --------
#name, sellIn, quality
#+5 Dexterity Vest, 10, 20  
#Aged Brie, 2, 0
#   (linea en blanco)
#-------- day 1 --------
#
#PSEUDOCODIGO:
'''Cojo una linea del fichero, utilizo las comas como separador 
para dividir la linea en 3 partes => los meto en
una lista mediante un append... !!!OJO!!! quitar caracter 
oculto \n en las lineas del fichero que corresponde a los saltos
de linea'''
archivo = open('stdout.gr', 'r')

def creaMatrizDelInventario(archivoTexto):
	matrizInventario=[]
	contadorDias=0
	for linea in archivoTexto:
		ignorarLinea=linea.find("name" and "sellIn" and "quality")!=-1
		if linea.find("--------") == 0:
			matrizInventario.append([])
			contadorDias+=1 
		elif ignorarLinea==True or linea=="\n":
			pass
		else: 
			linea = linea.rstrip() 
			lineaPartida = linea.split(',') #OJO! todo pasa a ser string
			longitudTotal=3 
			if len(lineaPartida)>longitudTotal:
				lineaPartida[0:-2]=[','.join(lineaPartida[0:-2])]
			matrizInventario[contadorDias-1].append(lineaPartida)
	if len(matrizInventario)==contadorDias:
		return matrizInventario

print (creaMatrizDelInventario(archivo))

##CASOS TEST
#El resultado debe ser una lista con las siguientes caracteristicas
# ==> [ [  => dia 0
#	    	[item 1], [item2], []...==> dentro de cada item
#										la lista debe contener 
#		],								tres elementos [0=nombre, 1=cuando venderlo, 2=calidad]
#
#		[  => dia 1
#			[item1], [item2], []...
#		],
#
#		[  => dia...
#			[item1], [item2], [] ....
#		],
#	  ]