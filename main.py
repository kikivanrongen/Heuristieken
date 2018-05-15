import csv
import random
import classes.classes
from algorithms.firstsol import firstsol
from algorithms.firstsol_noreturn import firstsol_noreturn
from algorithms.cornerstart import cornerstart
from algorithms.cornerstart_noreturn import cornerstart_noreturn
from algorithms.hillclimber import hillclimber

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# calculate score for random and cornetstart
random = []
corner = []
random_noreturn = []
corner_noreturn = []
for i in range(10):
    random.append(firstsol(NZ_Holland).score())
    corner.append(cornerstart(NZ_Holland).score())
    random_noreturn.append(firstsol_noreturn(NZ_Holland).score())
    corner_noreturn.append(cornerstart_noreturn(NZ_Holland).score())

mean_random = sum(random)/len(random)
mean_corner = sum(corner)/len(corner)
mean_random_noreturn = sum(random_noreturn)/len(random_noreturn)
mean_corner_noreturn = sum(corner_noreturn)/len(corner_noreturn)


print("FIRSTSOL:")
print(mean_random)
print("UITHOEKSOL:")
print(mean_corner)
print("FIRSTSOL NO RETURN:")
print(mean_random_noreturn)
print("UITHOEKSOL NO RETURN:")
print(mean_corner_noreturn)

# hill climber algorithm
hillclimber1 = hillclimber(NZ_Holland)

print("HILLCLIMBER:")

print(hillclimber1.score())
