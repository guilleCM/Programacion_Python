# Autor: guilleCM
# coding=utf-8

# Capitulo 28 Learning Python (Programando Clases, ejemplo Realista)

# Vamos a crear dos clases
# Persona ==> Que crea y procesa informacion sobre gente
# Manager ==> Una personalizacion de Persona que modifica su
			 #Comportamiento interno

class Person:
	#queremos que almacene informacion basica sobre la gente
	#Por ello generaremos atributos que se inicializarán en 
	#cada instancia de persona
	def __init__(self, name, job=None, pay=0): 
	#Constructor. Self será la nueva instancia del objeto. 
	#job sera opcional asi que por defecto sera None, y por lo tanto pagara 0
		self.name=name
		self.job=job
		self.pay=pay
	#name, job y pay seran la informacion sobre el estado
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay=int(self.pay*(1+percent))
	def __repr__(self):
		return '[Person: nombre: %s, cobra: %s]' %(self.name, self.pay)

class Manager(Person):
	def giveRaise(self, percent, bonus=.10):
		#self.pay=int(self.pay*(1+percent + bonus))  ==> copy/paste
		#del método original añadiendo el bonus. Malo, para extensiones
		#futuras tendriamos q cambiar el codigo en dos sitios
		#La mejor manera es llamar al original y aumentarlo los argumentos
		Person.giveRaise(self, percent + bonus)

#CASOS TEST#
if __name__=='__main__':
	#self-test code. When run for testing only
	#Testeando los atributos de las instancias
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(bob.name, bob.pay)
	print(sue.name, sue.pay)
	#Testing modificando los atributos de las instancias
	print(bob.lastName(), sue.lastName())
	sue.giveRaise(.10)
	print(sue)
	tom=Manager('Tom Jones', 'mgr', 50000)
	tom.giveRaise(.10)
	print(tom.lastName())
	print(tom)
	tom.someThingElse()
	print (tom)
	print("---Los tres---")
	for obj in (bob, sue, tom):
		obj.giveRaise(.10)
		print(obj)