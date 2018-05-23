import csv
import random
import classes.classes
# import algorithms as alg
from algorithms.firstsol import firstsol
from algorithms.firstsol_noreturn import firstsol_noreturn
from algorithms.cornerstart import cornerstart
from algorithms.cornerstart_noreturn import cornerstart_noreturn
from algorithms.hillclimber import hillclimber
from algorithms.greedy import greedy
from visualisation.visual import visual
from visualisation.visual import visual_solution

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# load data the Nederlands
Nederland = classes.classes.Stations()
Nederland.stations("data/StationsNationaal.csv")
Nederland.railroads("data/ConnectiesNationaal.csv")

# visualisation of possible trajectory
visual(NZ_Holland, "Visualisatie NZ Holland")
visual(Nederland, "Visualisatie Nederland")

max_t_n = 20
max_t_nz = 7
max_min_n = 180
max_min_nz = 120

# calculate score for random and cornerstart
random = []
corner = []
random_noreturn = []
corner_noreturn = []
hill_climber = []
greedy_alg = []

for i in range(1000):
    random.append(firstsol(NZ_Holland, max_t_nz, max_min_nz).score())
    corner.append(cornerstart(NZ_Holland, max_t_nz, max_min_nz).score())
    random_noreturn.append(firstsol_noreturn(NZ_Holland, max_t_nz, max_min_nz).score())
    corner_noreturn.append(cornerstart_noreturn(NZ_Holland, max_t_nz, max_min_nz).score())
    hill_climber.append(hillclimber(NZ_Holland, firstsol, random_trajectory_noreturns, max_t_nz, max_min_nz).score())
    greedy_alg.append(greedy(NZ_Holland, max_t_nz, max_min_nz).score())

mean_random = sum(random)/len(random)
mean_corner = sum(corner)/len(corner)
mean_random_noreturn = sum(random_noreturn)/len(random_noreturn)
mean_corner_noreturn = sum(corner_noreturn)/len(corner_noreturn)
mean_hillclimber = sum(hill_climber)/len(hill_climber)
mean_greedy = sum(greedy_alg)/len(greedy_alg)

lijst = [mean_random, mean_random_noreturn, mean_corner, mean_corner_noreturn]
print(lijst)


print("FIRSTSOL:")
print(mean_random)
print("UITHOEKSOL:")
print(mean_corner)
print("FIRSTSOL NO RETURN:")
print(mean_random_noreturn)
print("UITHOEKSOL NO RETURN:")
print(mean_corner_noreturn)
print("HILLCLIMBER")
print(mean_hillclimber)
print("GREEDY")
print(mean_greedy)
print(max(greedy_alg))

visual_solution(NZ_Holland, firstsol_noreturn(NZ_Holland, max_t_nz))

###################################################################
########## HOLLAND

n_random = []
n_corner = []
n_random_noreturn = []
n_corner_noreturn = []
n_hill_climber = []
n_greedy_alg = []

for i in range(1000):
    n_random.append(firstsol(Nederland, max_t_n, max_min_n).score())
    n_corner.append(cornerstart(Nederland, max_t_n, max_min_n).score())
    n_random_noreturn.append(firstsol_noreturn(Nederland, max_t_n, max_min_n).score())
    n_corner_noreturn.append(cornerstart_noreturn(Nederland, max_t_n, max_min_n).score())
    n_hill_climber.append(hillclimber(Nederland, firstsol, random_trajectory_noreturns, max_t_n, max_min_n).score())
    n_greedy_alg.append(greedy(Nederland, max_t_n, max_min_n).score())

mean_n_random = sum(n_random)/len(n_random)
mean_n_corner = sum(n_corner)/len(n_corner)
mean_n_random_noreturn = sum(n_random_noreturn)/len(n_random_noreturn)
mean_n_corner_noreturn = sum(n_corner_noreturn)/len(n_corner_noreturn)
mean_n_hillclimber = sum(n_hill_climber)/len(n_hill_climber)
mean_n_greedy = sum(n_greedy_alg)/len(n_greedy_alg)

lijst = [mean_n_random, mean_n_random_noreturn, mean_n_corner, mean_n_corner_noreturn]
print(lijst)


print("FIRSTSOL:")
print(mean_n_random)
print(max(n_random))
print("UITHOEKSOL:")
print(mean_n_corner)
print(max(n_corner))
print("FIRSTSOL NO RETURN:")
print(mean_n_random_noreturn)
print(max(n_random_noreturn))
print("UITHOEKSOL NO RETURN:")
print(mean_n_corner_noreturn)
print(max(n_corner_noreturn))
print("HILLCLIMBER")
print(mean_n_hillclimber)
print(max(n_hill_climber))
print("GREEDY")
print(mean_n_greedy)
print(max(n_greedy_alg))

visual_solution(Nederland, firstsol_noreturn(Nederland, max_t_n, max_min_n))
