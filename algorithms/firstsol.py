import classes.classes
from functions.random_trajectory import random_trajectory
import random

def firstsol(data):
    """ First algorithm for a random solution. """

    # initalize variables
    max_t = 7
    trains = classes.classes.Trains(data)
    start = random.choice(data.names)

    # for loop for 7 trains
    for t in range(max_t):

        # find random trajectory
        train = random_trajectory(start, data)

        # store train in class
        trains.add_train(train)

    return trains
