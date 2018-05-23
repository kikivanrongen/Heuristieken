import classes.classes
import random

def random_trajectory_noreturns(start, data, max_min):

    minutes = 0
    train = classes.classes.Train(start, data)
    previous = start

    # while loop for constrains
    while minutes < max_min:

        # possible connections from last station
        possible = data.connections[train.location]

        # make sure train does not go to previous station
        if previous in possible:
            possible.remove(previous)

        # pick random possible connection from possible connections
        next = random.choice(possible)

        train.update_trajectory(next)
        minutes = train.time_elapsed

        # update previous location
        previous = train.location

    return train
