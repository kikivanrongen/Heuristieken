import matplotlib.pyplot as plt
import numpy as np

def hist(scorevector, title):
    """ Function that makes a histogram of the interations of the solution. The
    scorevector of all iterations will be the input argument."""

    # plot histogram
    plt.figure(3)
    plt.hist(scorevector, 30)
    plt.xlabel("score")
    plt.ylabel("frequentie")
    plt.title(title)
    plt.show()
