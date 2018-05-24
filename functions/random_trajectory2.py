import classes.classes
import random
import copy

def random_trajectory2(start, data, max_min, returns):

    # set variables and
    minutes = 0
    train = classes.classes.Train(start, data)
    previous = start

    # while loop for constrains
    while minutes < max_min:

        # possible connections from last station
        possible = copy.deepcopy(data.connections[train.location])

        # remove previous from possible
        if returns == False:
            if previous in possible:
                possible.remove(previous)

            if not possible:
                break

        # pick random possible connection from possible connections
        next = random.choice(possible)

        # update previous location
        previous = train.location

        # update train trajectory and elapsed time
        train.update_trajectory(next)
        minutes = train.time_elapsed

    return train
