import classes.classes
import random
import copy

def greedy(data, max_t, max_min):
    """ Greedy iterative algorithm. This algorithm starts at a random station
    and checks the scores of every possible next station. After checking every
    score of every possible connection, the algorithm chooses the station
    with the highest score. """

    # create Trains object and copy
    trains = classes.classes.Trains(data)
    copy_trains = classes.classes.Trains(data)

    # create list of start stations
    # start_stations = copy.deepcopy(data.names)

    # for amount of minutes
    for t in range(max_t):

        # set minutes
        minutes = 0
        previous = []

        # determine start position and remove element from start stations list
        start = random.choice(data.names)
        # start_stations.remove(start)

        # store previous stations
        previous.append(start)

        # create Train object and copy
        train = classes.classes.Train(start, data)
        copy_train = classes.classes.Train(start, data)

        while minutes < max_min:

            new_scores = {}

            # find possible connections
            possible = data.connections[train.location]

            # check for corner station
            if len(possible) != 1:

                # remove previous stations from possibilities
                for prev in previous:
                    if prev in possible:
                        possible.remove(prev)

            # if no connections are possible, stop train
            if not possible:
                break

            # iterate over connections
            for element in possible:

                # calculate score for new trajectory
                copy_train.update_trajectory(element)
                copy_trains.add_train(copy_train)
                new_scores[element] = copy_trains.score()

                # reset train and trains
                copy_train = copy.deepcopy(train)
                copy_trains = copy.deepcopy(trains)

            # find best score in list
            best_score = max(new_scores.values())

            # determine corresponding go to location
            for location, score in new_scores.items():
                if score == best_score:
                    best_option = location

            # update previous location list
            previous.append(train.location)

            # update train
            train.update_trajectory(best_option)
            copy_train = copy.deepcopy(train)

            # update elapsed time
            minutes += train.time_elapsed

        # add train to trains object, copy and remove start station from list
        trains.add_train(train)
        copy_trains = copy.deepcopy(trains)

    return trains
