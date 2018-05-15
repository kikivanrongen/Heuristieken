import csv
import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def dijkstra(data):

    min = 0
    max_min = 120
    train = classes.classes.Train(start, data)
    start = random.choice(data.names)
    previous =

    # while loop for constrains
    while min < max_min:

        # possible connections from last station
        possible = data.connections[train.location]

        # make sure train does not go to previous station
        if previous in possible:
            possible.remove(previous)

        # make list of time to get the shortest
        time = []
        for i in possible:
            time.append(i + 1)

        sort(time)
        shortest_time = time[0]

        # make dict of time and connection
        my_dict = {item : possible[index+1] for index, item in enumerate(a) if index % 2 == 0}
        my_dict = {}
        for index, item in enumerate(a):
            if index % 2 == 0:
                my_dict[item] = a[index+1]

        print(my_dict)
        # pick shortest connection from possible connections
        next =

        train.update_trajectory(next)
        min = train.time_elapsed

        # update previous location
        previous = train.location

    return train
