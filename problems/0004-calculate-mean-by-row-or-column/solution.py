def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	match mode:
		case 'column':
			count = 0
			for j in range(len(matrix[0])):
				total = 0
				for i in range(len(matrix)):
					total += matrix[i][count]
				means.append(total/len(matrix))
				count +=1

		case 'row':
			count = 0
			for i in range(len(matrix)):
				# ave calculation
				total = 0
				for j in range(len(matrix[i])):
					total += matrix[i][j]
				means.append(total / len(matrix[0]))

	return means