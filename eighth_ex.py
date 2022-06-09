import numpy as np


def replace_with_0_array_values(array_to_replace: np.array, number_to_compare: float, comparison: str) -> np.array:
    """
    This function receives a np array and a number. It will compare each value in the array to the
    given number. If the value in the array doesn't satisfy the term (equals, smaller or larger then
    the given number), it will replace the value with 0. It then will print the new array with the
    replaced values.
    :param comparison: the comparison of the numbers in the array_to_replace to the number_to_compare.
    The options are- '<', '=', '>'.
    :param array_to_replace: the array that we will compare each of it's values to the given number.
    :param number_to_compare: the given number to which we will compare each value from the array.
    :return a new matrix depending on the comparison we received.
    """
    return {
        '<': np.where(array_to_replace < number_to_compare, 0, array_to_replace),
        '=': np.where(array_to_replace == number_to_compare, 0, array_to_replace),
        '>': np.where(array_to_replace > number_to_compare, 0, array_to_replace)
    }[comparison]


if __name__ == '__main__':
    print(replace_with_0_array_values(np.array([[9.54, 8.38, 5.9549], [3.6, 8.32, 6.99], [1.5, 22.2, 10.23]]), 8.32, '<'))
    print(replace_with_0_array_values(np.array([[9.54, 8.38, 5.9549], [3.6, 8.32, 6.99], [1.5, 22.2, 10.23]]), 8.32, '='))
    print(replace_with_0_array_values(np.array([[9.54, 8.38, 5.9549], [3.6, 8.32, 6.99], [1.5, 22.2, 10.23]]), 8.32, '>'))
