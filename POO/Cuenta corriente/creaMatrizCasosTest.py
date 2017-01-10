

archivo = open('clientes.gr', 'r')

def creaMatrizDelInventario(archivoTexto):
	matrizInventario=[]
	contadorDias=0
	for linea in archivoTexto:
		ignorarLinea=linea.find("nombre" and "apellidos" and "direccion")!=-1
		if linea.find("--------") == 0:
			matrizInventario.append([])
			contadorDias+=1 
		elif ignorarLinea==True or linea=="\n":
			pass
		else: 
			linea = linea.rstrip() 
			lineaPartida = linea.split(',') #OJO! todo pasa a ser string
			longitudTotal=6 
			matrizInventario[contadorDias-1].append(lineaPartida)
	if len(matrizInventario)==contadorDias:
		return matrizInventario
	archivo.close()