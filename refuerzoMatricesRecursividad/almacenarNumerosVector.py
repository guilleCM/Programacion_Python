# Autor: guilleCM
# coding=utf-8
# Enunciado:
'''
 Almacenar en un vector (una lista) 5 números enteros leídos por teclado.
 Leer a continuación otro número y comprobar si está en el vector o no. 
 En el caso de que esté visualizar qué posición ocupa. Sino indicarlo 
 mediante un mensaje. Visualizar también el elemento más pequeño, el más 
 grande y la posición de ambos en el vector.
'''

def introducirNumeros(cantidad):
    numerosIntroducidos=[]
    mensajeNumero=[
                    "primer",
                    "segundo",
                    "tercer",
                    "cuarto",
                    "quinto"
                  ]
    i=0
    while len(numerosIntroducidos) < cantidad:
        try:
            numero = int(input("Introduce el %s número entero" %mensajeNumero[i]))
        except ValueError:
            numero = 0
        numerosIntroducidos.append(numero)
        i+=1
    return numerosIntroducidos
 
def almacenNumeros():
    almacenNumeros = introducirNumeros(5)
    numeroMayorValor = max(almacenNumeros)
    numeroMenorValor = min(almacenNumeros)
    print ("Abriendo consulta:...")
    numeroConsultado = introducirNumeros(1)[0]
    if numeroConsultado in almacenNumeros:
        print ("El número consultado está en la posición %s del almacén" %almacenNumeros.index(numeroConsultado))
    else:
        print ("El número introducido no está guardado en el almacén")
    print ("Número más grande: %s en la posición %s del almacén" %(numeroMayorValor, almacenNumeros.index(numeroMayorValor)))
    print ("Número más pequeño: %s en la posición %s del almacén" %(numeroMenorValor, almacenNumeros.index(numeroMenorValor)))

  
almacenNumeros()
