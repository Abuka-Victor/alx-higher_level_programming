def square_matrix_simple(matrix=[]):
    newMatrix = []
    
    for i in matrix:
        newMatrix.append(list(map(lambda x: x ** 2, i)))
    return newMatrix
