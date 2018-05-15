import classes.classes
import random

def random_trajectory_noreturns(start, data):

    min = 0
    max_min = 120
    train = classes.classes.Train(start, data)
    previous = start

    # while loop for constrains
    while min < max_min:

        # possible connections from last station
        possible = data.connections[train.location]

        # make sure train does not go to previous station
        if previous in possible:
            possible.remove(previous)

        # pick random possible connection from possible connections
        next = random.choice(possible)

        train.update_trajectory(next)
        min = train.time_elapsed

        # update previous location
        previous = train.location

    return train
