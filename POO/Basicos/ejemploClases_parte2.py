# Autor: guilleCM
# coding=utf-8

# Capitulo 27 Learning Python (Programando Clases)

from ejemploClases import FirstClass
class SecondClass (FirstClass):
	def display(self):
		print ("Me comporto distinto '%s'" %self.data)

z=SecondClass()
z.setdata("Soy un rebelde")
z.display()


class ThirdClass(SecondClass):
	def __init__(self, value):
		self.data=value
	def __add__(self, other):
		return ThirdClass(self.data+other)
	def __str__(self):
		return '[ThirdClass: %s]' %self.data
	def mul(self, other):
		self.data *= other

a=ThirdClass('abc')		#invoca a __init__
a.display()				#invoca a display() de SecondClass
print(a)				#invoca a __str__: que devuelve una string por pantalla

#Crea una instancia invocando a _add__
b = a + 'xyz'
b.display()
print(b)

a.mul(3)	#Cambia la instancia a
print(a)