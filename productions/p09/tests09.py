import pytest
import networkx as nx


from productions.p09.production09 import ProductionP9

def get_graph_without_hanging_node(x_shift=0, y_shift=0):
    G = nx.Graph()
    G.add_node(f"P:{5.0 + x_shift}:{5.0 + y_shift}", label="P", R=1)
    G.add_nodes_from(
        [
            (f"v:{10 + x_shift}:{5 + y_shift}", {"label": "v", "x": 10 + x_shift, "y": 5 + y_shift, "h": 0}),
            (f"v:{8 + x_shift}:{9 + y_shift}", {"label": "v", "x": 8 + x_shift, "y": 9 + y_shift, "h": 0}),
            (f"v:{3 + x_shift}:{9 + y_shift}", {"label": "v", "x": 3 + x_shift, "y": 9 + y_shift, "h": 0}),
            (f"v:{0 + x_shift}:{5 + y_shift}", {"label": "v", "x": 0 + x_shift, "y": 5 + y_shift, "h": 0}),
            (f"v:{2 + x_shift}:{1 + y_shift}", {"label": "v", "x": 2 + x_shift, "y": 1 + y_shift, "h": 0}),
            (f"v:{8 + x_shift}:{1 + y_shift}", {"label": "v", "x": 8 + x_shift, "y": 1 + y_shift, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            (f"v:{10 + x_shift}:{5 + y_shift}", f"v:{8 + x_shift}:{9 + y_shift}", {"label": "E", "B": 1}),
            (f"v:{8 + x_shift}:{9 + y_shift}", f"v:{3 + x_shift}:{9 + y_shift}", {"label": "E", "B": 1}),
            (f"v:{3 + x_shift}:{9 + y_shift}", f"v:{0 + x_shift}:{5 + y_shift}", {"label": "E", "B": 1}),
            (f"v:{0 + x_shift}:{5 + y_shift}", f"v:{2 + x_shift}:{1 + y_shift}", {"label": "E", "B": 1}),
            (f"v:{2 + x_shift}:{1 + y_shift}", f"v:{8 + x_shift}:{1 + y_shift}", {"label": "E", "B": 1}),
            (f"v:{8 + x_shift}:{1 + y_shift}", f"v:{10 + x_shift}:{5 + y_shift}", {"label": "E", "B": 1}),

            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{10 + x_shift}:{5 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{8 + x_shift}:{9 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{3 + x_shift}:{9 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{0 + x_shift}:{5 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{2 + x_shift}:{1 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{8 + x_shift}:{1 + y_shift}"),
        ]
    )
    return G

def get_graph_with_1_hanging_node(x_shift=0, y_shift=0):
    G = get_graph_without_hanging_node(x_shift, y_shift)
    G.nodes[f"v:{8 + x_shift}:{9 + y_shift}"]["h"] = 1
    return G

def get_graph_with_2_hanging_nodes(x_shift=0, y_shift=0):
    G = get_graph_without_hanging_node(x_shift, y_shift)
    G.nodes[f"v:{8 + x_shift}:{9 + y_shift}"]["h"] = 1
    G.nodes[f"v:{3 + x_shift}:{9 + y_shift}"]["h"] = 1
    return G

def get_big_graph_with_2_hanging_nodes(x_shift=0, y_shift=0):
    G1 = get_graph_with_2_hanging_nodes(x_shift, y_shift)
    G2 = get_graph_with_2_hanging_nodes(x_shift + 20, y_shift)

    G = nx.compose(G1, G2)
    G.add_edge(f"v:{10 + x_shift}:{5 + y_shift}", f"v:{0 + x_shift + 20}:{5 + y_shift}", label="E", B=1)

    return G

def get_two_hexagons_without_hanging_node_with_common_edge(x_shift=0, y_shift=0):
    G1 = get_graph_without_hanging_node(x_shift, y_shift)
    G2 = get_graph_without_hanging_node(x_shift + 10, y_shift)

    G = nx.compose(G1, G2)

    return G

def get_two_hexagons_with_1_hanging_node_with_common_edge(x_shift=0, y_shift=0):
    G1 = get_graph_with_1_hanging_node(x_shift, y_shift)
    G2 = get_graph_with_1_hanging_node(x_shift + 10, y_shift)

    G = nx.compose(G1, G2)

    return G

def test_positive_p09_check():
    """check is not None if the graph is valid"""
    G = get_graph_without_hanging_node()
    assert ProductionP9(G).check is not None

def test_negative_p09_check():
    """check is not None if the graph is valid"""
    G = get_graph_with_1_hanging_node()
    assert ProductionP9(G).check is None
