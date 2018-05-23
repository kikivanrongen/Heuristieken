import classes.classes
import random

def random_trajectory(start, data, max_min):

    minutes = 0
    train = classes.classes.Train(start, data)

    # while loop for constrains
    while minutes < max_min:

        # possible connections from last station
        possible = data.connections[train.location]

        # pick random possible connection from possible connections
        next = random.choice(possible)

        train.update_trajectory(next)
        minutes = train.time_elapsed

    return train
