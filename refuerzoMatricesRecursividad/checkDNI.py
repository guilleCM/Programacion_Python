# Autor: guilleCM
# coding=utf-8
# Enunciado:Verificar si una cadena de texto leída por teclado es
# un  DNI correcto o no. Suponer que los DNI tienen 8 dígitos
# y a continuación una letra mayúscula.


def dniCheck(string):
	'''Comprueba si el tamaño de la string es de 9 (8 numeros mas una letra).
	Comprueba si el ultimo caracter es una letra. Lo es? Comprueba
	que los primeros ocho caracteres son numeros'''
	dniIntroducido=string
	letraDNI=dniIntroducido[8:9]
	numerosDNI=dniIntroducido[0:8]

	if len(dniIntroducido) != 9:
		print ("Error de formato. Debe contener 9 caracteres (8 numero + 1 letra)")
	elif numerosDNI.isdigit() == False:
		print ("Introduce 8 números")
	elif letraDNI.isalpha() == False:
		print ("Introduce una letra")
	else:
		letraDNI=letraDNI.upper()
		return True	



#CASOS TEST#
dniCheck("122")
#==> "Error de formato"
dniCheck("1234567AB")
#==> "Introduce 8 números"
dniCheck("123456789")
#==> "Introduce una letra"
print (dniCheck("43223381X"))
#==> True
