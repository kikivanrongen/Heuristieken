import __init__ as im

def hist(scorevector, title):
    """ Function that makes a histogram of the interations of the solution. The
    scorevector of all iterations will be the input argument."""

    # plot histogram
    im.plt.hist(scorevector, 20)
    im.plt.xlabel("score")
    im.plt.ylabel("frequentie")
    im.plt.title(title)
    im.plt.show()
