import __init__ as im

def random_solution(data, max_t, max_min, corner = None, returns = None):
<<<<<<< HEAD
    """ This function gives a random solution given the data, maximum amount of
    trains, maximum amount of minutes, whether to start in a corner or not and
    whether to return to the previous station or not. The stations are choosen
    with the builtin function random. In this function the function random_
    trajectory is called to determine one single trajectory. All these trajectories
    form the whole solution.
=======
    """ This function returns a random solution given the data, maximum amount of
    trains, maximum amount of minutes, start in a corner station or not and
    allowance of return to previous station. The stations are chosen with the
    built-in function random. In this function the function random_trajectory is
    called to determine one single trajectory. All these trajectories together
    form the entire solution.
>>>>>>> eb94c9b982038815c654ebedf80149c5ca51060f
    """

    # initalize variables
    trains = im.pythoncode.classes.classes.Trains(data)
    connections = data.connections
    one_connection = []

    # iterate over trains
    for t in range(max_t):

        # determine start station in corner if asked
        if corner == True:
            for key in connections:
                if len(connections[key]) == 1:
                    one_connection.append(key)
            start = im.random.choice(one_connection)

        # choose random start station otherwise
        else:
            start = im.random.choice(data.names)

        # create trajectory
        random_traj = im.random_trajectory(start, data, max_min, returns)

        # add trajectory to trains
        trains.add_train(random_traj)

    return trains
