import classes.classes
import random
from functions.random_trajectory import random_trajectory

def random_solution(data, max_t, max_min, corner = None, returns = None):
    """ This function gives a random solution given the data, maximum amount of
    trains, maximum amount of minutes, whether to start in a corner or not and
    whether to return to the previous station or not. The stations are choosen
    with the builtin function random. In this function the function random_
    trajectory is called to determine one single trajectory. All these trajectories
    form the whole solution. """

    # initalize variables
    trains = classes.classes.Trains(data)
    connections = data.connections
    one_connection = []

    # for loop for 7 trains
    for t in range(max_t):

        # chooses wheater the start is a corner or random
        if corner == True:
            for key in connections:
                if len(connections[key]) == 1:
                    one_connection.append(key)
            start = random.choice(one_connection)

        else:
            start = random.choice(data.names)

        # make trajectory
        random_traj = random_trajectory(start, data, max_min, returns)

        # add train to trains
        trains.add_train(random_traj)

    return trains
