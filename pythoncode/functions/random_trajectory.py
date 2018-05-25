import __init__ as im

def random_trajectory(start, data, max_min, returns):
    """ This funtion gives a random trajectory for one train. This trajectory
    depends on the start station, given in random_solution, the data, maximum
    amount of minutes en whether it is possible to return to the previous station,
    also given in random_solution. This function is called when a single
    trajectory is needed.
    """

    # set variables and make train object
    minutes = 0
    train = im.pythoncode.classes.classes.Train(start, data)
    previous = start

    # while loop for when maximum minutes is reached
    while minutes < max_min:

        # possible connections from last station
        possible = im.copy.deepcopy(data.connections[train.location])

        # remove previous from possible if no return is input 
        if returns == False:
            if previous in possible:
                possible.remove(previous)

            if not possible:
                break

        # pick random possible connection from possible connections
        next = im.random.choice(possible)

        # update previous location
        previous = train.location

        # update train trajectory and elapsed time
        train.update_trajectory(next)
        minutes = train.time_elapsed

    return train
