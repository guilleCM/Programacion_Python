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

def accesoCasosTest(matrizCasosTest, rutaArchivoTexto):
	archivoTexto=rutaArchivoTexto
	contadorDias=0
	for linea in archivoTexto:
		ignorarLinea=linea.find("name" and "sellIn" and "quality")!=-1
		if linea.find("--------") == 0:
			matrizCasosTest.append([])
			contadorDias+=1 
		elif ignorarLinea==True or linea=="\n":
			pass
		else: 
			linea = linea.rstrip() 
			linea = linea.split(',') #OJO! todo pasa a ser string
			longitudTotal=3 
			if len(linea)>longitudTotal:
				linea[0:-2]=[','.join(linea[0:-2])]
			matrizCasosTest[contadorDias-1].append(linea)
	if len(matrizCasosTest)==contadorDias:
		archivoTexto.close()
		return matrizCasosTest

#CASOS TEST
if __name__ == "__main__":
	matrizCasosTest=[]
	rutaArchivoTexto=open('stdout.gr', 'r')
	resultadoPruebaFuncion= accesoCasosTest(matrizCasosTest, rutaArchivoTexto)

	for (offset, dia) in enumerate(resultadoPruebaFuncion):
		print('-' * 8 + " Dia %d: " % offset + '-' * 8)
		for item in dia:
			print (item)

#añadir funcionalidad ==> meter esos datos (matrizCasosTest) ya
#comprobados en un archivo nuevo de texto (.txt)

def crearFicheroCasosTest(ficheroCasosTest, matrizCasosTest):
	try:
		if not isinstance(ficheroCasosTest, str):
			raise ValueError
		stdout=open(ficheroCasosTest, 'w')
	except ValueError:
		print ("La ruta de acceso al fichero ha de ser un string")
	else:
		for (offset, dia) in enumerate(resultadoPruebaFuncion):
			stdout.write("-"*8+ " Dia %d: " % offset + "-" *8 + '\n')
			for item in dia:
				stdout.write(','.join(item) + '\n')
		stdout.close()
#Crear el archivo.txt
ficheroCasosTest='./stdout.txt'
crearFicheroCasosTest(ficheroCasosTest, resultadoPruebaFuncion)