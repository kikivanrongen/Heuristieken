
import classes.classes
import random

def random_trajectory2(start, data, max_min, returns):
    """ This funtion gives a random trajectory for one train. This trajectory
    depends on the start station, given in random_solution, the data, maximum
    amount of minutes en whether it is possible to return to the previous station,
    also given in random_solution. This function is called when a single
    trajectory is needed. """


    minutes = 0
    train = classes.classes.Train(start, data)
    previous = start
    print("NEW TRAIN")
    # while loop for constrains
    while minutes < max_min:

        # possible connections from last station
        possible = data.connections[train.location]

        print(train.location)

        # remove previous from possible
        if returns == False:
            if previous in possible:
                print("IK BEN HIER")
                possible.remove(previous)
            if not possible:
                break

        print(possible)

        # pick random possible connection from possible connections
        next = random.choice(possible)
        previous = train.location
        print(next)

        train.update_trajectory(next)
        minutes = train.time_elapsed

    return train
