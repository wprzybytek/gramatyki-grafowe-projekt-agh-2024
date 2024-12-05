from itertools import combinations
import networkx as nx
from networkx.classes import neighbors

from productions.production import Production

class ProductionP2(Production):

    def check(self):
        for node, data in self.graph.nodes(data=True):
            if is_hyperedge_node(data) and can_be_splitted(data):
                neighbors = list(self.graph.neighbors(node))
                if all_are_not_hanging_node(self.graph, neighbors) and len(neighbors) == 4:
                    a, middle, b = find_vertex_line(self.graph, neighbors)
                    print(node, neighbors)
                    print(a, middle, b)

                    if middle is not None and self.graph.nodes[middle].get('h') == 1:
                        return self._extract_subgraph(node, neighbors + [middle]), (a, middle, b)
        return False

    def apply(self):
        result = self.check()
        if result != False:
            (q, neighbors), (a, middle, b) = result
            neighbors.pop() # remove middle
            self.subgraph.remove_node(q)
            self.graph.remove_node(q)

            midpoints = {middle: (a, b)}
            for (n1, n2) in combinations(neighbors, 2):
                if self.subgraph.has_edge(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)

            self._fill_graph(neighbors, midpoints)
            self.subgraph.nodes[middle]['h'] = 0

            self.graph.update(self.subgraph)


def is_hyperedge_node(data):
    return data.get('label') == 'Q'


def can_be_splitted(data):
    return data.get('R') == 1


def all_are_not_hanging_node(graph, neighbors):
    return all(graph.nodes[n].get('h') == 0 for n in neighbors)

def find_vertex_line(graph: nx.Graph, neighbors: list):
    for n1, n2 in combinations(neighbors, 2):
        # print(n1, n2)
        # if graph.has_edge(n1, n2):
        #     print("has edge")
        #     continue
        # else:
        #     print("no edge")

        m = find_middlepoint(graph, n1, n2)

        if m is not None:
            return n1, m, n2

    return None, None, None

    
def find_middlepoint(graph: nx.Graph, n1, n2):
    for n in graph.neighbors(n1):
        if n in graph.neighbors(n2) and not is_hyperedge_node(graph.nodes[n]) and graph.nodes[n].get('h') == 1:
            return n
    return None

 


