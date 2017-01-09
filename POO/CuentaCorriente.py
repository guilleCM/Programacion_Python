# Autor: guilleCM
# coding=utf-8
# Enunciado:
##Construye una clase de nombre CuentaCorriente que permita almacenar
##los datos asociados a la cuenta bancaria de un cliente, e interactuar con ellos.

#Propiedades privadas (de momento, en Python nos da igual que sean privadas): 
####nombre, apellidos, dirección, teléfono: todas de tipo string.
####NIF: objeto instancia de la clase DNI que resolvimos en clase**. Se trata de una relación “Has-A” o “Tiene-una”.
####saldo: de tipo double.

#Constructores (inicializador en Python): 
####Constructor que por defecto inicializa las propiedades de la clase (programación defensiva).
####Constructor al que se le pasen como argumentos todas las propiedades que tiene la clase.

#Métodos públicos: 
####set() y get() para todas las propiedades de la clase [Abstracción y encapsulamiento].
####retirarDinero(): resta al saldo una cantidad de dinero pasada como argumento.
####ingresarDinero(): añade al saldo una cantidad de dinero.
####consultarCuenta(): visualizará los datos de la cuenta.
####saldoNegativo(): devolverá un valor lógico indicando si la cuenta está o no en números rojos.

class OperacionesCuentaCorriente:
	def retirarDinero(self, cantidad):
		if cantidad>self.saldo:
			print ("No dispone de tal cantidad para retirar")
			print ("Su saldo disponible es de", self.saldo)
		else:
			self.saldo=self.saldo-cantidad
			print ("Ha retirado %s€, su saldo disponible es de %s€" %(cantidad, self.saldo))
	def ingresarDinero(self, cantidad):
		self.saldo+=cantidad
	def consultarCuenta(self):
		pass
	def saldoNegativo(self):
		if self.saldo<0:
			return True
		elif self.saldo==0:
			return ("Está a 0")
		else:
			return False

class DatosCuentaCorriente:
	def __init__(self,nombre,apellidos,direccion,telefono,nif,saldo):
		self.nombre=nombre
		self.apellidos=apellidos
		self.direccion=direccion
		self.telefono=telefono
		self.nif=nif
		self.saldo=saldo
	def __repr__(self):
		return '[Propietario: %s %s, Direccion: %s, Telefono: %s, NIF: %s, Saldo Disponible: %s]' %(self.nombre, self.apellidos, self.direccion, self.telefono, self.nif, self.saldo)

class CuentaCorriente(OperacionesCuentaCorriente, DatosCuentaCorriente):
	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
		DatosCuentaCorriente.__init__(self, nombre, apellidos, direccion, telefono, nif, saldo)





if __name__=='__main__':
	marian = CuentaCorriente("Marian", "Rodenas Pocovi", "C/ Jacinto Benavente", "622224680", "43461531H", 5000)
	guilleCM = CuentaCorriente("Guillermo", "Cirer Martorell", "C/ Tenor Bou Roig", "717114964", "43223381X", 6000)
	print(marian)
	print(guilleCM)

	for obj in (marian, guilleCM):
		obj.retirarDinero(5000)
		obj.ingresarDinero(5000)
		obj.saldoNegativo()
		print (obj)