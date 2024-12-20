import pytest
import networkx as nx

from plot_graph import plot_graph

from productions.p21.production21 import ProductionP21


def prepare_test_graph(R=0, x_shift=0.0, y_shift=0.0) -> nx.Graph:
    """Prepares the basic 6-nodes and one P-node graph with optional shifts"""
    G = nx.Graph()

    G.add_node(f"P:{5.0 + x_shift}:{5.0 + y_shift}", label="P", R=R)

    G.add_nodes_from(
        [
            (f"v:{3.0 + x_shift}:{7.0 + y_shift}", {"label": "v", "x": 3.0 + x_shift, "y": 7.0 + y_shift, "h": 0}),
            (f"v:{7.0 + x_shift}:{7.0 + y_shift}", {"label": "v", "x": 7.0 + x_shift, "y": 7.0 + y_shift, "h": 0}),
            (f"v:{3.0 + x_shift}:{3.0 + y_shift}", {"label": "v", "x": 3.0 + x_shift, "y": 3.0 + y_shift, "h": 0}),
            (f"v:{7.0 + x_shift}:{3.0 + y_shift}", {"label": "v", "x": 7.0 + x_shift, "y": 3.0 + y_shift, "h": 0}),
            (f"v:{5.0 + x_shift}:{3.0 + y_shift}", {"label": "v", "x": 5.0 + x_shift, "y": 3.0 + y_shift, "h": 0}),
            (f"v:{3.0 + x_shift}:{5.0 + y_shift}", {"label": "v", "x": 3.0 + x_shift, "y": 5.0 + y_shift, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{3.0 + x_shift}:{7.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{7.0 + x_shift}:{7.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{3.0 + x_shift}:{3.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{7.0 + x_shift}:{3.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{5.0 + x_shift}:{3.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{3.0 + x_shift}:{5.0 + y_shift}"),
        ]
    )

    return G

def prepare_test_graph_with_5_nodes(R=0, x_shift=0.0, y_shift=0.0) -> nx.Graph:
    G = nx.Graph()

    G.add_node(f"P:{5.0 + x_shift}:{5.0 + y_shift}", label="P", R=R)

    G.add_nodes_from(
        [
            (f"v:{3.0 + x_shift}:{7.0 + y_shift}", {"label": "v", "x": 3.0 + x_shift, "y": 7.0 + y_shift, "h": 0}),
            (f"v:{7.0 + x_shift}:{7.0 + y_shift}", {"label": "v", "x": 7.0 + x_shift, "y": 7.0 + y_shift, "h": 0}),
            (f"v:{3.0 + x_shift}:{3.0 + y_shift}", {"label": "v", "x": 3.0 + x_shift, "y": 3.0 + y_shift, "h": 0}),
            (f"v:{7.0 + x_shift}:{3.0 + y_shift}", {"label": "v", "x": 7.0 + x_shift, "y": 3.0 + y_shift, "h": 0}),
            (f"v:{5.0 + x_shift}:{3.0 + y_shift}", {"label": "v", "x": 5.0 + x_shift, "y": 3.0 + y_shift, "h": 0}),
        ]
    )
    G.add_edges_from(
        [
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{3.0 + x_shift}:{7.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{7.0 + x_shift}:{7.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{3.0 + x_shift}:{3.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{7.0 + x_shift}:{3.0 + y_shift}"),
            (f"P:{5.0 + x_shift}:{5.0 + y_shift}", f"v:{5.0 + x_shift}:{3.0 + y_shift}"),
        ]
    )

    return G

def prepare_test_graph_with_additional_edge(R=0, x_shift=0.0, y_shift=0.0) -> nx.Graph:
    G = prepare_test_graph(R=R, x_shift=x_shift, y_shift=y_shift)
    G.add_edge(f"v:{3.0 + x_shift}:{7.0 + y_shift}", f"v:{7.0 + x_shift}:{7.0 + y_shift}")
    return G

def prepare_big_graph():
    G1 = prepare_test_graph(R=0)
    G2 = prepare_test_graph(R=0, x_shift=4.0, y_shift=4.0)

    G = nx.compose(G1, G2)
    return G


def prepare_graph_with_hanging_node(R=0, x_shift=0.0, y_shift=0.0):
    G = prepare_test_graph(R=R, x_shift=x_shift, y_shift=y_shift)
    G.nodes[f"v:{5.0 + x_shift}:{3.0 + y_shift}"]["h"] = 1
    return G


# def test_positive_p21_check():
#     G = prepare_test_graph(R=0)
#     assert ProductionP21(G).check


# def test_negative_p21_check():
#     G = prepare_test_graph(R=1)
#     assert ProductionP21(G).check is None


# def test_0R_p21_apply():
#     G = prepare_test_graph(R=0)
#     plot_graph(G, title="p21_1_test_0R_p21_apply_1_before")
#     G_old = G.copy()
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_1_test_0R_p21_apply_2_after")

#     assert G.number_of_nodes() == 7
#     assert G.number_of_edges() == 6
#     assert G.nodes["P:5.0:5.0"]["label"] == "P"
#     assert G.nodes["P:5.0:5.0"]["R"] == 1


# def test_1R_p21_apply():
#     G = prepare_test_graph(R=1)
#     plot_graph(G, title="p21_2_test_1R_p21_apply_1_before")
#     G_old = G.copy()
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_2_test_1R_p21_apply_2_after")
#     assert nx.is_isomorphic(G, G_old)


# def test_big_graph():
#     G = prepare_big_graph()
#     plot_graph(G, title="p21_3_test_big_graph_1_before")
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_3_test_big_graph_2_after")

#     P_nodes = [node for node in G.nodes if G.nodes[node]["label"] == "P"]
#     assert len(P_nodes) == 2
#     P_nodes_R0 = [node for node in P_nodes if G.nodes[node]["R"] == 0]
#     assert len(P_nodes_R0) == 1
#     hanging_nodes = [node for node in G.nodes if G.nodes[node].get("h", 0) == 1]
#     assert len(hanging_nodes) == 0

#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_3_test_big_graph_3_after")
#     P_nodes = [node for node in G.nodes if G.nodes[node]["label"] == "P"]
#     assert len(P_nodes) == 2
#     P_nodes_R0 = [node for node in P_nodes if G.nodes[node]["R"] == 0]
#     assert len(P_nodes_R0) == 0

#     hanging_nodes = [node for node in G.nodes if G.nodes[node].get("h", 0) == 1]
#     assert len(hanging_nodes) == 0


# def test_hanging_node_R0_graph():
#     G = prepare_graph_with_hanging_node(R=0)
#     plot_graph(G, title="p21_4_test_hanging_node_R0_graph_1_before")
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_4_test_hanging_node_R0_graph_2_after")
#     assert G.number_of_nodes() == 7
#     assert G.number_of_edges() == 6
#     assert G.nodes["P:5.0:5.0"]["label"] == "P"
#     assert G.nodes["P:5.0:5.0"]["R"] == 1

#     assert G.nodes["v:5.0:3.0"]["h"] == 1


# def test_hanging_node_R1_graph():
#     G = prepare_graph_with_hanging_node(R=1)
#     plot_graph(G, title="p21_5_test_hanging_node_R1_graph_1_before")
#     G_old = G.copy()
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_5_test_hanging_node_R1_graph_2_after")
#     assert nx.is_isomorphic(G, G_old)

# def test_5_nodes_graph():
#     G = prepare_test_graph_with_5_nodes(R=0)
#     G_old = G.copy()
#     plot_graph(G, title="p21_6_test_5_nodes_graph_1_before")
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_6_test_5_nodes_graph_2_after")
#     assert nx.is_isomorphic(G, G_old)


# def test_graph_with_additional_edge_R0():
#     G = prepare_test_graph_with_additional_edge(R=0)
#     G_old = G.copy()
#     plot_graph(G, title="p21_7_test_graph_with_additional_edge_R0_1_before")
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_7_test_graph_with_additional_edge_R0_2_after")
#     assert nx.is_isomorphic(G, G_old)
#     assert G.nodes["P:5.0:5.0"]["R"] == 1

# def test_graph_with_additional_edge_R1():
#     G = prepare_test_graph_with_additional_edge(R=1)
#     G_old = G.copy()
#     plot_graph(G, title="p21_7_test_graph_with_additional_edge_R1_1_before")
#     ProductionP21(G).apply()
#     plot_graph(G, title="p21_7_test_graph_with_additional_edge_R1_2_after")
#     assert nx.is_isomorphic(G, G_old)
#     assert G.nodes["P:5.0:5.0"]["R"] == 1

def test_different_label_graph():
    G = prepare_test_graph()
    G.nodes["P:5.0:5.0"]["label"] = "Q"
    plot_graph(G, title="p21_8_test_different_label_graph_1_before")
    assert ProductionP21(G).check is None
    plot_graph(G, title="p21_8_test_different_label_graph_2_after")
