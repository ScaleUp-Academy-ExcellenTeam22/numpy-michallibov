import numpy as np
import matplotlib.pyplot as plt


def draw_sine_function() -> None:
    """
    This function draws the sine function using the matplotlib library. 
    """
    x_parameter = np.arange(0, 3 * np.pi, 0.2)
    y_parameter = np.sin(x_parameter)
    plt.plot(x_parameter, y_parameter)
    plt.show()


if __name__ == '__main__':
    draw_sine_function()