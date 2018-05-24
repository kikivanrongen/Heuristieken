import csv
import classes.classes
from functions.random_trajectory_noreturns import random_trajectory_noreturns
import random

def dijkstra(data, max_t, max_min):
    """ Dijkstra algorithm """

    # alle kritieke verbindingen berijden en dan opsplitsen in trajecten door min !!!!!!
    # beginnen met crit stations? of een station met een crit verbinding?
    # create Trains object
    trains = classes.classes.Trains(data)

    past_critical_connections = []
    remaining_crit_stations = data.self.stations_with_critical_connection

    while data.critical_connections != past_critical_connections:
        min = 0

        # create Train object
        train = classes.classes.Train(start, data)

        # start and end critical stations but randomly chosen
        start = random.choice(remaining_crit_stations)
        end = random.choice(remaining_crit_stations)
        while start == end:
            end = random.choice(remaining_crit_stations)

        train = classes.classes.Train(start, data)
        previous = []
        last_station = start
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

            # choose an critical connection unless there are none



            # sort the tuple list and pick station with shortest time
            time = sorted(possible, key=lambda times: times[1])
            shortest_time = time[0]
            next = shortest_time[0]

            # if critical add critical connection in list
            connection = [last_station, next]
            if connection in data.critical_connections:
                past_critical_connections.append(connection)
                list(set(past_critical_connections))

            # if next station is end station return train
            if next == end:
                break

            train.update_trajectory(next)
            min = train.time_elapsed

            # update previous location
            previous.append(train.location)

            # remove from remaining critical stations list
            if next in remaining_crit_stations:
                remaining_crit_stations.remove(next)

        # add train to trains object
        trains.add_train(train)

    return trains
