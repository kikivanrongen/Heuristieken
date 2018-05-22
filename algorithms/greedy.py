import classes.classes
import random
import copy

def greedy(data, max_t, max_min):
    """ Greedy iterative algorithm """

    # create Trains object and copy
    trains = classes.classes.Trains(data)
    copy_trains = classes.classes.Trains(data)

    # set minutes
    min = 0

    for t in range(max_t):

        # determine start position (geen uithoek!)
        start = random.choice(data.names)

        # create Train object and copy
        train = classes.classes.Train(start, data)
        copy_train = classes.classes.Train(start, data)

        while min < max_min:

            new_scores = {}

            # find possible connections
            possible = data.connections[train.location]

            # iterate over connections
            for element in possible:

                # calculate score for new trajectory
                copy_train.update_trajectory(element)
                copy_trains.add_train(copy_train)
                new_scores[element] = copy_trains.score()

                # reset train and trains
                copy_train = train
                copy_trains = trains

            # find best score in list
            best_score = max(new_scores.values())

            # determine corresponding go to location
            for location, score in new_scores.items():
                if score == best_score:
                    best_option = location

            # update train
            train.update_trajectory(best_option)
            min += train.time_elapsed

        # add train to trains object
        trains.add_train(train)

    return trains
