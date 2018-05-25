import __init__ as im

def greedy(data, max_t, max_min):
    """ Greedy iterative algorithm. This algorithm starts at a random station
    and checks the scores of every possible next station. After checking every
    score of every possible connection, the algorithm chooses the station
    with the highest score. """

    # create Trains object and copy
    trains = im.pythoncode.classes.classes.Trains(data)
    copy_trains = im.pythoncode.classes.classes.Trains(data)

    # iterate over number of trains
    for t in range(max_t):

        # set minutes
        minutes = 0
        previous = []

        # determine start position
        start = im.random.choice(data.names)

        # store previous stations
        previous.append(start)

        # create Train object and copy
        train = im.pythoncode.classes.classes.Train(start, data)
        copy_train = im.pythoncode.classes.classes.Train(start, data)

        # continue untill maximum minutes is reached
        while minutes < max_min:

            new_scores = {}

            # find possible connections
            possible = im.copy.deepcopy(data.connections[train.location])

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

                # calculate score for new trajectory and append to dictionary
                copy_train.update_trajectory(element)
                copy_trains.add_train(copy_train)
                new_scores[element] = copy_trains.score()

                # reset train and trains
                copy_train = im.copy.deepcopy(train)
                copy_trains = im.copy.deepcopy(trains)

            # find best score in list
            best_score = max(new_scores.values())

            # determine corresponding go-to location
            for location, score in new_scores.items():
                if score == best_score:
                    best_option = location

            # update previous location list
            previous.append(train.location)

            # update train and copy
            train.update_trajectory(best_option)
            copy_train = im.copy.deepcopy(train)

            # update elapsed time
            minutes += train.time_elapsed

        # add train to trains object and copy
        trains.add_train(train)
        copy_trains = im.copy.deepcopy(trains)

    return trains
