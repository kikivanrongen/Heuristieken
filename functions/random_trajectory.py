import classes.classes
import random

def random_trajectory(start, data):

    min = 0
    max_min = 120
    train = classes.classes.Train(start, data)

    # while loop for constrains
    while min < max_min:

        # possible connections from last station
        possible = data.connections[train.location]

        # pick random possible connection from possible connections
        next = random.choice(possible)

        train.update_trajectory(next)
        min = train.time_elapsed

    return train