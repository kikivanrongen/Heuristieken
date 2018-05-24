import classes.classes
import random
from functions.random_trajectory2 import random_trajectory2

def random_solution2(data, max_t, max_min, corner = None, returns = None):

    # initalize variables
    trains = classes.classes.Trains(data)
    connections = data.connections
    one_connection = []

    # for loop for 7 trains
    for t in range(max_t):

        # chooses wheater the start is a corner or random
        if corner == True:
            for key in connections:
                if len(connections[key]) == 1:
                    one_connection.append(key)
            start = random.choice(one_connection)

        else:
            start = random.choice(connections)

        # make trajectory
        train = random_trajectory2(start, data, max_min, returns)

        # add train to trains
        trains.add_train(train)

    return trains
