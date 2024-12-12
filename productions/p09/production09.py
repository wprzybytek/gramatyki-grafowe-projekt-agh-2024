from itertools import combinations

from ..production import Production


class ProductionP9(Production):
    """
    Production P9:
    Divides a hexagon into 6 smaller hexagons
    """

    @property
    def check(self):
        """Check if the production can be applied on the selected hexagon."""
        # Find nodes with R=1 (element marked for splitting) and h=0 for all vertices
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "S" and data.get("R") == 1:
                neighbors = list(self.graph.neighbors(node))
                if all(self.graph.nodes[n].get("h") == 0 for n in neighbors):
                    neighbors_edges_cnt = 0
                    for n1, n2 in combinations(neighbors, 2):
                        if self.graph.has_edge(n1, n2):
                            neighbors_edges_cnt += 1
                    print(neighbors_edges_cnt)
                    if neighbors_edges_cnt == 6:
                        print("prod 09 can be applied to this graph")
                        return self._extract_subgraph(node, neighbors)
        print("prod 09 can't be applied to this graph")
        return None

    def apply(self):
        """Apply P9 to divide the hexagon"""
        result = self.check
        if result:
            q_node, neighbors = result

            self.subgraph.remove_node(q_node)
            self.graph.remove_node(q_node)

            midpoints = {}
            for n1, n2 in combinations(neighbors, 2):
                if self.subgraph.get_edge_data(n1, n2):
                    self._create_midpoint(midpoints, n1, n2)

            self._fill_graph(neighbors, midpoints)
            self.graph.update(self.subgraph)


"""
from fake_graphs import *
from plot_graph import plot_graph
from productions.p09.production09 import ProductionP09

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node("S:5.0:5.0", label="S", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:10.0:10.0", {"label": "v", "x": 10.0, "y": 10.0, "h": 0}),
            ("v:0.0:10.0", {"label": "v", "x": 0.0, "y": 10.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:0.0:0.0", "v:10.0:0.0", {"label": "E", "B": 1}),
            ("v:15.0:5.0", "v:10.0:10.0", {"label": "E", "B": 1}),
            ("v:10.0:0.0", "v:15.0:5.0", {"label": "E", "B": 1}),
            ("v:10.0:10.0", "v:0.0:10.0", {"label": "E", "B": 1}),
            ("v:0.0:10.0", "v:15.0:15.0", {"label": "E", "B": 1}),
            ("v:15.0:15.0", "v:0.0:0.0", {"label": "E", "B": 1}),

            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:10.0:10.0"),
            ("S:5.0:5.0", "v:0.0:10.0"),
            ("S:5.0:5.0", "v:15.0:15.0"),

        ]
    )

    plot_graph(G)
    prod9 = ProductionP9(G)
    prod9.apply()
    plot_graph(G)
"""
