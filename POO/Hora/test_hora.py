# coding=utf-8
import pytest
from Hora import Hora

def test_setHora():
	'''
	Establece la hora.
	Cada argumento que no se le pase, lo inicializará a 0. Es decir,
	si se le pasan solo las horas, inicializará minutos y segundos a 0.
	Si se le pasa otro tipo de argumento, lo inicializa a valor neutro 
	igualmente.
	'''
	assert (0, 0, 0) == Hora.setHora()
	assert (10, 0, 0) == Hora.setHora(10)
	assert (0, 0, 10) == Hora.setHora(27, 1000, 10)
	assert (0, 39, 0) == Hora.setHora("stringTest", 39)
	assert (0, 39, 0) == Hora.setHora(12.25, 39)
	assert (22, 20, 0) == Hora.setHora(22, 20, 0, 1, 3, "Toma argumentos")

def test_inyector():
	objetoConstruido = Hora("stringTest",3)
	return objetoConstruido