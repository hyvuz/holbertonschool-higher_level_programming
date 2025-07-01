def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        squared = list(map(lambda elm: elm * elm, row))
        new_matrix.append(squared)
    return new_matrix
