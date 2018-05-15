import csv
import random
import classes.classes
from algorithms.firstsol import firstsol
from algorithms.firstsol_noreturn import firstsol_noreturn
from algorithms.cornerstart import cornerstart
from algorithms.cornerstart_noreturn import cornerstart_noreturn

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
# random = []
# corner = []
# for i in range(10):
#     random.append(firstsol(NZ_Holland).score())
#     corner.append(cornerstart(NZ_Holland).score())
#     random_noreturn.append(firstsol_noreturn(NZ_Holland).score())
#     corner_noreturn.append(cornerstart_noreturn(NZ_Holland).score())
#
# mean_random = sum(random)/len(random)
# mean_corner = sum(corner)/len(corner)
# mean_random_noreturn = sum(random_noreturn)/len(random_noreturn)
# mean_corner_noreturn = sum(corner_noreturn)/len(corner_noreturn)
#
#
# print("FIRSTSOL:")
# print(mean_random)
# print("UITHOEKSOL:")
# print(mean_corner)
# print("FIRSTSOL NO RETURN:")
# print(mean_random_noreturn)
# print("UITHOEKSOL NO RETURN:")
# print(mean_corner_noreturn)
start = random.choice(NZ_Holland.names)
train = classes.classes.Train(start, NZ_Holland)
possible = NZ_Holland.connections[train.location]
#my_dict = {item : possible[index+1] for index, item in enumerate(possible) if index % 2 == 0}
my_dict = {}
for index, item in enumerate(possible):
    if index % 2 == 0:
        my_dict[item] = possible[index+1]

print(my_dict)
