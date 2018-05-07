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
    trains = []
    one_connection = []
    amount_critical = 0
    # for loop for 7 trains
    for t in range(max_t):
        min = 0

        # loop through dictionary to find one connection
        for key in dict:
            if len(dict[key]) == 1:
                one_connection.append(key)

        start = random.choice(one_connection)
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
            min += train.time_elapsed

        amount_critical += train.number_critical

        # store train in list
        trains.append(train)

    # for element in trains:
    #
    #     print(element.past_stations)
    #     print(element.time_elapsed)
    #
    # print(amount_critical)

    s = score(amount_critical, t, min)
    # print("SCORE UITHOEK")
    # print(s)

    return s
