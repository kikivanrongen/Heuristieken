import matplotlib.pyplot as plt
import numpy as np

def hist(scorevector):
    """ Function that makes a histogram of the interations of the solution."""

    # plot histogram
    plt.hist(scorevector)
    plt.xlabel("score")
    plt.ylabel("frequentie")
    plt.show()
