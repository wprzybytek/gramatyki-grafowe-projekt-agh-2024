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
            if data.get("label") == "P" and data.get("R") == 1:
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
from productions.p09.production09 import ProductionP9

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
    G.add_nodes_from(
        [
            ("v:10:5", {"label": "v", "x": 10, "y": 5, "h": 0}),
            ("v:8:9", {"label": "v", "x": 8, "y": 9, "h": 0}),
            ("v:3:9", {"label": "v", "x": 3, "y": 9, "h": 0}),
            ("v:0:5", {"label": "v", "x": 0, "y": 5, "h": 0}),
            ("v:2:1", {"label": "v", "x": 2, "y": 1, "h": 0}),
            ("v:8:1", {"label": "v", "x": 8, "y": 1, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            ("v:10:5", "v:8:9", {"label": "E", "B": 0}),
            ("v:8:9", "v:3:9", {"label": "E", "B": 1}),
            ("v:3:9", "v:0:5", {"label": "E", "B": 1}),
            ("v:0:5", "v:2:1", {"label": "E", "B": 1}),
            ("v:2:1", "v:8:1", {"label": "E", "B": 1}),
            ("v:8:1", "v:10:5", {"label": "E", "B": 1}),

            ("P:5.0:5.0", "v:10:5"),
            ("P:5.0:5.0", "v:8:9"),
            ("P:5.0:5.0", "v:3:9"),
            ("P:5.0:5.0", "v:0:5"),
            ("P:5.0:5.0", "v:2:1"),
            ("P:5.0:5.0", "v:8:1"),
        ]
    )

    plot_graph(G)
    prod9 = ProductionP9(G)
    prod9.apply()
    plot_graph(G)
"""
