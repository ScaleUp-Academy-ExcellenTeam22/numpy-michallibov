import numpy as np


def create_and_print_number_of_rows_and_cols(given_array) -> None:
    """
    This function creates an array and prints the amount of rows and
    columns that this array has.
    :param given_array: A given array from the main which we will check it's size.
    """
    my_array = given_array
    number_of_rows, number_of_columns = my_array.shape

    print("Rows = ", number_of_rows)
    print("Columns = ", number_of_columns)


if __name__ == '__main__':
    create_and_print_number_of_rows_and_cols(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
