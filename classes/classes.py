import csv

class Stations():

    def __init__(self):

        self.names = []
        self.x = []
        self.y = []
        self.critical = []

        self.critical_stations = []

        self.connections = {}
        self.connection_time = {}
        self.critical_connections = []

    def stations(self, stations_csv):
        """creates object of stations with characteristics"""

        # open csv file with stations
        with open (stations_csv) as file_stations:

            # read csv file of stations and return list of columns
            read_stations = csv.reader(file_stations)

            # iterate over rows and append to class
            for row in read_stations:
                self.names.append(row[0])
                self.x.append(float(row[1]))
                self.y.append(float(row[2]))

                # create list of critical stations
                if row[3] == 'Kritiek':
                    self.critical.append(True)
                    self.critical_stations.append(row[0])
                else:
                    self.critical.append(False)

    def railroads(self, connections_csv):
        """creates object of connections with characteristics"""

        # open csv file of conections
        with open (connections_csv) as file_connections:

            # read csv file of connections and return list of columns
            read_connections = csv.reader(file_connections)

            # iterate over rows and append to class
            for row in read_connections:

                # create dictionary with station as key and possible connections (array) as value
                self.connections[row[0]] = self.connections.get(row[0], []) + [row[1]]
                self.connections[row[1]] = self.connections.get(row[1], []) + [row[0]]

                # create dictionary with station as key and connection times (array) as value
                self.connection_time[row[0]] = self.connection_time.get(row[0], []) + [float(row[2])]
                self.connection_time[row[1]] = self.connection_time.get(row[1], []) + [float(row[2])]

                # create list of critical connections
                if row[0] in self.critical_stations or row[1] in self.critical_stations:
                    self.critical_connections.append((row[0], row[1]))

class Train():

    def __init__(self, location, stations):

        self.location = location
        self.stations = stations
        self.past_stations = []
        self.past_critical_stations = []
        self.time_elapsed = 0
        self.number_critical = 0

    def update_trajectory(self, to_location):
        """update trajectory that the train has covered"""

        self.to_location = to_location

        # find possible connections with current location and corresponding time
        possibilities = self.stations.connections[self.location]
        possibilities_time = self.stations.connection_time[self.location]

        # iterate over possible connections
        for index, place in enumerate(possibilities):

            # check if given trajectory is valid
            if self.to_location == place:

                # update train properties
                self.time_elapsed += possibilities_time[index]
                self.past_stations.append(place)

                # check if trajectory is critical, and if so, update train properties
                for element in self.stations.critical_stations:

                    if element == place:
                        self.number_critical += 1
                        self.past_critical_stations.append(place)

                # update current location
                self.location = self.to_location
