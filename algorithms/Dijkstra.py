import csv
import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def dijkstra(data):
    """ Dijkstra algorithm """

    min = 0
    max_min = 120
    start = random.choice(data.names)
    train = classes.classes.Train(start, data)

    # while loop for constrains
    while min < max_min:

        # possible connections from last station
        possible = data.connection_and_time[train.location]

        # sort the tuple list
        time = sorted(possible, key=lambda times: times[1])
        shortest_time = time[0]
        print(shortest_time)
        # pick shortest connection from possible connections
        next =

        train.update_trajectory(next)
        min = train.time_elapsed

        # update previous location
        previous = train.location

    return train
