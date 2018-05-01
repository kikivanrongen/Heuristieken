import csv
import classes.classes

import random

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
NZ_Holland.railroads("data/ConnectiesHolland.csv")

stations = NZ_Holland.names

# je stopt beginpunt in de subclass train
t = 0
max_t = 7

random_stations = []
min = 0
max_min = 120

# train = classes.classes.Train()
#
# while t < max_t:
#     start = random.choice(stations)
#     print(start)
#     t += 1
#     print(random_stations)
#     min = 0

trains = []
for t in range(max_t):
    min = 0
    start = random.choice(stations)
    train = classes.classes.Train(start)

    while min < max_min:

        #begint punt en connecties halen random kiezen en in train gooien
        # Dit moet nog worden gereturned van de train

        print(min)
        print("huidige locatie:")
        print(train.location)

        possible = NZ_Holland.connections[train.location]
        name = []
        for s,z in zip(possible[0:2], possible[1:2]):
            name.append(s)

        print("opties:")
        print(name)
        next = random.choice(name)

        train.update_trajectory(next)
        min += train.time_elapsed

    # store train in list
    trains.append(train)

for element in trains:

    print(element.past_stations)
    print(element.time_elapsed)
