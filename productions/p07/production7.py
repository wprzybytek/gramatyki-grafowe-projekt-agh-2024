from productions.production import Production


class ProductionP7(Production):
    def extract_left_side(self) -> None | str:
        for node, data in self.graph.nodes(data=True):
            if is_unsplittable_hyperedge_node(data):
                return node
        return None

    def apply(self):
        left_side = self.extract_left_side()
        if left_side:
            self.graph.nodes[left_side]["R"] = 1


def is_unsplittable_hyperedge_node(data) -> bool:
    return data.get("label") == "Q" and data.get("R") == 0
