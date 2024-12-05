"""
Experimental file
Please DO NOT PUSH changes to this file 
"""
from fake_graphs import *
from plot_graph import plot_graph
from productions.p1.production1 import ProductionP1
from productions.p2.production2 import ProductionP2

if __name__ == '__main__':
    G = valid_graph2()
    plot_graph(G)
    prod2 = ProductionP2(G)
    prod2.apply()
    plot_graph(G)
