import csv
import classes.classes
import random
from functions.score import score

def firstsol(data):
    """ First algorithm for a random solution. """

    # initalize variables
    t = 0
    max_t = 7
    max_min = 120
    random_stations = []
    amount_critical = 0
    trains = classes.classes.Trains(data)

    # for loop for 7 trains
    for t in range(max_t):
        min = 0
        start = random.choice(data.names)
        # print("START:")
        # print(start)
        train = classes.classes.Train(start, data)

        # while loop for constrains
        while min < max_min:

            # possible connections from last station
            possible = data.connections[train.location]

            # pick random possible connection from possible connections
            next = random.choice(possible)

            train.update_trajectory(next)

        # store train in class
        trains.add_train(train)

    # for element in trains:
    #
    #     print(element.past_stations)
    #     print(element.time_elapsed)
    #
    # print(amount_critical)


    # print("SCORE RANDOM")
    # print(s)
    return trains
