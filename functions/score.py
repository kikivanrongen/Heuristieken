import classes.classes
import algorithms.firstsol


def score(critical_connections, t, min):
    """"""

    p = critical_connections / 22
    S = p * 10000 - (t * 20 + min / 10)

    return S
