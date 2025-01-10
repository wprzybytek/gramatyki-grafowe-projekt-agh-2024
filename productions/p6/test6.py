import pytest
from productions.p6.production6 import ProductionP6
from .utils import (
    valid_graph_p6,
    valid_graph_p5,
    big_graph_2_h_nodes,
    prepare_square_with_four_hanging_nodes_graph,
    prepare_square_with_three_hanging_nodes_graph_broken,
)
from plot_graph import plot_graph


@pytest.mark.parametrize("graph_func, should_apply", [
    (valid_graph_p6, True),  # Valid P6
    (valid_graph_p5, False),  # P6 on P5
    (big_graph_2_h_nodes, False),  # P6 on 2H
    (prepare_square_with_four_hanging_nodes_graph, True),  # P6 with 4 hanging nodes
    (prepare_square_with_three_hanging_nodes_graph_broken, False),  # P6 broken graph
])
def test_production_p6(graph_func, should_apply):
    """
    Testuje produkcję P6 na różnych grafach.
    """
    G = graph_func()
    plot_graph(G)  # Opcjonalne: Wizualizacja grafu przed przekształceniem
    prod = ProductionP6(G)

    try:
        prod.apply()
        applied = True
    except Exception as e:
        applied = False

    assert applied == should_apply, (
        f"Expected application of ProductionP6 to be {should_apply}, "
        f"but got {applied}."
    )
    plot_graph(G)  # Opcjonalne: Wizualizacja grafu po przekształceniu