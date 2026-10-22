def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	import numpy as np
	vectors = np.array(vectors)
	
	return np.cov(vectors)