import csv

def stations(stations_csv):
    """returns list of dictionaries containing all stations with
    corresponding coordinates"""

    # create empty list
    stations = list()

    # open csv file with stations
    with open (stations_csv) as file_stations:

        # read csv file and return list of columns
        read_stations = csv.reader(file_stations)

        # iterate over rows and append to list
        for row in read_stations:
            stations.append(row)

    return stations

def railroads(railroads_csv):
    """returns list of all railroads between stations"""

    # create empty list
    railroads = list()

    # open csv file with connections
    with open (railroads_csv) as file_railroads:

        # read csv file and return list of columns
        read_railroads = csv.DictReader(file_railroads)

        # iterate over rows and append to list
        for row in read_railroads:
            railroads.append(row)

    return railroads
