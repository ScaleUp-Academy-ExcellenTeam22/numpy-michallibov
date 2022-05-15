import numpy as np


def create_evenly_distributed_vector() -> None:
    """
    This function creates an evenly distributed vector in length of 10 and the values will be
    in range of 5 to 50.
    """
    evenly_distributed_vector = np.linspace(5, 50, 10)


if __name__ == '__main__':
    create_evenly_distributed_vector()
