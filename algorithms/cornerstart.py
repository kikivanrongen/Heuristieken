import csv
import classes.classes
import random
from functions.score import score

def cornerstart(data):
    """ First algorithm for a random solution. """

    # initalize variables
    t = 0
    max_t = 7
    max_min = 120
    dict = data.connections
    random_stations = []
    one_connection = []
    amount_critical = 0
    trains = classes.classes.Trains(data)

    # for loop for 7 trains
    for t in range(max_t):
        min = 0

        # loop through dictionary to find one connection
        for key in dict:
            if len(dict[key]) == 1:
                one_connection.append(key)

        start = random.choice(one_connection)
        train = classes.classes.Train(start, data)
        previous = start

        # while loop for constrains
        while min < max_min:

            # possible connections from last station
            possible = data.connections[train.location]

            # make sure train does not go to previous station
            if previous in possible:    
                possible.remove(previous)

            # pick random possible connection from possible connections
            next = random.choice(possible)

            train.update_trajectory(next)
            min = train.time_elapsed

            previous = train.location

        # store train in class
        trains.add_train(train)

    return trains
