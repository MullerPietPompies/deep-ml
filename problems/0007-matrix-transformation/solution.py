import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	try: 
		np.linalg.inv(S)
		np.linalg.inv(T)
		return np.matmul(np.linalg.inv(T), np.matmul(A, S))
	except np.linalg.LinAlgError:
		return -1

	