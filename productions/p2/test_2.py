import pytest
import networkx as nx
import pickle

from productions.p2.production2 import ProductionP2
from productions.utils import prepare_big_graph, prepare_basic_square_graph, prepare_basic_square_with_hanging_node_graph

@pytest.fixture(scope='function')
def prepare_test_big_graph():
    return prepare_big_graph()

@pytest.fixture(scope='function')
def one_square_subgraph():
    yield prepare_basic_square_graph()


@pytest.fixture(scope='function')
def basic_square_with_hanging_node():
    yield prepare_basic_square_with_hanging_node_graph()



def test_p02_extraction_without_hanging_node(one_square_subgraph: nx.Graph):
    """Production is not able to extract left side when graph is basic square"""
    assert ProductionP2(one_square_subgraph).extract_left_side() is None


def test_p02_extraction_with_hanging_node(basic_square_with_hanging_node: nx.Graph):
    """Production is able to extract left side when graph is exactly left side of the production"""
    assert ProductionP2(basic_square_with_hanging_node).extract_left_side() is not None


def test_p02_check_after_production(basic_square_with_hanging_node: nx.Graph):
    """check is None after apply the production1"""
    ProductionP2(basic_square_with_hanging_node).apply()
    assert ProductionP2(basic_square_with_hanging_node).extract_left_side() is None



def test_p2_on_3x3_grid():
    with open('productions/p2/3x3-grid-before.pkl', 'rb') as f:
        before_graph = pickle.load(f)

    with open('productions/p2/3x3-grid-after.pkl', 'rb') as f:
        after_graph = pickle.load(f)

    prod2 = ProductionP2(before_graph)
    assert prod2.extract_left_side() is not None
    prod2.apply()

    assert nx.is_isomorphic(before_graph, after_graph)

