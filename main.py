import csv
import classes.classes
from algorithms.firstsol import firstsol

from algorithms.cornerstart import cornerstart

# import data
# station_list = loading.load.stations("data/StationsHolland.csv")
# connection_list = loading.load.railroads("data/ConnectiesHolland.csv")

# put data in classes
# for element in station_list:
#     element[0] = classes.classes.Station(name=element[0], x=element[1],
#     y=element[2], critical = element[3])
    # classes.classes.Station(element)

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

# calculate score for random and cornetstart
random = []
corner = []
for i in range(10):
    random.append(firstsol(NZ_Holland).score())
    corner.append(cornerstart(NZ_Holland).score())

mean_random = sum(random)/len(random)
mean_corner = sum(corner)/len(corner)


print("FIRSTSOL:")
print(mean_random)
print("UITHOEKSOL:")
print(mean_corner)
