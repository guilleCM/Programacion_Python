
#Rutina 


def esCuadrado(sudoku):


	for fila in sudoku:
		if len(fila) != len(sudoku):
			return False
	return True
#	if len(sudoku[0]) != len(sudoku[1]) or len(sudoku[0]) != len(sudoku[2]):
#		return False

#	if len(sudoku) == len(sudoku[0]):
#		return True
#	else: 
#		return False



	#longitud primer elemento de sudoku == longitud sudoku







correcto1 = [[1, 2, 3],
             [2, 3, 1],
             [3, 1, 2]]

correcto2 = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 3],
               [4, 4, 4, 4]]


incorrecto3 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 3, 4],]


print(esCuadrado(correcto1) )
# -> True

print(esCuadrado(correcto2) )
# -> True

print(esCuadrado(incorrecto2) )
# -> False

print(esCuadrado(incorrecto3) )
# -> False
