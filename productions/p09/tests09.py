import pytest
import networkx as nx
from plot_graph import plot_graph

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


def get_graph_without_hanging_node_b0(x_shift=0, y_shift=0):
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
            (f"v:{8 + x_shift}:{1 + y_shift}", f"v:{10 + x_shift}:{5 + y_shift}", {"label": "E", "B": 0}),
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


def get_two_hexagons_without_hanging_node_with_common_vertex(x_shift=0, y_shift=0):
    G1 = get_graph_without_hanging_node(x_shift, y_shift)
    G2 = get_graph_without_hanging_node(x_shift + 10, y_shift)

    G = nx.compose(G1, G2)

    return G


def get_two_hexagons_with_1_hanging_node_with_common_vertex(x_shift=0, y_shift=0):
    G1 = get_graph_with_1_hanging_node(x_shift, y_shift)
    G2 = get_graph_with_1_hanging_node(x_shift + 10, y_shift)

    G = nx.compose(G1, G2)

    return G


def test_positive_p09_check():
    G = get_graph_without_hanging_node()
    assert ProductionP9(G).check is not None


def test_negative_p09_check():
    G = get_graph_with_1_hanging_node()
    assert ProductionP9(G).check is None


def test_with_1_hanging_node_p09_apply():
    G = get_graph_with_1_hanging_node()
    plot_graph(G, title="p09_1_test_with_1_hanging_node_p09_apply_1_before")
    G_old = G.copy()
    ProductionP9(G).apply()
    assert nx.is_isomorphic(G, G_old)
    plot_graph(G, title="p09_1_test_with_1_hanging_node_p09_apply_2_after")

def test_with_2_hanging_nodes_p09_apply():
    G = get_graph_with_2_hanging_nodes()
    plot_graph(G, title="p09_2_test_with_2_hanging_nodes_p09_apply_1_before")
    G_old = G.copy()
    ProductionP9(G).apply()
    assert nx.is_isomorphic(G, G_old)
    plot_graph(G, title="p09_2_test_with_2_hanging_nodes_p09_apply_2_after")


def test_without_hanging_node_p09_apply():
    G = get_graph_without_hanging_node()
    plot_graph(G, title="p09_3_test_without_hanging_node_p09_apply_1_before")
    G_old = G.copy()
    ProductionP9(G).apply()
    plot_graph(G, title="p09_3_test_without_hanging_node_p09_apply_2_after")
    assert nx.is_isomorphic(G, G_old) is False

    for node in G.nodes:
        assert G.nodes[node].get("h", 0) == 0

    p_nodes_with_r_0 = [node for node in G.nodes if G.nodes[node].get("label") == "Q" and G.nodes[node].get("R") == 0]
    assert len(p_nodes_with_r_0) == 6

    p_nodes_with_r_0_neighbors = [set(G.neighbors(node)) for node in p_nodes_with_r_0]
    common_neighbors = set.intersection(*p_nodes_with_r_0_neighbors)
    assert len(common_neighbors) == 1

    common_neighbor = common_neighbors.pop()
    for neighbor in G.neighbors(common_neighbor):
        if neighbor in p_nodes_with_r_0:
            continue
        assert G[common_neighbor][neighbor].get("B") == 0


def test_two_hexagons_with_1_hanging_node_with_common_vertex_p09_apply():
    G = get_two_hexagons_with_1_hanging_node_with_common_vertex()
    plot_graph(G, title="p09_4_test_two_hexagons_with_1_hanging_node_with_common_vertex_p09_apply_1_before")
    G_old = G.copy()
    ProductionP9(G).apply()
    plot_graph(G, title="p09_4_test_two_hexagons_with_1_hanging_node_with_common_vertex_p09_apply_2_after")
    assert nx.is_isomorphic(G, G_old)

    ProductionP9(G).apply()
    plot_graph(G, title="p09_4_test_two_hexagons_with_1_hanging_node_with_common_vertex_p09_apply_3_after")
    assert nx.is_isomorphic(G, G_old)


