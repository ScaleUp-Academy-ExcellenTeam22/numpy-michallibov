import numpy as np


def multiply_arrays(first_array, second_array) -> None:
    """
    This function receives two arrays in the same size and multiplies them.
    It will print the result.
    :param first_array: the first array we want to multiply
    :param second_array: the second array we want to multiply
    """
    print(np.multiply(first_array, second_array))


if __name__ == '__main__':
    multiply_arrays(np.array([[1, 2, 3], [6, 4, 3], [10, 11, 4]]), np.array([[9, 2, 1], [4, 1, 1], [1, 4, 9]]))
