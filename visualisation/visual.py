# In dit document worden de stations en de uiteindelijke optimale
# route gevisualiseerd dmv van een scatterplot

import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# # laad de verschillende stations
# def visualization(?):
#     """ Visualiseerd de stations. """
#     G = nx.Graph()
#
#     # voeg alle stations van de classes toe
#     G.add_node()
#
#     # maak lijnen voor sations met sporen ertussen
#     G.add_path()
#
#     #als node kritiek is geef andere kleur dan anderen
#
#     # teken de plot en sla afbeelding op
#     nx.draw(G)
#     plt.savefig(path.png)

def histogram(list):
    num = len(list)
    plt.plot(list)
    plt.ylabel("score")
    return plt.show()
