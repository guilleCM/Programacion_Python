# Autor: guilleCM
# coding=utf-8

# Capitulo 27 Learning Python (Programando Clases)

class FirstClass: 				# Define el objeto PrimeraClase
	def setdata(self,value):	# Define los métodos de la clase ()
		self.data=value			# Self es la instancia
	def display(self):
		print(self.data)		# self.data: por instancia

x = FirstClass()	# Creamos dos instancias de la clase (x,y)						
y = FirstClass()	# Cada una con su propio espacio de nombres			

x.setdata("King Arthur")
#Busca el atributo setdata en la clase de la cual es instancia x
#encuentra el metodo ==> def setdata(self,value):
							#self.data=value
#Ahora self es x, y el value es "King Arthur"
y.setdata(3.14159)
#Lo mismo hace con la instancia y

#Asi que si ahora llamamos al método display() nos devolvera el valor
x.display() #==> "King Arthur" que es de tipo string
y.display() #==> "3.14159" que es de tipo float

#Como ahora ya se han generado las variables "data" en nuestras
#instancias, podemos reasignarles el valor. Sin antes haberlas 
#generado, no sería posible puesto que no existirían en su espacio
#de nombres:

x.data="nuevo valor"
x.display() #==> "nuevo valor"

#Podemos incluso generar nuevos atributos en el espacio de nombres 
#de la instancia, asignandoles nombres a los atributos,y estos estaran
#fuera del espacio de nombres de la clase de la que son instancia
x.anothername="spam"

#Creamos otra clase que hereda de una SuperClase
class SecondClass(FirstClass):	#Hereda los métodos de FirstClass
	def display(self):			#Cambia el método display. Override
		print ("El valor es = '%s'" %self.data)
#Creamos una instancia del objeto SegundaClase
z=SecondClass()
z.setdata(17)
z.display()

