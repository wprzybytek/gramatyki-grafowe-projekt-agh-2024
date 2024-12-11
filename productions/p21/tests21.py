import pytest
import networkx as nx


from productions.p21.production21 import ProductionP21


def prepare_0R_test_graph() -> nx.Graph:
    """Prepares the basic 6-nodes and one S-node graph"""
    G = nx.Graph()
    
    G.add_node("S:5.0:5.0", label="S", R=0)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:5.0:15.0", {"label": "v", "x": 5.0, "y": 15.0, "h": 0}),
            ("v:0.0:5.0", {"label": "v", "x": 0.0, "y": 5.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}), # added
        ]
    )
    G.add_edges_from(
        [
            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:5.0:15.0"),
            ("S:5.0:5.0", "v:0.0:5.0"),
            ("S:5.0:5.0", "v:15.0:15.0"), # added
        ]
    )
    return G

def prepare_non_OR_test_graph() -> nx.Graph:
    """Prepares the basic 6-nodes and one S-node graph"""
    G = nx.Graph()
    
    G.add_node("S:5.0:5.0", label="S", R=1)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:5.0:15.0", {"label": "v", "x": 5.0, "y": 15.0, "h": 0}),
            ("v:0.0:5.0", {"label": "v", "x": 0.0, "y": 5.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}), # added
        ]
    )
    G.add_edges_from(
        [
            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:5.0:15.0"),
            ("S:5.0:5.0", "v:0.0:5.0"),
            ("S:5.0:5.0", "v:15.0:15.0"), # added
        ]
    )
    return G

G0R = prepare_0R_test_graph()
G1R = prepare_non_OR_test_graph()

@pytest.fixture(scope="function")
def prepare_graph_positive():
    yield prepare_0R_test_graph()

@pytest.fixture(scope="function")
def prepare_graph_negative():
    yield prepare_non_OR_test_graph()

def test_positive_p21_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP21(prepare_graph_positive).check is not None

def test_negative_p21_check(prepare_graph_negative: nx.Graph):
    """check is None if the graph is not valid"""
    assert ProductionP21(prepare_graph_negative).check is None
