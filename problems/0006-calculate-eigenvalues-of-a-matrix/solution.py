def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	'''
	a very manual mathematical way of doing it 
	'''
	
	# Simple 2x2 determinant
	import math
	detA = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	
	# Small Trace helper function (sum of the main diagonal)
	def trace(matrix):
		result = 0
		for i in range(len(matrix)):
			result += matrix[i][i]
		return result

	# lambda**2 - trance(matrix)* lambda + det(A) = 0
	eigen = []
	
	eigen.append((trace(matrix)+ math.sqrt((-trace(matrix))**2 - 4*detA))/2)
	eigen.append((trace(matrix)- math.sqrt((-trace(matrix))**2 - 4*detA))/2)
	return eigen
	# return eigenvalues