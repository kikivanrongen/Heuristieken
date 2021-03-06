import __init__ as im

def visual_solution(data, solution, title):
    """ Function that visualizes the solution. Every trajectory has another color.
    """

    # get stations and coordinates
    stations = data.names
    x = data.x
    y = data.y

    # loop through trains and draw a trajectory
    for train in solution.trains:
        x_cor = []
        y_cor = []
        past_stations = train.past_stations

        # append x and y coordinates for past stations
        for station in past_stations:
            index = stations.index(station)
            x_cor.append(x[index])
            y_cor.append(y[index])

        # plot trajectories
        im.plt.plot(y_cor, x_cor)

    # plot all trajectories in one plot
    im.plt.title(title)
    im.plt.show()

def visual(data, title):
    """ Visualisation of all possible trajectories. The critical connections
    and critical stations are marked red. The other stations and connections are
    marked blue.
    """

    # define variables
    stations = data.names
    x = data.x
    y = data.y
    connections = data.connections
    critical_connections = data.critical_connections
    critical_stations = data.critical_stations

    # define lists for x and y coordinates for critical stations and all stations
    x_cor_s = []
    y_cor_s = []
    x_cor_cs = []
    y_cor_cs = []

    # plot all connections
    for key, values in connections.items():
        for value in values:
            index = stations.index(key)
            x_cor = x[index]
            y_cor = y[index]

            index2 = stations.index(value)
            x_cor2 = x[index2]
            y_cor2 = y[index2]

            im.plt.plot([y_cor, y_cor2], [x_cor, x_cor2], "blue")

    # plot critical connections
    for a, b in critical_connections:
        index = stations.index(a)
        x_cor = x[index]
        y_cor = y[index]

        index2 = stations.index(b)
        x_cor2 = x[index2]
        y_cor2 = y[index2]

        im.plt.plot([y_cor, y_cor2], [x_cor, x_cor2], "red")

    # plot all stations
    im.plt.plot(y, x, "bo")

    # plot critical stations
    for station in critical_stations:
        index = stations.index(station)
        x_cor_cs.append(x[index])
        y_cor_cs.append(y[index])

    im.plt.plot(y_cor_cs, x_cor_cs, "ro")

    # name plot and show it
    im.plt.title(title)
    im.plt.show()
