import csv
import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def dijkstra(data, max_t):
    """ Dijkstra algorithm """

    min = 0
    max_min = 120

    for t in range(max_t):

        trains = classes.classes.Trains(data)

        # start and end critical stations but randomly chosen
        start = random.choice(data.critical_stations)
        end = random.choice(data.critical_stations)
        while start == end:
            end = random.choice(data.critical_stations)

        train = classes.classes.Train(start, data)
        previous = []
        previous.append(start)

        # while loop for constrains
        while min < max_min:

            # possible connections from last station
            possible = data.connection_and_time[train.location]

            # make sure train does not go to previous stations
            for prev in previous:
                for pos in possible:
                    if pos[0] == prev:
                        possible.remove(pos)

            # sort the tuple list and pick station with shortest time
            time = sorted(possible, key=lambda times: times[1])
            shortest_time = time[0]
            next = shortest_time[0]

            # if next station is end station return train
            if next == end:
                return train

            train.update_trajectory(next)
            min = train.time_elapsed

            # update previous location
            previous.append(train.location)

    return trains
