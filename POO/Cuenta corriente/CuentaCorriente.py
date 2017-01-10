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
from creaMatrizCasosTest import *

class DatosCuentaCorriente:
	def __init__(self,nombre,apellidos,direccion,telefono,nif,saldo):
		self.nombre=nombre
		self.apellidos=apellidos
		self.direccion=direccion
		self.telefono=telefono
		self.nif=nif
		self.saldo=saldo

	def __str__(self):
		return '[Propietario: %s %s, Direccion: %s, Telefono: %s, NIF: %s, Saldo Disponible: %s]' %(self.nombre, self.apellidos, self.direccion, self.telefono, self.nif, self.saldo)

class InterfazCuentaCorriente():
	def setNombre(self, nombre):
		self.nombre=nombre
	def setApellidos(self, apellidos):
		self.apellidos=apellidos
	def setDireccion(self, direccion):
		self.direccion=direccion
	def setTelefono(self, telefono):
		self.telefono=telefono
	def setNif(self, nif):
		self.nif=nif
	def setSaldo(self, saldo):
		self.saldo=saldo

	def getNombre(self):
		return self.nombre
	def getApellidos(self):
		return self.apellidos
	def getDireccion(self):
		return self.direccion
	def getTelefono(self):
		return self.telefono
	def getNif(self):
		return self.nif
	def getSaldo(self):
		return self.saldo


	def retirarDinero(self, cantidad):
		if cantidad>self.saldo:
			print ("No dispone de tal cantidad para retirar")
			print ("Su saldo disponible es de", self.saldo)
		else:
			self.saldo=self.saldo-cantidad
			print ("Ha retirado %s€, su saldo disponible es de %s€" %(cantidad, self.saldo))

	def ingresarDinero(self, cantidad):
		self.saldo+=cantidad

	def saldoNegativo(self):
		if self.saldo<0:
			return True
		else:
			return False

	def consultarCuenta(self):
		print(self)

class CuentaCorriente(InterfazCuentaCorriente, DatosCuentaCorriente):
	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
		DatosCuentaCorriente.__init__(self, nombre, apellidos, direccion, telefono, nif, saldo)

class Cliente(CuentaCorriente):
	def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
		DatosCuentaCorriente.__init__(self, nombre, apellidos, direccion, telefono, nif, saldo)



if __name__=='__main__':
	guilleCM = Cliente("Guillermo", "Cirer Martorell", "C/ Tenor Bou Roig", 717114964, "43223381X", 60)
	guilleCM.ingresarDinero(40) #saldo pasa a ser 100
	guilleCM.setNombre("Pedro") #nombre pasa a ser Pedro
	guilleCM.consultarCuenta() #comprueba que lo anterior se ha cumplido