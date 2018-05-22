import classes.classes
import random
from functions.random_trajectory_noreturns import random_trajectory_noreturns

def cornerstart_noreturn(data, max_t):
    """ First algorithm for a random solution. No returns possible. """

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

        start = random.choice(one_connection)
        train = classes.classes.Train(start, data)

        train = random_trajectory_noreturns(start, data)

        # store train in class
        trains.add_train(train)

    return trains
