import numpy as np


def add_a_vector_to_matrix(vector: np.array, matrix: np.array) -> None:
    """
    This function gets a vector and a matrix and creates a new matrix in which each row is each row
    of the given matrix + the vector.
    :param vector: the vector we want to add to each row of the matrix.
    :param matrix: the matrix we want to add to each of it's rows the vector.
    """
    print(matrix + vector)


if __name__ == '__main__':
    add_a_vector_to_matrix(np.array([1, 2, 3]), np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]]))
