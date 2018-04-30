import csv

class Stations():

    def __init__(self):

        self.names = []
        self.x = []
        self.y = []
        self.critical = []

        self.critical_stations = []

        self.connections = {}
        self.critical_connections = []

    def stations(self, stations_csv):
        """returns list of all stations with corresponding coordinates"""

        # open csv file with stations
        with open (stations_csv) as file_stations:

            # read csv file and return list of columns
            read_stations = csv.reader(file_stations)

            # iterate over rows and append to class
            for row in read_stations:
                self.names.append(row[0])
                self.x.append(float(row[1]))
                self.y.append(float(row[2]))

                # check for 
                if row[3] == 'Kritiek':
                    self.critical.append(True)
                    self.critical_stations.append(row[0])
                else:
                    self.critical.append(False)

    def railroads(self, connections_csv):
        """returns dictionary with station and all corresponding connections"""

        with open (connections_csv) as file_connections:

            read_connections = csv.reader(file_connections)

            for row in read_connections:
                self.connections[row[0]] = self.connections.get(row[0], []) + [row[1], float(row[2])]
                self.connections[row[1]] = self.connections.get(row[1], []) + [row[0], float(row[2])]

                if row[0] in self.critical_stations or row[1] in self.critical_stations:
                    self.critical_connections.append((row[0], row[1]))

class Train(Stations):

    def __init__(self, location):

        super().__init__()
        super().stations("data/StationsHolland.csv")
        super().railroads("data/ConnectiesHolland.csv")

        self.location = location
        self.past_stations = []
        self.past_critical_stations = []
        self.time_elapsed = 0
        self.number_critical = 0


    def update_trajectory(self, to_location):
        """update trajectory that the train has covered"""

        self.to_location = to_location

        possibilities = self.connections[self.location]

        for s,t in zip(possibilities[0::2], possibilities[1::2]):

            if self.to_location == s:

                self.time_elapsed += t
                self.past_stations.append(self.to_location)

                for element in self.critical_stations:

                    if element == self.location:
                        self.number_critical += 1
                        self.past_critical_stations.append(self.to_location)

            self.location = self.to_location
