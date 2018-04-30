# In dit document worden de stations en de uiteindelijke optimale
# route gevisualiseerd dmv van een scatterplot

import csv
import networkx as nx
import matplotlib.pyplot as plt
from classes import classes

# laad de verschillende stations
def visualization(?):
    """ Visualiseerd de stations. """
    G = nx.Graph()

    # voeg alle stations van de classes toe
    G.add_node()

    # maak lijnen voor sations met sporen ertussen
    G.add_path()

    #als node kritiek is geef andere kleur dan anderen

    # teken de plot en sla afbeelding op
    nx.draw(G)
    plt.savefig(path.png)
