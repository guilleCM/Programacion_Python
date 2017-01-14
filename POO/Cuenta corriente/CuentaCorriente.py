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

class CuentaCorriente:

    def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__direccion = direccion
        self.__telefono = telefono
        self.__nif = nif
        self.__saldo = saldo
    # SETTERS

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setApellidos(self, apellidos):
        self.__apellidos = apellidos

    def setDireccion(self, direccion):
        self.__direccion = direccion

    def setTelefono(self, telefono):
        self.__telefono = telefono

    def setNif(self, nif):
        self.__nif = nif

    def setSaldo(self, saldo):
        self.__saldo = saldo
    # GETTERS

    def getNombre(self):
        return self.__nombre

    def getApellidos(self):
        return self.__apellidos

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    def getNif(self):
        return self.__nif

    def getSaldo(self):
        return self.__saldo

    def __str__(self):
        return '[Propietario: %s %s, Direccion: %s, Telefono: %s, NIF: %s, Saldo Disponible: %s]' % (self.__nombre, self.__apellidos, self.__direccion, self.__telefono, self.__nif, self.__saldo)

    def saldoNegativo(self):
        if self.__saldo < 0:
            return True
        else:
            return False

    def consultarCuenta(self):
        print(self)

    def ingresarDinero(self, cantidad):
        self.__saldo += cantidad

    def retirarDinero(self, cantidad):
        if cantidad > self.__saldo:
            print("No dispone de tal cantidad para retirar")
            print("Su saldo disponible es de", self.saldo)
        else:
            self.__saldo = self.__saldo-cantidad
            print("Ha retirado %s€, su saldo disponible es de %s€" %
                  (cantidad, self.__saldo))





if __name__=='__main__':
	guilleCM = CuentaCorriente("Guillermo", "Cirer Martorell", "C/ Tenor Bou Roig", 717114964, "43223381X", 60)
	guilleCM.ingresarDinero(40) #saldo pasa a ser 100
	guilleCM.retirarDinero(100)
	guilleCM.setNombre("Pedro") #nombre pasa a ser Pedro
	guilleCM.consultarCuenta() #comprueba que lo anterior se ha cumplido
	cuentaGuille = CuentaCorriente("Guillermo", "Cirer Martorell", "C/ Tenor Bou Roig", 717114964, "43223381X", 60)
	print(cuentaGuille.getNombre())
	print(cuentaGuille.setNif("re"))
	print(cuentaGuille.getNif())