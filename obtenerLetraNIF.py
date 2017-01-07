# Autor: guilleCM
# coding=utf-8
#Enunciado:
#Hacer un programa que dado un número de DNI obtenga la letra del NIF.
#La letra correspondiente a un número de DNI se calcula mediante el siguiente algoritmo: 
#Se obtiene el resto de dividir el número de DNI entre 23. 
#El número resultante nos indica la posición de la letra correspondiente a ese DNI, en la siguiente cadena:
diccionarioAsignacion={	 0:"T",
						 1:"R",
						 2:"W",
						 3:"A",
						 4:"G",
						 5:"M",
						 6:"Y",
						 7:"F",
						 8:"P",
						 9:"D",
						 10:"X",
						 11:"B",
						 12:"N",
						 13:"J",
						 14:"Z",
						 15:"S",
						 16:"Q",
						 17:"V",
						 18:"H",
						 19:"L",
						 20:"C",
						 21:"K",
						 22:"E"
						 }

listaAsignacion=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

def accesoDatos(lista):
	datos=diccionarioAsignacion
	if type(datos) is list:
		return lista.extend(datos)
	elif type(datos) is dict:
		return lista.extend(list(datos.values()))

def asignarLetraDNI(numero):
	assert isinstance(numero, int), "no estas utilizando un numero entero"
	posicionLetra=numero%23
	listaAsignaciones=[]
	accesoDatos(listaAsignaciones)
	letraAsignada=listaAsignaciones[posicionLetra]
	return letraAsignada




 #CASOS TEST
print (asignarLetraDNI(43461531))
#==> H
print (asignarLetraDNI(43223381))
#==> X
