from itertools import combinations

from ..production import Production


class ProductionP21(Production):
    """
    Production P21:
    Marks the hexagon elements as breakable. 
    """

    @property
    def check(self):
        """Checks if the production can be applied to the selected hexagon."""
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "S" and data.get("R") == 0:
                print("check passed")
                neighbors = list(self.graph.neighbors(node))
                return self._extract_subgraph(node, neighbors)
        print("didnt pass check")
        return None

    def apply(self):
        """Apply P21 to mark the hexagon elements as breakable."""

        result = self.check
        if result:
            r_node, neighbors = result
            self.graph.nodes[r_node]['R'] = 1 