def test_get_two_hexagons_without_hanging_node_with_common_vertex_p09_apply():
    G = get_two_hexagons_without_hanging_node_with_common_vertex()
    plot_graph(G, title="p09_5_test_get_two_hexagons_without_hanging_node_with_common_vertex_p09_apply_1_before")
    G_old = G.copy()
    ProductionP9(G).apply()
    plot_graph(G, title="p09_5_test_get_two_hexagons_without_hanging_node_with_common_vertex_p09_apply_2_after")
    assert nx.is_isomorphic(G, G_old) is False

    for node in G.nodes:
        assert G.nodes[node].get("h", 0) == 0

    p_nodes_with_r_0 = [node for node in G.nodes if G.nodes[node].get("label") == "Q" and G.nodes[node].get("R") == 0]
    assert len(p_nodes_with_r_0) == 6

    p_nodes_with_r_0_neighbors = [set(G.neighbors(node)) for node in p_nodes_with_r_0]
    common_neighbors = set.intersection(*p_nodes_with_r_0_neighbors)
    assert len(common_neighbors) == 1

    common_neighbor = common_neighbors.pop()
    for neighbor in G.neighbors(common_neighbor):
        if neighbor in p_nodes_with_r_0:
            continue
        assert G[common_neighbor][neighbor].get("B") == 0

    ProductionP9(G).apply()
    plot_graph(G, title="p09_5_test_get_two_hexagons_without_hanging_node_with_common_vertex_p09_apply_3_after")
    assert nx.is_isomorphic(G, G_old) is False

    for node in G.nodes:
        assert G.nodes[node].get("h", 0) == 0

    p_nodes_with_r_0 = [node for node in G.nodes if G.nodes[node].get("label") == "Q" and G.nodes[node].get("R") == 0]
    assert len(p_nodes_with_r_0) == 12

    b_0_edges = [edge for edge in G.edges if G[edge[0]][edge[1]].get("B") == 0]
    assert len(b_0_edges) == 12

    b_1_edges = [edge for edge in G.edges if G[edge[0]][edge[1]].get("B") == 1]
    assert len(b_1_edges) == 24


def test_without_hanging_node_b0_p09_apply():
    G = get_graph_without_hanging_node_b0()
    plot_graph(G, title="p09_6_test_without_hanging_node_b0_p09_apply_1_before")
    G_old = G.copy()
    ProductionP9(G).apply()
    plot_graph(G, title="p09_6_test_without_hanging_node_b0_p09_apply_2_after")
    assert nx.is_isomorphic(G, G_old) is False

    h_node = "v:9.0:3.0"

    assert G.nodes[h_node].get("h") == 1

    not_h_nodes = [node for node in G.nodes if node != h_node]
    for node in not_h_nodes:
        assert G.nodes[node].get("h", 0) == 0

    p_nodes_with_r_0 = [node for node in G.nodes if G.nodes[node].get("label") == "Q" and G.nodes[node].get("R") == 0]
    assert len(p_nodes_with_r_0) == 6

    p_nodes_with_r_0_neighbors = [set(G.neighbors(node)) for node in p_nodes_with_r_0]
    common_neighbors = set.intersection(*p_nodes_with_r_0_neighbors)
    assert len(common_neighbors) == 1

    common_neighbor = common_neighbors.pop()
    for neighbor in G.neighbors(common_neighbor):
        if neighbor in p_nodes_with_r_0:
            continue
        assert G[common_neighbor][neighbor].get("B") == 0


def test_different_label_graph():
    G = get_graph_without_hanging_node()
    G.nodes["P:5.0:5.0"]["label"] = "Q"
    plot_graph(G, title="p09_7_test_different_label_graph_1_before")
    assert ProductionP9(G).check is None
    plot_graph(G, title="p09_7_test_different_label_graph_2_after")
