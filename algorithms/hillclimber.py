import classes.classes
import random
import copy
from algorithms.firstsol import firstsol
from algorithms.cornerstart_noreturn import cornerstart_noreturn
from algorithms.cornerstart import cornerstart
from functions.random_trajectory import random_trajectory
from functions.random_trajectory_noreturns import random_trajectory_noreturns

def hillclimber(data, startfunction, trajectory, max_t, max_min):
    """ Hill Climber iterative algortihm. Replaces one trajectory and checks score. """

    # start with a possible solution
    solution = startfunction(data, max_t, max_min)
    copy_solution = copy.deepcopy(solution)

    # calculate score
    current_score = copy_solution.score()
    max_loop = 1000
    index = 0

    # iterate over trains in current solution
    for element in solution.trains:

        # determine new start station
        start = random.choice(data.names)

        # iterate new trajectories
        for i in range(max_loop):

            # change one train in the solution
            new_train = trajectory(start, data, max_min)
            copy_solution.trains[index] = new_train
            temporary_score = copy_solution.score()

            # store new train if score is improved
            if temporary_score > current_score:
                solution.trains[index] = new_train

                current_score = temporary_score

            # set copy
            copy_solution = copy.deepcopy(solution)

        # update index
        index += 1

    return solution
