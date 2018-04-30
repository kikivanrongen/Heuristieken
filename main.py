import csv
import classes.classes
import loading.load

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

# print(NZ_Holland.connections)
# print(NZ_Holland.connections['Alkmaar'])

B = classes.classes.Train("Alkmaar")
print(B.location)
print(B.past_stations)
print(B.past_critical_stations)
print(B.time_elapsed)

B.update_trajectory(to_location="Hoorn")
print(B.location)
print(B.past_stations)
print(B.past_critical_stations)
print(B.time_elapsed)
print(B.number_critical)

B.update_trajectory(to_location="Zaandam")
print(B.location)
print(B.past_stations)
print(B.past_critical_stations)
print(B.time_elapsed)
print(B.number_critical)

B.update_trajectory(to_location="Beverwijk")
print(B.location)
print(B.past_stations)
print(B.past_critical_stations)
print(B.time_elapsed)
print(B.number_critical)
