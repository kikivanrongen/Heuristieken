import classes.classes
import random
from algorithms.firstsol import firstsol
from algorithms.cornerstart_noreturn import cornerstart_noreturn
from functions.random_trajectory import random_trajectory
from functions.random_trajectory_noreturns import random_trajectory_noreturns

def hillclimber(data):
    """ Hill Climber iterative algortihm. Replaces one trajectory and checks score. """

    # start with a possible solution
    solution = cornerstart_noreturn(data)
    start_solution = solution

    # calculate score
    old_score = start_solution.score()
    max_loop = 1000
    index = 0

    for element in start_solution.trains:

        start = element.past_stations[0]

        for i in range(max_loop):

            # change one train in the solution
            new_train = random_trajectory_noreturns(start, data)
            start_solution.trains[index] = new_train
            temporary_score = start_solution.score()

            if temporary_score > old_score:
                solution.trains[index] = new_train
                new_score = temporary_score

        # update index
        index += 1

    return solution
