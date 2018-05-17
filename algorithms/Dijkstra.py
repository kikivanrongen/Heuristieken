import csv
import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def dijkstra(data):

    min = 0
    max_min = 120
    start = random.choice(data.names)
    train = classes.classes.Train(start, data)

    # while loop for constrains
    while min < max_min:

        # possible connections from last station
        possible = data.connection_and_time[train.location]

        # touple van de lijst possible maken in de classe
        time = sorted(possible, key=lambda times: times[1])
        print(time)

        # # make dict of time and connection
        # my_dict = {item : possible[index+1] for index, item in enumerate(a) if index % 2 == 0}
        # my_dict = {}
        # for index, item in enumerate(a):
        #     if index % 2 == 0:
        #         my_dict[item] = a[index+1]

        print(my_dict)
        # pick shortest connection from possible connections
        next =

        train.update_trajectory(next)
        min = train.time_elapsed

        # update previous location
        previous = train.location

    return train
