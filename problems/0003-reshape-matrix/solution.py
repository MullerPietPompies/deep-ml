import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	reshaped_matrix = np.zeros((new_shape[0], new_shape[1]))
	a_size = len(a) * len(a[0])
	new_size = len(reshaped_matrix) * len(reshaped_matrix[0])

	if a_size != new_size:
		return []
	flat = np.zeros(a_size)
	count = 0
	for i in range(len(a)):
		for j in range(len(a[0])):
			flat[count] = a[i][j]
			count+=1
	count = 0
	for i in range(new_shape[0]):
		for j in range(new_shape[1]):
			reshaped_matrix[i][j] = flat[count]
			count+=1
	return reshaped_matrix.tolist()