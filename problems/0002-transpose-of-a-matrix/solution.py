def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    M = len(a)
    N = len(a[0])
    lst = [[0 for _ in range(M)] for _ in range(N)]
    # T = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(len(a)):
        for j in range(len(a[i])):
            lst[j][i] = a[i][j]
    return lst