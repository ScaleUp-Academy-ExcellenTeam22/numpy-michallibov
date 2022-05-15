import numpy as np


def create_and_print_number_of_rows_and_cols() -> None:
    """
    This function creates an array and prints the amount of rows and
    columns that this array has.
    """
    my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    number_of_rows, number_of_columns = my_array.shape

    print("Rows = ", number_of_rows)
    print("Columns = ", number_of_columns)


if __name__ == '__main__':
    create_and_print_number_of_rows_and_cols()
