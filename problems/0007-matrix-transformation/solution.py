import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	try: 
		
		np.linalg.inv(S)
		return np.matmul(np.linalg.inv(T), np.matmul(A, S))
	# if np.isnan(np.linalg.inv(S)).any():
	# 	return -1
	except:
		return -1

	