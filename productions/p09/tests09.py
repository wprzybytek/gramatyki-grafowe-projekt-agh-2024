import pytest
import networkx as nx


from productions.p09.production09 import ProductionP9

def prepare_valid_test_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_node("P:5.0:5.0", label="P", R=1)
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

            ("P:5.0:5.0", "v:0.0:0.0"),
            ("P:5.0:5.0", "v:15.0:5.0"),
            ("P:5.0:5.0", "v:10.0:0.0"),
            ("P:5.0:5.0", "v:10.0:10.0"),
            ("P:5.0:5.0", "v:0.0:10.0"),
            ("P:5.0:5.0", "v:15.0:15.0"),

        ]
    )

    return G

def prepare_valid_test_graph_with_hanging_node() -> nx.Graph:
    pass


@pytest.fixture(scope="function")
def prepare_graph_positive():
    yield prepare_valid_test_graph()


@pytest.fixture(scope="function")
def prepare_graph_positive_hanging():
    yield prepare_valid_test_graph_with_hanging_node()


def test_positive_p09_check(prepare_graph_positive: nx.Graph):
    """check is not None if the graph is valid"""
    assert ProductionP9(prepare_graph_positive).check is not None

