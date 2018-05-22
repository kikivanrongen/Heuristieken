import classes.classes
import random
from functions.random_trajectory import random_trajectory

def cornerstart(data, max_t, max_min):
    """ First algorithm for a random solution. """

    # initalize variables
    connections = data.connections
    one_connection = []
    trains = classes.classes.Trains(data)

    # for loop for 7 trains
    for t in range(max_t):

        # loop through dictionary to find one connection
        for key in connections:
            if len(connections[key]) == 1:
                one_connection.append(key)

        # determine start position
        start = random.choice(one_connection)

        # find random trajectory
        train = random_trajectory(start, data, max_min)

        # store train in class
        trains.add_train(train)

    return trains
