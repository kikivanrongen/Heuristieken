import classes.classes
from functions.random_trajectory import random_trajectory
import random

def firstsol(data, max_t, max_min):
    """ First algorithm for a random solution. It starts with a random startpoint,
    and chooses a random connection of the possible connections. This is done
    until the train reaches the maximum amount of minutes and the maximum amount
    of trains. """

    # initalize variables
    trains = classes.classes.Trains(data)

    # for loop for 7 trains
    for t in range(max_t):

        start = random.choice(data.names)

        # find random trajectory
        train = random_trajectory(start, data, max_min)

        # store train in class
        trains.add_train(train)

    return trains
