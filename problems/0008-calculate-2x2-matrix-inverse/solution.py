def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Create Identity matrix 
    import numpy as np
    
    matrix = np.array(matrix)

    I = np.zeros((len(matrix),len(matrix[0])))

    for i in range(len(matrix)):
        I[i][i] = 1
    
    # Calculate the determinant 

    det = matrix[0][0]* matrix[1][1] - matrix[0][1]* matrix[1][0]

    if det == 0:
        return None
    # Caclulate Inverse

    mat_2 = np.zeros((2,2))
    mat_2[0][0] = matrix[1][1]
    mat_2[0][1] = -matrix[0][1]
    mat_2[1][0] = -matrix[1][0]
    mat_2[1][1] = matrix[0][0]
    # print(matrix)
    inv = (1/det) * mat_2
    return inv 
    
