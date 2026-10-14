def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	lst = []
	for i in range(len(a)):
		sum = 0
		for j in range(len(a[i])):
			sum = a[i][j] * b[j] + sum
		lst.append(sum)
	
	if len(a[0]) != len(lst): 
		return -1
	return lst