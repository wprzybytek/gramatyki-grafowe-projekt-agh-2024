"""
Experimental file
Please DO NOT PUSH changes to this file 
"""
from fake_graphs import valid_graph
from plot_graph import plot_graph
from productions.p1.production1 import ProductionP1

if __name__ == '__main__':
    G = valid_graph()
    plot_graph(G)
    prod1 = ProductionP1(G)
    prod1.apply()
    plot_graph(G)
