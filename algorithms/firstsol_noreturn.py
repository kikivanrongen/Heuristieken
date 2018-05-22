import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def firstsol_noreturn(data, max_t):
    """ First algorithm for a random solution. No returns possible. """

    # initalize variables
    trains = classes.classes.Trains(data)

    # for loop for 7 trains
    for t in range(max_t):

        start = random.choice(data.names)

        # find random trajectory with no returns allowed
        train = random_trajectory_noreturns(start, data)

        # store train in class
        trains.add_train(train)

    return trains
