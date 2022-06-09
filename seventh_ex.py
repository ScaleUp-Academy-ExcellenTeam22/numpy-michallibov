import numpy as np


def print_swapped_first_and_last_rows(randomized_array) -> None:
    """
    This function gets an array and swaps it's first rows with it's last rows. It prints
    the swapped array.
    :param randomized_array: the array that we will swap it's first and last rows.
    """
    print(randomized_array[::-1])


def randomize_array() -> np.array:
    """
    This function creates a random array in the size of 4x4.
    :return: the randomized array.
    """
    return np.random.rand(4, 4)


if __name__ == '__main__':
    print_swapped_first_and_last_rows(randomize_array())
