import numpy as np


def swap_first_and_last_rows(randomized_array) -> None:
    """
    This function gets an array and swaps it's first rows with it's last rows.
    :param randomized_array: the array that we will swap it's first and last rows.
    """
    swapped_array = randomized_array[::-1]


def randomize_array() -> None:
    """
    This function creates a random array in the size of 4x4. It then calls the function
    swap_first_and_last_rows to swap the first rows with the last rows.
    """
    randomized_array = np.random.rand(4, 4)
    swap_first_and_last_rows(randomized_array)


if __name__ == '__main__':
    randomize_array()
