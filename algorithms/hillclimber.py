import csv
import classes.classes
import random
from algorithms.firstsol import firstsol

def hillclimber(data):
    """ Hill Climber iterative algortihm """

    start_solution = firstsol(data)

    change_trajectory(start_solution)


def change_trajectory(solution):

    # iterate over trains
    for t in trains:
        
