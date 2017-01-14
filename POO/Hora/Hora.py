# Autor: guilleCM
# coding=utf-8
# Enunciado:
'''
Construye una clase de nombre Hora que permita almacenar la hora, así como 
los métodos para manipularla (este es nuestro ADT). Tendrá las siguientes propiedades y métodos:
	Propiedades (todas ellas privadas):
	hora: de tipo entero (00 - 24)
	minutos: de tipo entero (00 - 59)
	segundos: de tipo entero (00 - 59)
Constructor (inicializador en Python):
	Constructor que, por defecto, inicialice las propiedades de la clase a 0 [programación defensiva].
	Constructor al que se le pasen como argumentos tres enteros y se los asigne a las propiedades
	de la clase. Si la cantidad recibida no satisface las restricciones de los valores
    impuestos a horas, minutos y segundos, el valor que se fija es 0 [Manejo de errores]:
    devolver un valor neutro, aunque en este caso no lo sea.
Métodos de la clase (públicos):
	setHora(): recibe como argumentos tres enteros y se los asigna a las propiedades de la clase.
	Utiliza el mismo nombre en las variables que reciben los argumentos y en las propiedades
	de la clase. Este método ha de diseñarse mediante programación por contrato, es decir,
	debe incluir una precondición: si los valores recibidos no satisfacen las restricciones 
	de los valores impuestos a horas, minutos y segundos, el valor que se establece es
	0 [Manejo de errores: devolver un valor neutro, aunque en este caso no lo sea].
	Ya que va a ser utilizado en el cosntructor, este precondición podría implementarse 
	en su propia rutina para ser llamada desde este método y desde el “constructor”.
	getHora(): devuelve la hora como una lista de la forma [horas, minutos, segundos] o como un string de la forma "horas:minutos:segundos".
	imprimirHora() que muestra en consola la hora en formato string de la forma "horas:minutos:segundos".
	Métodos set() y get() para todas las propiedades [Abstracción y encapsulamiento].
'''

class Hora:

    def __init__(self, hora=0, minutos=0, segundos=0):
    	'''
    	Inicializo un constructor defensivo, que coge los argumentos
    	y los pasa por la funcion setHora. La funcion devuelve 3 valores
    	válidos o neutros para garantizar que las propiedades de la clase
    	tomarán los valores esperados.
    	'''
        constructorDefensivo = Hora.setHora(hora, minutos, segundos)
        self.__hora = constructorDefensivo[0]
        self.__minutos = constructorDefensivo[1]
        self.__segundos = constructorDefensivo[2]

    def __str__(self):
        return str(self.__hora)+":" + str(self.__minutos) + ":"+str(self.__segundos)

    @staticmethod
    def setHora(hora=0, minutos=0, segundos=0, *ignorarRestoArgumentos):
    	'''
    	Los tres primeros argumentos son los que nos interesan.
    		- hora tiene que estar entre 0 y 23
    		- minutos y segundos tienen que estar entre 0 y 59
    	Si se pasan valores que no estan entre esos rangos, o de otro 
    	tipo (como strings) los formateará al valor neutro 0 [defensivamente]
    	'''
        if hora not in range(0, 24, 1):
            hora = 0
        if minutos not in range(0, 60, 1):
            minutos = 0
        if segundos not in range(0, 60, 1):
            segundos = 0
        return hora, minutos, segundos

    def getHora(self):
        propiedades = [str(self.__hora), str(self.__minutos), str(self.__segundos)]
        resultado = []
        for propiedad in propiedades:
            if len(propiedad) != 1:
                resultado.append(propiedad)
            else:
                resultado.append("0"+propiedad)
        return resultado

    def imprimirHora(self):
        propiedadesFormateadas = ':'.join(Hora.getHora(self))
        print(propiedadesFormateadas)
        return propiedadesFormateadas
