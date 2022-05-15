import numpy as np


def create_vector_with_negative_and_positive_values() -> None:
    """
    This function creates a vector with values in the size of 20. The values of each cell equals to
    the index of the cell. The function then will change the values of indexes 9-15 to negative.
    """
    vector_with_index_values = array = np.arange(20)
    vector_with_index_values[9:16] *= -1


if __name__ == '__main__':
    create_vector_with_negative_and_positive_values()
