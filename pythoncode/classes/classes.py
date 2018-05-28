import __init__ as im

class Stations():
    """
    Open and read data, and store data in variables accordingly. This object constains
    the environment of the project.
    """

    def __init__(self):
        """
        The init function defines all variables that are set with data in the
        following functions: stations and railroads. This contains characteristics
        of the stations, such as: name, coordinates, critical/non-critical, connections
        (critical / non-critical) and connections with time. It also stores stations
        that have a critical connection seperately.
        """

        self.names = []
        self.x = []
        self.y = []
        self.critical = []

        self.critical_stations = []

        self.connections = {}
        self.connection_time = {}
        self.connection_and_time= {}
        self.critical_connections = []
        self.stations_with_critical_connection = []

    def stations(self, stations_csv):
        """
        This function opens and reads the station file that contains all stations
        in the environment with corresponding coordinates. It also keeps track of
        critical stations.
        """

        # open csv file with stations
        with open (stations_csv) as file_stations:

            # read csv file of stations and return list of columns
            read_stations = im.csv.reader(file_stations)

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
        """
        This function opens and reads the connections file that contains all possible
        connections in the environment. The connections are stored in a dictionary as
        location: connection, location: connection time and location: (connection, time).
        It also stores critical connections in a seperate variable.
        """

        # open csv file of connections
        with open (connections_csv) as file_connections:

            # read csv file of connections and return list of columns
            read_connections = im.csv.reader(file_connections)

            # iterate over rows and append to class
            for row in read_connections:

                # create dictionary with station as key and possible connections (array) as value
                self.connections[row[0]] = self.connections.get(row[0], []) + [row[1]]
                self.connections[row[1]] = self.connections.get(row[1], []) + [row[0]]

                # create dictionary with station as key and connection times (array) as value
                self.connection_time[row[0]] = self.connection_time.get(row[0], []) + [float(row[2])]
                self.connection_time[row[1]] = self.connection_time.get(row[1], []) + [float(row[2])]

                # create dict with tuples of connection and the time
                self.connection_and_time[row[0]] = self.connection_and_time.get(row[0], []) + [(row[1], float(row[2]))]
                self.connection_and_time[row[1]] = self.connection_and_time.get(row[1], []) + [(row[0], float(row[2]))]

                # create list of critical connections
                if row[0] in self.critical_stations or row[1] in self.critical_stations:
                    self.critical_connections.append((row[0], row[1]))

                # make list of stations with a critical connections
                for station in self.critical_stations:
                    for connection in self.critical_connections:
                        if station == connection[0]:
                            self.stations_with_critical_connection.append(connection[1])
                        if station == connection[1]:
                            self.stations_with_critical_connection.append(connection[0])

                for station in self.critical_stations:
                    self.stations_with_critical_connection.append(station)

                self.stations_with_critical_connection = list(set(self.stations_with_critical_connection))

class Train():
    """
    Object that stores information of one train at a certain point in the trajectory
    in the given environment.
    """

    def __init__(self, location, stations):
        """
        The init function contains sets variables for the current location,
        past stations, past connections (critical/non-critical with count variable)
        and elapsed time.
        """

        self.location = location
        self.stations = stations
        self.past_stations = []
        self.past_critical_stations = []
        self.past_critical_connections = []
        self.past_connections = []
        self.time_elapsed = 0
        self.number_critical = 0

        self.past_stations.append(location)

    def update_trajectory(self, to_location):
        """
        This function checks if a go-to location is valid and if so, updates the
        trajectory. The elapsed time, past stations (critical/non-critical) and
        past critical connections are adjusted accordingly.
        """

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

                # check if trajectory is critical and if so, update train properties
                for element in self.stations.critical_stations:

                    if element == place:
                        self.number_critical += 1
                        self.past_critical_stations.append(place)
                        self.past_critical_connections.append((self.location, place))

                    else:
                        self.past_connections.append((self.location, place))

                # update current location
                self.location = self.to_location

class Trains():
    """
    This object keeps track of the entire solution given a particular environment.
    It contains two functions for adding new trains and calculating the score of
    a certain solution.
    """


    def __init__(self, stations):
        """
        The init function stores all the driven trajectories of class Train
        in a list and counts the number of trains.
        """

        self.trains = []
        self.stations = stations
        self.train_count = 0

    def add_train(self, train):
        """
        This function adds a new trajectory (train) to the entire solution. This
        trajectory is of class Train and is stored in the list trains. A count variable
        is also logged.
        """

        self.train = train
        self.trains.append(self.train)
        self.train_count += 1

    def score(self):
        """
        This function is implemented to calculate the score of a given solution.
        The formula is provided in the assignment and it requires the proportion of
        driven critical connections, the number of trains and the elapsed time of
        all trains. In order to calculate the proportion the covered critical connections
        of every train are stored in one list and duplicates are removed.
        """

        # set variables
        all_past_critical_connections = []
        minutes = 0
        total_critical = len(self.stations.critical_connections)

        # create list of all past critical stations
        for element in self.trains:
            all_past_critical_connections.append(element.past_critical_connections)
            minutes += element.time_elapsed

        # create one list of all past critical connections
        one_list = []
        for train in all_past_critical_connections:
            for route in train:
                one_list.append(route)

        # remove duplicates (both (a,b) and (b,a))
        cleared_set = set(one_list)
        complete_dict = {tuple(item) for item in map(sorted, cleared_set)}

        # calculate proportion of driven critical connections
        p = len(complete_dict) / total_critical

        # calculate score
        S = p * 10000 - (self.train_count * 20 + minutes / 10)

        return S

def score2(self):
    """
    Score function with only critical connections
    """

    # set variables
    all_past_connections = []
    minutes = 0
    total = len(self.stations.past_connections)

    # create list of all past critical stations
    for element in self.trains:
        all_past_connections.append(element.past_connections)
        minutes += element.time_elapsed

    # create one list of all past critical connections
    one_list = []
    for train in all_past_connections:
        for route in train:
            one_list.append(route)

    # remove duplicates (both (a,b) and (b,a))
    cleared_set = set(one_list)
    complete_dict = {tuple(item) for item in map(sorted, cleared_set)}

    # calculate proportion of driven critical connections
    p = len(complete_dict) / total

    # calculate score
    S = p * 10000 - (self.train_count * 20 + minutes / 10)

    return S
