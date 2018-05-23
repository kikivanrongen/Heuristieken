import classes.classes
import random
import copy

def greedy(data, max_t, max_min):
    """ Greedy iterative algorithm """

    # create Trains object and copy
    trains = classes.classes.Trains(data)
    copy_trains = classes.classes.Trains(data)

    for t in range(max_t):

        # set minutes
        minutes = 0

        # determine start position (geen uithoek!)
        start = random.choice(data.names)

        # store previous stations
        previous = []
        previous.append(start)

        # create Train object and copy
        train = classes.classes.Train(start, data)
        copy_train = classes.classes.Train(start, data)

        # determine start start score
        previous_score = trains.score()

        while minutes < max_min:

            new_scores = {}

            # find possible connections
            possible = data.connections[train.location]

            # check for corner station
            if len(possible) != 1:

                # make sure train does not go to previous station
                for prev in previous:
                    if prev in possible:
                        possible.remove(prev)

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

            # go to new location if score is improved
            if best_score > 0.90 * previous_score:

                # determine corresponding go to location
                for location, score in new_scores.items():
                    if score == best_score:
                        best_option = location

                # update train
                train.update_trajectory(best_option)
                copy_train = copy.deepcopy(train)

                # update elapsed time
                minutes += train.time_elapsed

                # update previous location and previous score
                previous.append(train.location)
                previous_score = best_score

            else:
                # stop train
                minutes = 120

        # add train to trains object
        trains.add_train(train)
        copy_trains = copy.deepcopy(trains)

    return trains
