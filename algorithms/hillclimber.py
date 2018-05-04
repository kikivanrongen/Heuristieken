# import score function
# from functions import score

import csv
import classes.classes
import random

def hillclimber(data):
    """ Hill Climber iterative algorithm """

    max_trains = 7
    min_max = 120
    trains = 0

    while trains < max_trains:
        min = 0
        begin_score = 0
        trains += 1
        start = random.choice(data.names)
        train = classes.classes.Train(start, data)
        name_last = "None"

        while min < min_max:

            count = 0
            score = score(train.number_critical, trains, train.time_elapsed)
            score_new = score

            while score_new <= score:

                count += 1

                # possible connections from last station
                possible = data.connections[train.location]

                # pick random possible connection from possible connections
                next = random.choice(possible)

                # go to new location
                train.possible_trajectory(next)

                # calculate score
                score_new = score(train.number_critical, trains, train.time_elapsed)

                # if trajectory cannot be improved, break out if while loop
                if count > 4:
                    break

            # break if there is no new/better score and start new train
            if next == start or next == name_last :
                break

            # if no break update name for next check
            name_last = next

            # update location of train
            train.update_trajectory(next)

            # update elapsed time
            min += train.time_elapsed
