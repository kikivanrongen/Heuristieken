import classes.classes
import random

def greedy(data):
    """ Greedy iterative algorithm """

    # create Trains object and copy
    trains = classes.classes.Trains(data)
    copy_trains = classes.classes.Trains(data)

    # maximum minutes for trains
    min = 0
    max_min = 120
    max_t = 7

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
                copy_trains.add_train(train)
                new_scores[element] = copy_trains.score()

                # reset train
                copy_train = train

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
        trains.add_train(best_option)

    return trains
