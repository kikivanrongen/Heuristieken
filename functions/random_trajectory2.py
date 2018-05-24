import classes.classes
import random
import copy

def random_trajectory2(start, data, max_min, returns):
    """ This funtion gives a random trajectory for one train. This trajectory
    depends on the start station, given in random_solution, the data, maximum
    amount of minutes en whether it is possible to return to the previous station,
    also given in random_solution. This function is called when a single
    trajectory is needed. """


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
