import numpy as np


def multiply_arrays(first_array: np.array, second_array: np.array) -> np.array:
    """
    This function receives two arrays in the same size and multiplies them.
    :param first_array: the first array we want to multiply
    :param second_array: the second array we want to multiply
    :return an array that is a multiplication of the first_array and the second_array.
    """
    return np.multiply(first_array, second_array)


if __name__ == '__main__':
    print(multiply_arrays(np.array([[1, 2, 3], [6, 4, 3], [10, 11, 4]]), np.array([[9, 2, 1], [4, 1, 1], [1, 4, 9]])))
