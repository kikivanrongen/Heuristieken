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

# print("Which area would you like to ride? (Nederland / NZHolland)")

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# calculate score for random and cornerstart
random = []
corner = []
random_noreturn = []
corner_noreturn = []
hill_climber = []
greedy_alg = []

for i in range(10000):
    random.append(firstsol(NZ_Holland).score())
    corner.append(cornerstart(NZ_Holland).score())
    random_noreturn.append(firstsol_noreturn(NZ_Holland).score())
    corner_noreturn.append(cornerstart_noreturn(NZ_Holland).score())
    # hill_climber.append(hillclimber(NZ_Holland).score())
    # greedy_alg.append(greedy(NZ_Holland).score())

mean_random = sum(random)/len(random)
mean_corner = sum(corner)/len(corner)
mean_random_noreturn = sum(random_noreturn)/len(random_noreturn)
mean_corner_noreturn = sum(corner_noreturn)/len(corner_noreturn)
mean_hillclimber = sum(hill_climber)/len(hill_climber)
mean_greedy = sum(greedy_alg)/len(greedy_alg)


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
