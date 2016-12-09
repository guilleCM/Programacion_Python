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
	#inicializo la lista que contendra las listas de los dias dentro
	matrizInventario=[]
	contadorDias=0
	for linea in archivoTexto:
		#variable para comprobar si encuentra las tres palabras
		#que no me interesan de la linea
		ignorarLinea=linea.find("name" and "sellIn" and "quality")!=-1
		#si encuentra la linea correspondiente al dia, añade una lista nueva
		#a la definida anteriormente como matrizInventario
		if linea.find("--------") == 0:
			print("linea contiene referencia a Dia")
			matrizInventario.append([])
			contadorDias+=1 #la siguiente vez que encuentre un dia se agregara
							#en la posicion correspondiente de la lista
		elif ignorarLinea==True or linea=="\n":
			print("Linea con contenido esteril")
			pass #si encuentra las palabras que no nos interesan o una linea en blanco pasamos
		else: #descartados los dos casos anteriores, encuentra contenido de los items
			print("Linea con contenido util")
			linea = linea.rstrip() #elimina el caracter oculto \n del final de la linea
			lineaPartida = linea.split(',') #divide la linea segun las "," que tiene y mete 
											#las partes en una lista. OJO! todo pasa a ser string
			longitudTotal=3 #establezco que la lista como maximo tendra tres posiciones
							#la 0==>(nombreItem), la 1==>(ventaItem), la 2==>(calidadItem)
			if len(lineaPartida)>longitudTotal:
			######Si supera la longitud establecida, como en el caso de ['Sulfuras,'] ['Hand of Ragnaros'],
			######nos interesa juntar el nombre del item en la posicion 0 de la lista
				lineaPartida[0:longitudTotal-1]=[','.join(lineaPartida[0:longitudTotal-1])]
			matrizInventario[contadorDias-1].append(lineaPartida)
	if len(matrizInventario)==contadorDias:
		print("POSTCONDICION OK")
		return matrizInventario

creaMatrizDelInventario(archivo)

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