import pytest
import networkx as nx
from plot_graph import plot_graph

from productions.p10.production10 import ProductionP10


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


def get_7_nodes_graph_with_hanging_node(x_shift=0, y_shift=0):
    G = get_graph_without_hanging_node(x_shift, y_shift)
    G.add_node(f"v:{5.5 + x_shift}:{9 + y_shift}", label="v", x=5.5 + x_shift, y=9 + y_shift, h=1)
    G.add_edge(f"v:{5.5 + x_shift}:{9 + y_shift}", f"v:{8 + x_shift}:{9 + y_shift}", label="E", B=1)
    G.add_edge(f"v:{5.5 + x_shift}:{9 + y_shift}", f"v:{3 + x_shift}:{9 + y_shift}", label="E", B=1)
    G.remove_edge(f"v:{8 + x_shift}:{9 + y_shift}", f"v:{3 + x_shift}:{9 + y_shift}")
    return G


def get_7_nodes_graph_with_hanging_node_b0(x_shift=0, y_shift=0):
    G = get_graph_without_hanging_node_b0(x_shift, y_shift)
    G.add_node(f"v:{5.5 + x_shift}:{9 + y_shift}", label="v", x=5.5 + x_shift, y=9 + y_shift, h=1)
    G.add_edge(f"v:{5.5 + x_shift}:{9 + y_shift}", f"v:{8 + x_shift}:{9 + y_shift}", label="E", B=1)
    G.add_edge(f"v:{5.5 + x_shift}:{9 + y_shift}", f"v:{3 + x_shift}:{9 + y_shift}", label="E", B=1)
    G.remove_edge(f"v:{8 + x_shift}:{9 + y_shift}", f"v:{3 + x_shift}:{9 + y_shift}")
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
    G1 = get_7_nodes_graph_with_hanging_node(x_shift, y_shift)
    G2 = get_7_nodes_graph_with_hanging_node(x_shift + 10, y_shift)

    G = nx.compose(G1, G2)

    return G


def get_two_hexagons_with_1_hanging_node_with_common_vertex(x_shift=0, y_shift=0):
    G1 = get_graph_with_1_hanging_node(x_shift, y_shift)
    G2 = get_graph_with_1_hanging_node(x_shift + 10, y_shift)

    G = nx.compose(G1, G2)

    return G


def test_positive_p10_check():
    G = get_7_nodes_graph_with_hanging_node()
    assert ProductionP10(G).check


def test_negative_graph_without_hanging_node_p10_check():
    G = get_graph_without_hanging_node()
    assert ProductionP10(G).check is None


def test_negative_graph_with_1_hanging_node_p10_check():
    G = get_graph_with_1_hanging_node()

    assert ProductionP10(G).check is None


def test_with_1_hanging_node_p10_apply():
    G = get_graph_with_1_hanging_node()
    G_old = G.copy()
    ProductionP10(G).apply()
    assert nx.is_isomorphic(G, G_old)


def test_with_2_hanging_nodes_p10_apply():
    G = get_graph_with_2_hanging_nodes()
    G_old = G.copy()
    ProductionP10(G).apply()
    assert nx.is_isomorphic(G, G_old)


def test_without_hanging_node_p10_apply():
    G = get_graph_without_hanging_node()
    G_old = G.copy()
    ProductionP10(G).apply()
    assert nx.is_isomorphic(G, G_old)


def test_without_hanging_node_p10_apply():
    G = get_7_nodes_graph_with_hanging_node()
    G_old = G.copy()
    ProductionP10(G).apply()
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


def test_two_hexagons_with_1_hanging_node_with_common_vertex_p10_apply():
    G = get_two_hexagons_with_1_hanging_node_with_common_vertex()
    G_old = G.copy()
    ProductionP10(G).apply()
    assert nx.is_isomorphic(G, G_old)

    ProductionP10(G).apply()
    assert nx.is_isomorphic(G, G_old)


def test_get_two_hexagons_without_hanging_node_with_common_vertex_p10_apply():
    G = get_two_hexagons_without_hanging_node_with_common_vertex()
    # print(G.nodes)
    # plot_graph(G)
    G_old = G.copy()
    ProductionP10(G).apply()
    assert nx.is_isomorphic(G, G_old) is False

    h_node_count = len([node for node in G.nodes if G.nodes[node].get("h") == 1])
    assert h_node_count == 1

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

    ProductionP10(G).apply()
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
    G = get_7_nodes_graph_with_hanging_node_b0()
    G_old = G.copy()
    ProductionP10(G).apply()
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
