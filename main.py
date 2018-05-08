import csv
import classes.classes
from algorithms.firstsol import firstsol

from algorithms.cornerstart import cornerstart

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

random = []
corner = []
for i in range(10000):
    random.append(firstsol(NZ_Holland).score())
    corner.append(cornerstart(NZ_Holland).score())

mean_random = sum(random)/len(random)
mean_corner = sum(corner)/len(corner)


print("FIRSTSOL:")
print(mean_random)
print("UITHOEKSOL:")
print(mean_corner)
