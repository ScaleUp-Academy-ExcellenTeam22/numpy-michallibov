import numpy as np


def create_array_filled_with_zeros_with_border_of_ones() -> None:
    array_with_border_of_ones_filled_with_zeros = np.ones((10, 10))
    # Fill the inside of the array with zeros (from index 1 till the last one- not included)
    array_with_border_of_ones_filled_with_zeros[1:-1, 1:-1] = 0


if __name__ == '__main__':
    create_array_filled_with_zeros_with_border_of_ones()