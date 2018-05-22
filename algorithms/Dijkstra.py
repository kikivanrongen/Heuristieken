import csv
import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def dijkstra(data):
    """ Dijkstra algorithm """

    min = 0
    max_min = 120

    # start and end critical stations but randomly chosen
    start = random.choice(data.critical_stations)
    end = random.choice(data.critical_stations)
    while start == end:
        end = random.choice(data.critical_stations)

    train = classes.classes.Train(start, data)
    previous = []
    previous.append(start)

    print("!!!!!!!!BEGIN!!!!!!!!!!")

    # while loop for constrains
    while min < max_min:
        # mag geen previous hebben , check voor eind station anders door naar korte verbinding
        # possible connections from last station
        possible = data.connection_and_time[train.location]

        #print(possible)
        print(previous)
        print("\n")
        print(possible)
        print("\n")

        # make sure train does not go to previous station
        for prev in previous:
            for pos in possible:
                    if prev[0] == pos[0]:
                            possible.remove(prev)

        print(possible)
        print("--------")

        # sort the tuple list and pick station with shortest time
        time = sorted(possible, key=lambda times: times[1])
        shortest_time = time[0]
        next = shortest_time[0]

        # if next station is end station return train
        if next == end:
            return train.past_stations

        train.update_trajectory(next)
        min = train.time_elapsed

        # update previous location
        previous.append(train.location)

    return train.past_stations
