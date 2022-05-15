import numpy as np


def sort_along_first_and_last_axios(original_array) -> None:
    """
    This function receives an array and prints firstly the sorted array
    by first axis, and then by the last axis.
    :param original_array: the array we want to sort by first and last axis.
    """
    print("sort by first axis:")
    print(np.sort(original_array, axis=0))
    print("sort by last axis:")
    print(np.sort(original_array))


if __name__ == '__main__':
    sort_along_first_and_last_axios(np.array([[4, 6], [2, 1]]))
