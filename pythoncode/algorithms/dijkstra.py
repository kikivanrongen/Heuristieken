import __init__ as im

def dijkstra(data, max_t, max_min):
    """ The Dijkstra algorithm finds the shortest path between the stations. The
    algorithm's start and end is randomly chosen of a list of stations with at
    least one critical connection. From the possible connections, it chooses the
    shortest time of the possible critical connections. When there are no critical
    connections it chooses the shortest time of the other possible connections.
    A trajectory cannot return to one of the ridden stations. The algorithm keeps
    track of the ridden critical connections and stops when all have been ridden
    or when the maximum trajectories are used.
    """

    # create Trains object
    trains = im.pythoncode.classes.classes.Trains(data)
    t = 0

    # create list of past critical connections and the remaining stations
    past_critical_connections = []
    remaining_crit_stations = data.stations_with_critical_connection

    # continue untill all critical connections are covered
    while len(data.critical_connections) != len(past_critical_connections):

        # if the max number of trains is reached, break
        if t == max_t:
            break

        # set minutes to 0
        minutes = 0

        # start and end critical stations, randomly chosen
        start = im.random.choice(remaining_crit_stations)
        end = im.random.choice(remaining_crit_stations)

        # start and end station cannot be the same
        while start == end:
            end = im.random.choice(remaining_crit_stations)

        # create Train object
        train = im.pythoncode.classes.classes.Train(start, data)

        # create list of previous stations and store last station
        previous = []
        last_station = start

        # append start position
        previous.append(start)

        # continue untill maximum minutes is reached
        while minutes < max_min:

            # retrieve possible connections from last station
            possible = im.copy.deepcopy(data.connection_and_time[train.location])
            possible_critical = []

            # make sure train does not go to previous stations
            for prev in previous:
                for pos in possible:
                    if pos[0] == prev:
                        possible.remove(pos)

            # break if there are no possible stations left
            if not possible:
                break

            # make list of the critical possible connections
            for pos in possible:
                if  (last_station, pos[0]) in data.critical_connections or (pos[0], last_station) in data.critical_connections:
                    possible_critical.append(pos)

            # choose shortest time of critical connections if possible
            if not possible_critical:
                time = sorted(possible, key=lambda times: times[1])
                shortest_time = time[0]
                next = shortest_time[0]

            # otherwise choose from possible connections
            else:
                time = sorted(possible_critical, key=lambda times: times[1])
                shortest_time = time[0]
                next = shortest_time[0]

            # if critical, add critical connection to list
            connection = (last_station, next)
            connection_turned = (next, last_station)
            if connection in data.critical_connections:
                past_critical_connections.append(connection)

            # add reversed connection
            if connection_turned in data.critical_connections:
                past_critical_connections.append(connection_turned)

            # remove duplicates
            past_critical_connections = list(set(past_critical_connections))

            # if next station is end station return train
            if next == end:
                break

            # update last station
            last_station = train.location

            # update previous location
            previous.append(train.location)

            # update train properties and minutes
            train.update_trajectory(next)
            minutes = train.time_elapsed

            # remove from remaining critical stations list
            if next in remaining_crit_stations:
                remaining_crit_stations.remove(next)

        # add train to trains object
        trains.add_train(train)

        # update number of trains
        t += 1

    return trains
