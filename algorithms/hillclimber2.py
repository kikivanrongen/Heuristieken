import classes.classes
import random
from algorithms.firstsol import firstsol
from algorithms.cornerstart_noreturn import cornerstart_noreturn
from algorithms.cornerstart import cornerstart
from functions.random_trajectory import random_trajectory
from functions.random_trajectory_noreturns import random_trajectory_noreturns

def hillclimber(data, startfunction, trajectory, max_t, max_min):
    """ Hill Climber iterative algortihm. Replaces one trajectory and checks score. """

    # start with a possible solution
    solution = startfunction(data, max_t, max_min)
    start_solution = solution

    # calculate score
    old_score = start_solution.score()
    max_loop = 100000
    index = 0

    for element in start_solution.trains:

        start = element.past_stations[0]

        for i in range(max_loop):

            # change multiple trains in the solution depending on the score
            new_train = trajectory(start, data, max_min)
            start_solution.trains[index] = new_train
            temporary_score = start_solution.score()

            if temporary_score > old_score:
                solution.trains[index] = new_train
                new_score = temporary_score
                old_score = new_score

        # update index
        index += 1

    return solution
