def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	import numpy as np
	# result = np.zeros((len(matrix), len(matrix[0])))
	# for i in range(len(matrix)):
	# 	for j in range(len(matrix[0])):
	# 		result[i][j] = matrix[i][j] * scalar 
	# return result

	return (np.array(matrix) * scalar).tolist()