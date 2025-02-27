from statistics import fmean

import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(graph: nx.Graph, title: str = "Graph Visualization"):
    multiedges_labels = ["Q", "P"]

    plt.figure(figsize=(12, 12), facecolor='black')

    positions = nodes_positions(graph, multiedges_labels)

    nx.draw(
        graph,
        pos=positions,
        with_labels=True,
        labels=node_labels(graph, multiedges_labels),
        node_color=node_colors(graph, multiedges_labels),
        node_size=node_sizes(graph, multiedges_labels),
        edge_color="gray",
        width=2,
        font_size=15,
        font_weight='bold',
        font_color='black',
        alpha=0.8,
    )

    nx.draw_networkx_edge_labels(
        graph,
        pos=positions,
        edge_labels=edge_labels(graph),
        font_size=14,
        font_color='black',
        font_weight='bold',
    )

    plt.title(title, fontsize=20, color='black', fontweight='bold')
    plt.axis('off')
    plt.show()


def node_labels(graph, multiedges_labels):
    labels = {}

    for node, data in graph.nodes(True):
        label = data.get("label")
        if label in multiedges_labels:
            labels[node] = f"{label}\nR = {data.get('R')}"
        else:
            labels[node] = (
                f"x = {data.get('x')}\ny = {data.get('y')}\nh = {data.get('h')}"
            )

    return labels


def node_sizes(graph, multiedges_labels):
    sizes = [
        3000 if data.get("label") in multiedges_labels else 5500
        for _, data in graph.nodes(True)
    ]
    return sizes


def node_colors(graph, multiedges_labels):
    colors = []
    for _, data in graph.nodes(True):
        label = data.get("label")
        h = data.get("h")
        if label in multiedges_labels and data.get("R") == 0:
            colors.append("red")
        elif label in multiedges_labels and data.get("R") == 1:
            colors.append("lightgreen")
        elif h == 1:
            colors.append("darkorange")
        else:
            colors.append("lightblue")
    return colors


def edge_labels(graph):
    edge_labels_dict = {}
    for u, v, data in graph.edges(data=True):
        if data.get("label") is not None:
            edge_labels_dict[(u, v)] = f"{data.get('label')}\nB = {data.get('B')}"
    return edge_labels_dict


def nodes_positions(graph, multiedges_labels):
    positions = {}
    for point, data in graph.nodes(True):
        if data.get("label") in multiedges_labels:
            x = fmean(
                [graph.nodes[neighbor].get("x") for neighbor in graph.neighbors(point)]
            )
            y = fmean(
                [graph.nodes[neighbor].get("y") for neighbor in graph.neighbors(point)]
            )
            positions[point] = (x, y)
        else:
            positions[point] = (data.get("x"), data.get("y"))
    return positions
