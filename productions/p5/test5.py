import pytest
from productions.p5.production5 import ProductionP5
from .utils import (
    valid_graph_p5,
    valid_graph_p6,
    big_graph_2_h_nodes,
    prepare_square_with_three_hanging_nodes_graph_broken,
)
from plot_graph import plot_graph


@pytest.mark.parametrize("graph_func, should_apply", [
    (valid_graph_p5, True),  # Valid P5
    (valid_graph_p6, False),  # P5 on P6
    (big_graph_2_h_nodes, False),  # P5 on 2H
    (prepare_square_with_three_hanging_nodes_graph_broken, False),  # P5 R=0
])
def test_production_p5(graph_func, should_apply):
    """
    Testuje produkcję P5 na różnych grafach.
    """
    G = graph_func()
    plot_graph(G)  # Opcjonalne: Wizualizacja grafu przed przekształceniem
    prod = ProductionP5(G)

    try:
        prod.apply()
        applied = True
    except Exception as e:
        applied = False

    assert applied == should_apply, (
        f"Expected application of ProductionP5 to be {should_apply}, "
        f"but got {applied}."
    )
    plot_graph(G)  # Opcjonalne: Wizualizacja grafu po przekształceniu