import classes.classes
from functions.random_trajectory import random_trajectory
import random

def firstsol(data, max_t):
    """ First algorithm for a random solution. """

    # initalize variables
    trains = classes.classes.Trains(data)

    # for loop for 7 trains
    for t in range(max_t):

        start = random.choice(data.names)

        # find random trajectory
        train = random_trajectory(start, data)

        # store train in class
        trains.add_train(train)

    return trains
