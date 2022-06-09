import numpy as np


def sort_by_last_axios(original_array: np.array) -> np.array:
    """
    This function receives an array and returns the sorted array by the last axis.
    :param original_array: the array we want to sort by last axis.
    :return the sorted array by the last axis.
    """
    return np.sort(original_array)


def sort_by_first_axios(original_array: np.array) -> np.array:
    """
    This function receives an array and returns the sorted array by first axis.
    :param original_array: the array we want to sort by first axis.
    :return the sorted array by the first axis.
    """
    return np.sort(original_array, axis=0)


if __name__ == '__main__':
    print("sort by first axis:")
    print(sort_by_first_axios(np.array([[4, 6], [2, 1]])))
    print("sort by last axis:")
    print(sort_by_last_axios(np.array([[4, 6], [2, 1]])))
