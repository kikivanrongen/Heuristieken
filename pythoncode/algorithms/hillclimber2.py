import __init__ as im

def hillclimber2(data, startfunction, trajectory, max_t, max_min, max_loop = 1000):
    """ Hill Climber iterative algortihm. Starts with a random solution with no
    returns. Thereafter it changes one trajectory a given number of times (in
    default 1000 times) and checks whether the score is higher or not. It
    chooses the trajectory with the highest score. This is done for every
    trajectory. All connections are critical
    """

    # start with a possible solution
    solution = startfunction(data, max_t, max_min, False, False)
    copy_solution = im.copy.deepcopy(solution)

    # calculate score
    current_score = copy_solution.score2()
    index = 0

    # iterate over trains in current solution
    for element in solution.trains:

        # determine new start station
        start = im.random.choice(data.names)

        # iterate new trajectories
        for i in range(max_loop):

            # change one train in the solution
            new_train = trajectory(start, data, max_min, False)
            copy_solution.trains[index] = new_train
            temporary_score = copy_solution.score2()

            # store new train if score is improved
            if temporary_score > current_score:
                solution.trains[index] = new_train
                current_score = temporary_score

            # set copy
            copy_solution = im.copy.deepcopy(solution)

        # update index
        index += 1

    return solution
