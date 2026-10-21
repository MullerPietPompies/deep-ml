def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    import numpy as np
    # if len(a) != len(b[0]):
    
    #     return -1
    try:
        a_arr = np.array(a)
        b_arr = np.array(b)

        c = np.matmul(a, b)
    except ValueError:
        return -1
    return c