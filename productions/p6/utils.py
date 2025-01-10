import networkx as nx

def prepare_square_with_three_hanging_nodes_graph() -> nx.Graph:
    """Prepares a 4-nodes square with Q-node and 3 hanging nodes.
       Hanging nodes are placed on three edges of the square.
    """
    G = nx.Graph()
    # Węzły narożne
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
    ])

    G.add_nodes_from([
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:0.5:1.0', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': 1}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
    ])

    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 0}),

        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:1.0', 'v:0.5:1.0', {'label': 'E', 'B': 1}),
        ('v:0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
    ])

    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='P', breakable=True)

    return G

def prepare_square_with_three_hanging_nodes_graph_broken() -> nx.Graph:
    """Prepares a 4-nodes square with Q-node and 3 hanging nodes.
       Hanging nodes are placed on three edges of the square.
    """
    G = nx.Graph()
    # Węzły narożne
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 1}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
    ])

    G.add_nodes_from([
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:0.5:1.0', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': 1}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
    ])

    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),

        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:1.0', 'v:0.5:1.0', {'label': 'E', 'B': 1}),
        ('v:0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
    ])

    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G

def prepare_square_with_three_hanging_nodes_graph_isomorf() -> nx.Graph:
    """Prepares a 4-nodes square with Q-node and 3 hanging nodes.
       Hanging nodes are placed on three edges of the square.
    """
    G = nx.Graph()
    # Węzły narożne
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
    ])

    G.add_nodes_from([
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:0.5:1.0', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': 1}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1}),
    ])

    G.add_edges_from([
        ('v:0.0:0.5', 'v:1.0:0.0', {'label': 'E', 'B': 1}),

        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:1.0', 'v:0.5:1.0', {'label': 'E', 'B': 1}),
        ('v:0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
    ])

    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G

def prepare_square_with_four_hanging_nodes_graph() -> nx.Graph:
    """Prepares a 4-nodes square with Q-node and 4 hanging nodes.
       Each of the four edges of the square has one hanging node.
    """
    G = nx.Graph()

    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
    ])

    G.add_nodes_from([
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:0.5:1.0', {'label': 'v', 'x': 0.5, 'y': 1.0, 'h': 1}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
    ])

    G.add_edges_from([
        ('v:0.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.5:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),

        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('v:1.0:1.0', 'v:0.5:1.0', {'label': 'E', 'B': 1}),
        ('v:0.5:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),

        ('v:0.0:1.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    ])

    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G

def add_hyperedge_to_graph(G: nx.Graph, nodes: list, hyperedge_label='Q',  breakable=True):
    """Add a hyperedge to the graph G."""
    G.add_node(hyperedge_label, label=hyperedge_label, R=1 if breakable else 0)
    G.add_edges_from([(node, hyperedge_label) for node in nodes])


def prepare_big_graph_with_hanging_node():
    G = nx.Graph()
    
    # Podstawowe wierzchołki graniczne i siatki
    base_nodes = [
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:5.0:0.0', {'label': 'v', 'x': 5.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:5.0', {'label': 'v', 'x': 10.0, 'y': 5.0, 'h': 0}),
        ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
        ('v:5.0:10.0', {'label': 'v', 'x': 5.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:5.0', {'label': 'v', 'x': 0.0, 'y': 5.0, 'h': 0}),
        ('v:5.0:5.0', {'label': 'v', 'x': 5.0, 'y': 5.0, 'h': 0}),
        
        ('v:2.5:5.0', {'label': 'v', 'x': 2.5, 'y': 5.0, 'h': 1}),
        ('v:0.0:2.5', {'label': 'v', 'x': 0.0, 'y': 2.5, 'h': 0}),
        ('v:2.5:0.0', {'label': 'v', 'x': 2.5, 'y': 0.0, 'h': 0}),
        ('v:5.0:2.5', {'label': 'v', 'x': 5.0, 'y': 2.5, 'h': 1}),
        ('v:2.5:2.5', {'label': 'v', 'x': 2.5, 'y': 2.5, 'h': 0}),
    ]
    
    # Węzły Q R=1
    Q_R1 = [
        ('Q:2.5:7.5', {'label': 'Q', 'R': 1}),
        ('Q:7.5:7.5', {'label': 'Q', 'R': 1}),
        ('Q:7.5:2.5', {'label': 'Q', 'R': 1}),  # wcześniej był R=0, teraz R=1 aby pasować do wzorca
    ]
    
    # Węzły Q R=0 istniejące w siatce
    Q_existing_R0 = [
        ('Q:1.25:1.25', {'label': 'Q', 'R': 0}),
        ('Q:1.25:3.75', {'label': 'Q', 'R': 0}),
        ('Q:3.75:1.25', {'label': 'Q', 'R': 0}),
        ('Q:3.75:3.75', {'label': 'Q', 'R': 0})
    ]
    
    G.add_nodes_from(base_nodes)
    G.add_nodes_from(Q_R1)
    G.add_nodes_from(Q_existing_R0)
    
    base_edges = [
        # Obrzeże zewnętrzne
        ('v:0.0:0.0', 'v:2.5:0.0', {'label': 'E', 'B': 1}),
        ('v:2.5:0.0', 'v:5.0:0.0', {'label': 'E', 'B': 1}),
        ('v:5.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
        ('v:10.0:0.0', 'v:10.0:5.0', {'label': 'E', 'B': 1}),
        ('v:10.0:5.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
        ('v:10.0:10.0', 'v:5.0:10.0', {'label': 'E', 'B': 1}),
        ('v:5.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
        ('v:0.0:10.0', 'v:0.0:5.0', {'label': 'E', 'B': 1}),
        ('v:0.0:5.0', 'v:0.0:2.5', {'label': 'E', 'B': 1}),
        ('v:0.0:2.5', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        
        # Sieć wewnętrzna
        ('v:5.0:5.0', 'v:10.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:10.0', {'label': 'E', 'B': 0}),
        ('v:0.0:5.0', 'v:2.5:5.0', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:5.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:5.0:0.0', {'label': 'E', 'B': 0}),
        
        ('v:0.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:0.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        
        # Połączenia do Q R=1
        ('Q:2.5:7.5', 'v:5.0:10.0'),
        ('Q:2.5:7.5', 'v:0.0:10.0'),
        ('Q:2.5:7.5', 'v:0.0:5.0'),
        ('Q:2.5:7.5', 'v:5.0:5.0'),
        
        ('Q:7.5:7.5', 'v:5.0:5.0'),
        ('Q:7.5:7.5', 'v:10.0:5.0'),
        ('Q:7.5:7.5', 'v:10.0:10.0'),
        ('Q:7.5:7.5', 'v:5.0:10.0'),
        
        ('Q:7.5:2.5', 'v:5.0:5.0'),
        ('Q:7.5:2.5', 'v:5.0:0.0'),
        ('Q:7.5:2.5', 'v:10.0:0.0'),
        ('Q:7.5:2.5', 'v:10.0:5.0'),
        
        # Połączenia do Q R=0 już istniejących
        ('Q:1.25:1.25', 'v:2.5:2.5'),
        ('Q:1.25:1.25', 'v:0.0:0.0'),
        ('Q:1.25:1.25', 'v:0.0:2.5'),
        ('Q:1.25:1.25', 'v:2.5:0.0'),
        
        ('Q:1.25:3.75', 'v:0.0:5.0'),
        ('Q:1.25:3.75', 'v:2.5:5.0'),
        ('Q:1.25:3.75', 'v:2.5:2.5'),
        ('Q:1.25:3.75', 'v:0.0:2.5'),
        
        ('Q:3.75:1.25', 'v:2.5:2.5'),
        ('Q:3.75:1.25', 'v:2.5:0.0'),
        ('Q:3.75:1.25', 'v:5.0:0.0'),
        ('Q:3.75:1.25', 'v:5.0:2.5'),
        
        ('Q:3.75:3.75', 'v:2.5:2.5'),
        ('Q:3.75:3.75', 'v:2.5:5.0'),
        ('Q:3.75:3.75', 'v:5.0:5.0'),
        ('Q:3.75:3.75', 'v:5.0:2.5'),
    ]
    G.add_edges_from(base_edges)
    
    # -------------------------------------
    # Podziały obszarów R=1 na mniejsze kwadraty z Q R=0
    # -------------------------------------
    
    def add_sub_squares(G, x_start, y_start, size=5.0):
        half = size / 2.0
        offsets = [(0,0),(half,0),(0,half),(half,half)]
        
        for dx, dy in offsets:
            x0 = x_start + dx
            y0 = y_start + dy
            # Wierzchołki małego kwadratu
            v_corners = [
                (x0, y0),
                (x0+half, y0),
                (x0+half, y0+half),
                (x0, y0+half)
            ]
            # Dodaj wierzchołki (o ile nie istnieją)
            for (vx, vy) in v_corners:
                v_name = f'v:{vx}:{vy}'
                if v_name not in G:
                    G.add_node(v_name, label='v', x=vx, y=vy, h=0)
            
            # Połącz wierzchołki kwadratu krawędziami
            edges_square = [
                (v_corners[0], v_corners[1]),
                (v_corners[1], v_corners[2]),
                (v_corners[2], v_corners[3]),
                (v_corners[3], v_corners[0])
            ]
            for (ax,ay),(bx,by) in edges_square:
                G.add_edge(f'v:{ax}:{ay}', f'v:{bx}:{by}', label='E', B=0)
            
            # Środek małego kwadratu i węzeł Q R=0
            cx = x0 + half/2.0
            cy = y0 + half/2.0
            q_name = f'Q:{cx}:{cy}'
            if q_name not in G:
                G.add_node(q_name, label='Q', R=0)
            
            # Połącz węzeł Q z czterema rogami kwadratu
            for (vx, vy) in v_corners:
                G.add_edge(q_name, f'v:{vx}:{vy}')
    
    # Podział obszaru wokół Q:2.5:7.5 (R=1)
    add_sub_squares(G, 0.0, 5.0, 5.0)
    
    # Podział obszaru wokół Q:7.5:7.5 (R=1)
    add_sub_squares(G, 5.0, 5.0, 5.0)

    # Podział obszaru wokół Q:7.5:2.5 (R=1)
    # Ten Q:7.5:2.5 znajduje się w kwadracie (5,0)-(10,0)-(10,5)-(5,5)
    add_sub_squares(G, 5.0, 0.0, 5.0)

    # -------------------------------------
    # Dodanie dodatkowego "wiszącego" węzła
    # -------------------------------------
    # Dodajemy węzeł Q poniżej v:10.0:0.0
    G.add_node('Q:10.0:-2.5', label='Q', R=0)
    G.add_edge('v:10.0:0.0', 'Q:10.0:-2.5', label='E', B=0)

    return G



def prepare_big_graph_5() -> nx.Graph:
    G = nx.Graph()
    # Węzły typu v
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:5.0:0.0', {'label': 'v', 'x': 5.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:5.0', {'label': 'v', 'x': 10.0, 'y': 5.0, 'h': 0}),
        ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
        ('v:5.0:10.0', {'label': 'v', 'x': 5.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:5.0', {'label': 'v', 'x': 0.0, 'y': 5.0, 'h': 0}),
        ('v:5.0:5.0', {'label': 'v', 'x': 5.0, 'y': 5.0, 'h': 0}),
        ('v:2.5:5.0', {'label': 'v', 'x': 2.5, 'y': 5.0, 'h': 1}),
        ('v:0.0:2.5', {'label': 'v', 'x': 0.0, 'y': 2.5, 'h': 0}),
        ('v:2.5:0.0', {'label': 'v', 'x': 2.5, 'y': 0.0, 'h': 0}),
        ('v:5.0:2.5', {'label': 'v', 'x': 5.0, 'y': 2.5, 'h': 1}),
        ('v:2.5:2.5', {'label': 'v', 'x': 2.5, 'y': 2.5, 'h': 0}),
    ])

    # Węzły Q z R=0 (pozostawione)
    G.add_nodes_from([
        ('Q:7.5:2.5', {'label': 'Q', 'R': 0}),
        ('Q:1.25:1.25', {'label': 'Q', 'R': 0}),
        ('Q:1.25:3.75', {'label': 'Q', 'R': 0}),
        ('Q:3.75:1.25', {'label': 'Q', 'R': 0}),
        ('Q:3.75:3.75', {'label': 'Q', 'R': 0})
    ])

    # Krawędzie typu E pomiędzy węzłami v
    G.add_edges_from([
        ('v:0.0:0.0', 'v:2.5:0.0', {'label': 'E', 'B': 1}),
        ('v:2.5:0.0', 'v:5.0:0.0', {'label': 'E', 'B': 1}),
        ('v:5.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
        ('v:10.0:0.0', 'v:10.0:5.0', {'label': 'E', 'B': 1}),
        ('v:10.0:5.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
        ('v:10.0:10.0', 'v:5.0:10.0', {'label': 'E', 'B': 1}),
        ('v:5.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
        ('v:0.0:10.0', 'v:0.0:5.0', {'label': 'E', 'B': 1}),
        ('v:0.0:5.0', 'v:0.0:2.5', {'label': 'E', 'B': 1}),
        ('v:0.0:2.5', 'v:0.0:0.0', {'label': 'E', 'B': 1}),

        ('v:5.0:5.0', 'v:10.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:10.0', {'label': 'E', 'B': 0}),

        ('v:0.0:5.0', 'v:2.5:5.0', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:5.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:5.0:0.0', {'label': 'E', 'B': 0}),

        ('v:0.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:0.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
    ])

    # Zastąpione hiper-krawędzie Q z R=0 (pozostały) -> już były obecne:
    G.add_edges_from([
        ('Q:7.5:2.5', 'v:5.0:5.0'), ('Q:7.5:2.5', 'v:5.0:0.0'), 
        ('Q:7.5:2.5', 'v:10.0:0.0'), ('Q:7.5:2.5', 'v:10.0:5.0'),

        ('Q:1.25:1.25', 'v:2.5:2.5'), ('Q:1.25:1.25', 'v:0.0:0.0'),
        ('Q:1.25:1.25', 'v:0.0:2.5'), ('Q:1.25:1.25', 'v:2.5:0.0'),

        ('Q:1.25:3.75', 'v:0.0:5.0'), ('Q:1.25:3.75', 'v:2.5:5.0'),
        ('Q:1.25:3.75', 'v:2.5:2.5'), ('Q:1.25:3.75', 'v:0.0:2.5'),

        ('Q:3.75:1.25', 'v:2.5:2.5'), ('Q:3.75:1.25', 'v:2.5:0.0'),
        ('Q:3.75:1.25', 'v:5.0:0.0'), ('Q:3.75:1.25', 'v:5.0:2.5'),

        ('Q:3.75:3.75', 'v:2.5:2.5'), ('Q:3.75:3.75', 'v:2.5:5.0'),
        ('Q:3.75:3.75', 'v:5.0:5.0'), ('Q:3.75:3.75', 'v:5.0:2.5'),
    ])

    # Dodajemy brakującą krawędź pomiędzy v:0.0:5.0 a v:5.0:5.0 (wynikającą z rozbicia Q:R=1)
    # Ta krawędź zapewnia połączenie odpowiadające dawnemu hiperwęzłowi Q:2.5:7.5.
    G.add_edge('v:0.0:5.0', 'v:5.0:5.0', label='E', B=0)

    return G


def determine_B(x1, y1, x2, y2, N, M):
    """
    Zwraca 1 jeśli krawędź jest na zewnętrznej granicy grafu, w przeciwnym razie 0.
    Granice to x=0, x=N, y=0, y=M.
    Jeżeli krawędź łączy węzły o takich samych współrzędnych brzegowych,
    tzn. jest to krawędź zewnętrzna.
    """
    # Sprawdzamy, czy oba węzły leżą na tej samej krawędzi zewnętrznej.
    if ((x1 == 0 and x2 == 0) or (x1 == N and x2 == N) or (y1 == 0 and y2 == 0) or (y1 == M and y2 == M)):
        return 1
    else:
        return 0

def cell_graph(G, base_x, base_y, cell_id, N, M):
    """
    Dodaje do grafu G jeden "kwadrat" i Q w środku.
    base_x, base_y - przesunięcie bazowe (całkowite) dla tej komórki.
    cell_id - unikalny identyfikator komórki (np. 'i_j').
    N, M - wymiary całej siatki (N w poziomie, M w pionie).
    """
    v1_name = f"v:{base_x}:{base_y}"
    v2_name = f"v:{base_x+1}:{base_y}"
    v3_name = f"v:{base_x+1}:{base_y+1}"
    v4_name = f"v:{base_x}:{base_y+1}"
    q_name = f"Q:{cell_id}"

    # Dodajemy wierzchołki
    G.add_node(q_name, label='Q', R=1)
    G.add_node(v1_name, label='v', x=float(base_x),   y=float(base_y),   h=0)
    G.add_node(v2_name, label='v', x=float(base_x+1), y=float(base_y),   h=0)
    G.add_node(v3_name, label='v', x=float(base_x+1), y=float(base_y+1), h=0)
    G.add_node(v4_name, label='v', x=float(base_x),   y=float(base_y+1), h=0)

    # Funkcja pomocnicza do dodawania krawędzi z odpowiednim B
    def add_square_edge(u,v):
        x1, y1 = (G.nodes[u]['x'], G.nodes[u]['y'])
        x2, y2 = (G.nodes[v]['x'], G.nodes[v]['y'])
        B_val = determine_B(x1, y1, x2, y2, N, M)
        G.add_edge(u, v, label='E', B=B_val)

    # Dodajemy krawędzie kwadratu
    add_square_edge(v1_name, v2_name)
    add_square_edge(v2_name, v3_name)
    add_square_edge(v3_name, v4_name)
    add_square_edge(v4_name, v1_name)

    # Dodajemy krawędzie od Q do wierzchołków kwadratu (te nie mają label='E', więc bez B)
    G.add_edge(q_name, v1_name)
    G.add_edge(q_name, v2_name)
    G.add_edge(q_name, v3_name)
    G.add_edge(q_name, v4_name)

def big_graph(N=3, M=3):
    """
    Tworzy duży graf N x M "komórek".
    Każda komórka to kwadrat z Q w środku, o wymiarach 1x1, 
    współrzędne wierzchołków od (0,0) do (N,M).
    """
    G = nx.Graph()

    for i in range(M):
        for j in range(N):
            cell_id = f"{i}_{j}"
            cell_graph(G, j, i, cell_id, N, M)

    return G



def valid_graph_p5() -> nx.Graph:
    G = nx.Graph()

    # Add nodes
    G.add_node('v:0:0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1:0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1:1', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0:1', label='v', x=0.0, y=1.0, h=0)
    G.add_node('Q:0_1', label='Q', R=1)
    G.add_node('v:2:0', label='v', x=2.0, y=0.0, h=0)
    G.add_node('v:2:1', label='v', x=2.0, y=1.0, h=0)
    G.add_node('v:3:0', label='v', x=3.0, y=0.0, h=0)
    G.add_node('v:3:1', label='v', x=3.0, y=1.0, h=0)
    G.add_node('Q:1_0', label='Q', R=1)
    G.add_node('v:1:2', label='v', x=1.0, y=2.0, h=0)
    G.add_node('v:0:2', label='v', x=0.0, y=2.0, h=0)
    G.add_node('v:2:2', label='v', x=2.0, y=2.0, h=0)
    G.add_node('Q:1_2', label='Q', R=1)
    G.add_node('v:3:2', label='v', x=3.0, y=2.0, h=0)
    G.add_node('Q:2_0', label='Q', R=1)
    G.add_node('v:1:3', label='v', x=1.0, y=3.0, h=0)
    G.add_node('v:0:3', label='v', x=0.0, y=3.0, h=0)
    G.add_node('Q:2_1', label='Q', R=1)
    G.add_node('v:2:3', label='v', x=2.0, y=3.0, h=0)
    G.add_node('Q:2_2', label='Q', R=1)
    G.add_node('v:3:3', label='v', x=3.0, y=3.0, h=0)
    G.add_node('v:0.5:0.0', label='v', x=0.5, y=0.0, h=0)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=0)
    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=1)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.5:0.5', label='v', x=0.5, y=0.5, h=0)
    G.add_node('Q:0.25:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.75', label='Q', R=0)
    G.add_node('Q:0.25:0.75', label='Q', R=0)
    G.add_node('v:2.5:0.0', label='v', x=2.5, y=0.0, h=0)
    G.add_node('v:2.0:0.5', label='v', x=2.0, y=0.5, h=1)
    G.add_node('v:3.0:0.5', label='v', x=3.0, y=0.5, h=0)
    G.add_node('v:2.5:1.0', label='v', x=2.5, y=1.0, h=1)
    G.add_node('v:2.5:0.5', label='v', x=2.5, y=0.5, h=0)
    G.add_node('Q:2.25:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.75', label='Q', R=0)
    G.add_node('Q:2.25:0.75', label='Q', R=0)
    G.add_node('v:1.5:1.0', label='v', x=1.5, y=1.0, h=1)
    G.add_node('v:1.0:1.5', label='v', x=1.0, y=1.5, h=1)
    G.add_node('v:2.0:1.5', label='v', x=2.0, y=1.5, h=1)
    G.add_node('v:1.5:2.0', label='v', x=1.5, y=2.0, h=1)
    G.add_node('v:1.5:1.5', label='v', x=1.5, y=1.5, h=0)
    G.add_node('Q:1.25:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.75', label='Q', R=0)
    G.add_node('Q:1.25:1.75', label='Q', R=0)
    
    
    # Add edges (including attributes)
    # Just follow the data you provided. For edges with 'label':'E' and 'B', include them. 
    # For edges to Q (with no attributes), just add them.

    G.add_edge('v:0:0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:0:0', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0:0', 'Q:0.25:0.25')
    G.add_edge('v:1:0', 'v:2:0', label='E', B=1)
    G.add_edge('v:1:0', 'Q:0_1')
    G.add_edge('v:1:0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:1:0', 'v:1.0:0.5', label='E', B=0)
    G.add_edge('v:1:0', 'Q:0.75:0.25')
    G.add_edge('v:1:1', 'Q:0_1')
    G.add_edge('v:1:1', 'Q:1_0')
    G.add_edge('v:1:1', 'v:1.0:0.5', label='E', B=0)
    G.add_edge('v:1:1', 'v:0.5:1.0', label='E', B=0)
    G.add_edge('v:1:1', 'Q:0.75:0.75')
    G.add_edge('v:1:1', 'v:1.5:1.0', label='E', B=0)
    G.add_edge('v:1:1', 'v:1.0:1.5', label='E', B=0)
    G.add_edge('v:1:1', 'Q:1.25:1.25')
    G.add_edge('v:0:1', 'v:0:2', label='E', B=1)
    G.add_edge('v:0:1', 'Q:1_0')
    G.add_edge('v:0:1', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0:1', 'v:0.5:1.0', label='E', B=0)
    G.add_edge('v:0:1', 'Q:0.25:0.75')
    G.add_edge('Q:0_1', 'v:2:0')
    G.add_edge('Q:0_1', 'v:2:1')
    G.add_edge('v:2:0', 'v:2.5:0.0', label='E', B=1)
    G.add_edge('v:2:0', 'v:2.0:0.5', label='E', B=0)
    G.add_edge('v:2:0', 'Q:2.25:0.25')
    G.add_edge('v:2:1', 'Q:1_2')
    G.add_edge('v:2:1', 'v:2.0:0.5', label='E', B=0)
    G.add_edge('v:2:1', 'v:2.5:1.0', label='E', B=0)
    G.add_edge('v:2:1', 'Q:2.25:0.75')
    G.add_edge('v:2:1', 'v:1.5:1.0', label='E', B=0)
    G.add_edge('v:2:1', 'v:2.0:1.5', label='E', B=0)
    G.add_edge('v:2:1', 'Q:1.75:1.25')
    G.add_edge('v:3:0', 'v:2.5:0.0', label='E', B=1)
    G.add_edge('v:3:0', 'v:3.0:0.5', label='E', B=1)
    G.add_edge('v:3:0', 'Q:2.75:0.25')
    G.add_edge('v:3:1', 'v:3:2', label='E', B=1)
    G.add_edge('v:3:1', 'Q:1_2')
    G.add_edge('v:3:1', 'v:3.0:0.5', label='E', B=1)
    G.add_edge('v:3:1', 'v:2.5:1.0', label='E', B=0)
    G.add_edge('v:3:1', 'Q:2.75:0.75')
    G.add_edge('Q:1_0', 'v:1:2')
    G.add_edge('Q:1_0', 'v:0:2')
    G.add_edge('v:1:2', 'v:0:2', label='E', B=0)
    G.add_edge('v:1:2', 'v:1:3', label='E', B=0)
    G.add_edge('v:1:2', 'Q:2_0')
    G.add_edge('v:1:2', 'Q:2_1')
    G.add_edge('v:1:2', 'v:1.0:1.5', label='E', B=0)
    G.add_edge('v:1:2', 'v:1.5:2.0', label='E', B=0)
    G.add_edge('v:1:2', 'Q:1.25:1.75')
    G.add_edge('v:0:2', 'v:0:3', label='E', B=1)
    G.add_edge('v:0:2', 'Q:2_0')
    G.add_edge('v:2:2', 'v:3:2', label='E', B=0)
    G.add_edge('v:2:2', 'Q:1_2')
    G.add_edge('v:2:2', 'v:2:3', label='E', B=0)
    G.add_edge('v:2:2', 'Q:2_1')
    G.add_edge('v:2:2', 'Q:2_2')
    G.add_edge('v:2:2', 'v:2.0:1.5', label='E', B=0)
    G.add_edge('v:2:2', 'v:1.5:2.0', label='E', B=0)
    G.add_edge('v:2:2', 'Q:1.75:1.75')
    G.add_edge('Q:1_2', 'v:3:2')
    G.add_edge('v:3:2', 'v:3:3', label='E', B=1)
    G.add_edge('v:3:2', 'Q:2_2')
    G.add_edge('Q:2_0', 'v:1:3')
    G.add_edge('Q:2_0', 'v:0:3')
    G.add_edge('v:1:3', 'v:0:3', label='E', B=1)
    G.add_edge('v:1:3', 'v:2:3', label='E', B=1)
    G.add_edge('v:1:3', 'Q:2_1')
    G.add_edge('Q:2_1', 'v:2:3')
    G.add_edge('v:2:3', 'v:3:3', label='E', B=1)
    G.add_edge('v:2:3', 'Q:2_2')
    G.add_edge('Q:2_2', 'v:3:3')
    G.add_edge('v:0.5:0.0', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.5:0.0', 'Q:0.25:0.25')
    G.add_edge('v:0.5:0.0', 'Q:0.75:0.25')
    G.add_edge('v:0.0:0.5', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.0:0.5', 'Q:0.25:0.25')
    G.add_edge('v:0.0:0.5', 'Q:0.25:0.75')
    G.add_edge('v:1.0:0.5', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:1.0:0.5', 'Q:0.75:0.25')
    G.add_edge('v:1.0:0.5', 'Q:0.75:0.75')
    G.add_edge('v:0.5:1.0', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.5:1.0', 'Q:0.75:0.75')
    G.add_edge('v:0.5:1.0', 'Q:0.25:0.75')
    G.add_edge('v:0.5:0.5', 'Q:0.25:0.25')
    G.add_edge('v:0.5:0.5', 'Q:0.75:0.25')
    G.add_edge('v:0.5:0.5', 'Q:0.75:0.75')
    G.add_edge('v:0.5:0.5', 'Q:0.25:0.75')
    G.add_edge('v:2.5:0.0', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:2.5:0.0', 'Q:2.25:0.25')
    G.add_edge('v:2.5:0.0', 'Q:2.75:0.25')
    G.add_edge('v:2.0:0.5', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:2.0:0.5', 'Q:2.25:0.25')
    G.add_edge('v:2.0:0.5', 'Q:2.25:0.75')
    G.add_edge('v:3.0:0.5', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:3.0:0.5', 'Q:2.75:0.25')
    G.add_edge('v:3.0:0.5', 'Q:2.75:0.75')
    G.add_edge('v:2.5:1.0', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:2.5:1.0', 'Q:2.75:0.75')
    G.add_edge('v:2.5:1.0', 'Q:2.25:0.75')
    G.add_edge('v:2.5:0.5', 'Q:2.25:0.25')
    G.add_edge('v:2.5:0.5', 'Q:2.75:0.25')
    G.add_edge('v:2.5:0.5', 'Q:2.75:0.75')
    G.add_edge('v:2.5:0.5', 'Q:2.25:0.75')
    G.add_edge('v:1.5:1.0', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:1.5:1.0', 'Q:1.25:1.25')
    G.add_edge('v:1.5:1.0', 'Q:1.75:1.25')
    G.add_edge('v:1.0:1.5', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:1.0:1.5', 'Q:1.25:1.25')
    G.add_edge('v:1.0:1.5', 'Q:1.25:1.75')
    G.add_edge('v:2.0:1.5', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:2.0:1.5', 'Q:1.75:1.25')
    G.add_edge('v:2.0:1.5', 'Q:1.75:1.75')
    G.add_edge('v:1.5:2.0', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:1.5:2.0', 'Q:1.75:1.75')
    G.add_edge('v:1.5:2.0', 'Q:1.25:1.75')
    G.add_edge('v:1.5:1.5', 'Q:1.25:1.25')
    G.add_edge('v:1.5:1.5', 'Q:1.75:1.25')
    G.add_edge('v:1.5:1.5', 'Q:1.75:1.75')
    G.add_edge('v:1.5:1.5', 'Q:1.25:1.75')

    return G

def big_graph_2_h_nodes() -> nx.Graph:
    G = nx.Graph()

    # Add nodes
    G.add_node('v:0:0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1:0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1:1', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0:1', label='v', x=0.0, y=1.0, h=0)
    G.add_node('v:2:0', label='v', x=2.0, y=0.0, h=0)
    G.add_node('v:2:1', label='v', x=2.0, y=1.0, h=0)
    G.add_node('Q:0_2', label='Q', R=1)
    G.add_node('v:3:0', label='v', x=3.0, y=0.0, h=0)
    G.add_node('v:3:1', label='v', x=3.0, y=1.0, h=0)
    G.add_node('Q:1_0', label='Q', R=1)
    G.add_node('v:1:2', label='v', x=1.0, y=2.0, h=0)
    G.add_node('v:0:2', label='v', x=0.0, y=2.0, h=0)
    G.add_node('Q:1_1', label='Q', R=1)
    G.add_node('v:2:2', label='v', x=2.0, y=2.0, h=0)
    G.add_node('v:3:2', label='v', x=3.0, y=2.0, h=0)
    G.add_node('Q:2_0', label='Q', R=1)
    G.add_node('v:1:3', label='v', x=1.0, y=3.0, h=0)
    G.add_node('v:0:3', label='v', x=0.0, y=3.0, h=0)
    G.add_node('Q:2_1', label='Q', R=1)
    G.add_node('v:2:3', label='v', x=2.0, y=3.0, h=0)
    G.add_node('Q:2_2', label='Q', R=1)
    G.add_node('v:3:3', label='v', x=3.0, y=3.0, h=0)
    G.add_node('v:0.5:0.0', label='v', x=0.5, y=0.0, h=0)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=0)
    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=0)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.5:0.5', label='v', x=0.5, y=0.5, h=0)
    G.add_node('Q:0.25:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.75', label='Q', R=0)
    G.add_node('Q:0.25:0.75', label='Q', R=0)
    G.add_node('v:1.5:0.0', label='v', x=1.5, y=0.0, h=0)
    G.add_node('v:2.0:0.5', label='v', x=2.0, y=0.5, h=1)
    G.add_node('v:1.5:1.0', label='v', x=1.5, y=1.0, h=1)
    G.add_node('v:1.5:0.5', label='v', x=1.5, y=0.5, h=0)
    G.add_node('Q:1.25:0.25', label='Q', R=0)
    G.add_node('Q:1.75:0.25', label='Q', R=0)
    G.add_node('Q:1.75:0.75', label='Q', R=0)
    G.add_node('Q:1.25:0.75', label='Q', R=0)
    G.add_node('v:2.5:1.0', label='v', x=2.5, y=1.0, h=1)
    G.add_node('v:2.0:1.5', label='v', x=2.0, y=1.5, h=1)
    G.add_node('v:3.0:1.5', label='v', x=3.0, y=1.5, h=0)
    G.add_node('v:2.5:2.0', label='v', x=2.5, y=2.0, h=1)
    G.add_node('v:2.5:1.5', label='v', x=2.5, y=1.5, h=0)
    G.add_node('Q:2.25:1.25', label='Q', R=0)
    G.add_node('Q:2.75:1.25', label='Q', R=0)
    G.add_node('Q:2.25:1.75', label='Q', R=0)
    G.add_node('Q:2.75:1.75', label='Q', R=0)

    # Add edges
    G.add_edge('v:0:0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:0:0', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0:0', 'Q:0.25:0.25')

    G.add_edge('v:1:0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:1:0', 'v:1.0:0.5', label='E', B=0)
    G.add_edge('v:1:0', 'Q:0.75:0.25')
    G.add_edge('v:1:0', 'v:1.5:0.0', label='E', B=1)
    G.add_edge('v:1:0', 'Q:1.25:0.25')

    G.add_edge('v:1:1', 'v:1:2', label='E', B=0)
    G.add_edge('v:1:1', 'Q:1_0')
    G.add_edge('v:1:1', 'Q:1_1')
    G.add_edge('v:1:1', 'v:1.0:0.5', label='E', B=0)
    G.add_edge('v:1:1', 'v:0.5:1.0', label='E', B=0)
    G.add_edge('v:1:1', 'Q:0.75:0.75')
    G.add_edge('v:1:1', 'v:1.5:1.0', label='E', B=0)
    G.add_edge('v:1:1', 'Q:1.25:0.75')

    G.add_edge('v:0:1', 'v:0:2', label='E', B=1)
    G.add_edge('v:0:1', 'Q:1_0')
    G.add_edge('v:0:1', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0:1', 'v:0.5:1.0', label='E', B=0)
    G.add_edge('v:0:1', 'Q:0.25:0.75')

    G.add_edge('v:2:0', 'v:3:0', label='E', B=1)
    G.add_edge('v:2:0', 'Q:0_2')
    G.add_edge('v:2:0', 'v:1.5:0.0', label='E', B=1)
    G.add_edge('v:2:0', 'v:2.0:0.5', label='E', B=0)
    G.add_edge('v:2:0', 'Q:1.75:0.25')

    G.add_edge('v:2:1', 'Q:0_2')
    G.add_edge('v:2:1', 'Q:1_1')
    G.add_edge('v:2:1', 'v:2.0:0.5', label='E', B=0)
    G.add_edge('v:2:1', 'v:1.5:1.0', label='E', B=0)
    G.add_edge('v:2:1', 'Q:1.75:0.75')
    G.add_edge('v:2:1', 'v:2.5:1.0', label='E', B=0)
    G.add_edge('v:2:1', 'v:2.0:1.5', label='E', B=0)
    G.add_edge('v:2:1', 'Q:2.25:1.25')

    G.add_edge('Q:0_2', 'v:3:0')
    G.add_edge('Q:0_2', 'v:3:1')
    G.add_edge('v:3:0', 'v:3:1', label='E', B=1)
    G.add_edge('v:3:1', 'v:2.5:1.0', label='E', B=0)
    G.add_edge('v:3:1', 'v:3.0:1.5', label='E', B=1)
    G.add_edge('v:3:1', 'Q:2.75:1.25')

    G.add_edge('Q:1_0', 'v:1:2')
    G.add_edge('Q:1_0', 'v:0:2')

    G.add_edge('v:1:2', 'v:0:2', label='E', B=0)
    G.add_edge('v:1:2', 'v:2:2', label='E', B=0)
    G.add_edge('v:1:2', 'Q:1_1')
    G.add_edge('v:1:2', 'v:1:3', label='E', B=0)
    G.add_edge('v:1:2', 'Q:2_0')
    G.add_edge('v:1:2', 'Q:2_1')

    G.add_edge('v:0:2', 'v:0:3', label='E', B=1)
    G.add_edge('v:0:2', 'Q:2_0')

    G.add_edge('Q:1_1', 'v:2:2')
    G.add_edge('v:2:2', 'v:2:3', label='E', B=0)
    G.add_edge('v:2:2', 'Q:2_1')
    G.add_edge('v:2:2', 'Q:2_2')
    G.add_edge('v:2:2', 'v:2.0:1.5', label='E', B=0)
    G.add_edge('v:2:2', 'v:2.5:2.0', label='E', B=0)
    G.add_edge('v:2:2', 'Q:2.25:1.75')

    G.add_edge('v:3:2', 'v:3:3', label='E', B=1)
    G.add_edge('v:3:2', 'Q:2_2')
    G.add_edge('v:3:2', 'v:3.0:1.5', label='E', B=1)
    G.add_edge('v:3:2', 'v:2.5:2.0', label='E', B=0)
    G.add_edge('v:3:2', 'Q:2.75:1.75')

    G.add_edge('Q:2_0', 'v:1:3')
    G.add_edge('Q:2_0', 'v:0:3')
    G.add_edge('v:1:3', 'v:0:3', label='E', B=1)
    G.add_edge('v:1:3', 'v:2:3', label='E', B=1)
    G.add_edge('v:1:3', 'Q:2_1')
    G.add_edge('Q:2_1', 'v:2:3')
    G.add_edge('v:2:3', 'v:3:3', label='E', B=1)
    G.add_edge('v:2:3', 'Q:2_2')
    G.add_edge('Q:2_2', 'v:3:3')

    G.add_edge('v:0.5:0.0', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.5:0.0', 'Q:0.25:0.25')
    G.add_edge('v:0.5:0.0', 'Q:0.75:0.25')

    G.add_edge('v:0.0:0.5', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.0:0.5', 'Q:0.25:0.25')
    G.add_edge('v:0.0:0.5', 'Q:0.25:0.75')

    G.add_edge('v:1.0:0.5', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:1.0:0.5', 'Q:0.75:0.25')
    G.add_edge('v:1.0:0.5', 'Q:0.75:0.75')
    G.add_edge('v:1.0:0.5', 'v:1.5:0.5', label='E', B=0)
    G.add_edge('v:1.0:0.5', 'Q:1.25:0.25')
    G.add_edge('v:1.0:0.5', 'Q:1.25:0.75')

    G.add_edge('v:0.5:1.0', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.5:1.0', 'Q:0.75:0.75')
    G.add_edge('v:0.5:1.0', 'Q:0.25:0.75')
    G.add_edge('v:0.5:0.5', 'Q:0.25:0.25')
    G.add_edge('v:0.5:0.5', 'Q:0.75:0.25')
    G.add_edge('v:0.5:0.5', 'Q:0.75:0.75')
    G.add_edge('v:0.5:0.5', 'Q:0.25:0.75')

    G.add_edge('v:1.5:0.0', 'v:1.5:0.5', label='E', B=0)
    G.add_edge('v:1.5:0.0', 'Q:1.25:0.25')
    G.add_edge('v:1.5:0.0', 'Q:1.75:0.25')
    G.add_edge('v:2.0:0.5', 'v:1.5:0.5', label='E', B=0)
    G.add_edge('v:2.0:0.5', 'Q:1.75:0.25')
    G.add_edge('v:2.0:0.5', 'Q:1.75:0.75')
    G.add_edge('v:1.5:1.0', 'v:1.5:0.5', label='E', B=0)
    G.add_edge('v:1.5:1.0', 'Q:1.75:0.75')
    G.add_edge('v:1.5:1.0', 'Q:1.25:0.75')
    G.add_edge('v:1.5:0.5', 'Q:1.25:0.25')
    G.add_edge('v:1.5:0.5', 'Q:1.75:0.25')
    G.add_edge('v:1.5:0.5', 'Q:1.75:0.75')
    G.add_edge('v:1.5:0.5', 'Q:1.25:0.75')

    G.add_edge('v:2.5:1.0', 'v:2.5:1.5', label='E', B=0)
    G.add_edge('v:2.5:1.0', 'Q:2.25:1.25')
    G.add_edge('v:2.5:1.0', 'Q:2.75:1.25')
    G.add_edge('v:2.0:1.5', 'v:2.5:1.5', label='E', B=0)
    G.add_edge('v:2.0:1.5', 'Q:2.25:1.25')
    G.add_edge('v:2.0:1.5', 'Q:2.25:1.75')
    G.add_edge('v:3.0:1.5', 'v:2.5:1.5', label='E', B=0)
    G.add_edge('v:3.0:1.5', 'Q:2.75:1.25')
    G.add_edge('v:3.0:1.5', 'Q:2.75:1.75')
    G.add_edge('v:2.5:2.0', 'v:2.5:1.5', label='E', B=0)
    G.add_edge('v:2.5:2.0', 'Q:2.25:1.75')
    G.add_edge('v:2.5:2.0', 'Q:2.75:1.75')
    G.add_edge('v:2.5:1.5', 'Q:2.25:1.25')
    G.add_edge('v:2.5:1.5', 'Q:2.75:1.25')
    G.add_edge('v:2.5:1.5', 'Q:2.25:1.75')
    G.add_edge('v:2.5:1.5', 'Q:2.75:1.75')

    return G



def valid_graph_p6() -> nx.Graph:
    G = nx.Graph()

    # Add nodes
    G.add_node('v:0:0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1:0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1:1', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0:1', label='v', x=0.0, y=1.0, h=0)
    G.add_node('Q:0_1', label='Q', R=1)
    G.add_node('v:2:0', label='v', x=2.0, y=0.0, h=0)
    G.add_node('v:2:1', label='v', x=2.0, y=1.0, h=0)
    G.add_node('v:3:0', label='v', x=3.0, y=0.0, h=0)
    G.add_node('v:3:1', label='v', x=3.0, y=1.0, h=0)
    G.add_node('Q:1_0', label='Q', R=1)
    G.add_node('v:1:2', label='v', x=1.0, y=2.0, h=0)
    G.add_node('v:0:2', label='v', x=0.0, y=2.0, h=0)
    G.add_node('v:2:2', label='v', x=2.0, y=2.0, h=0)
    G.add_node('Q:1_2', label='Q', R=1)
    G.add_node('v:3:2', label='v', x=3.0, y=2.0, h=0)
    G.add_node('Q:2_0', label='Q', R=1)
    G.add_node('v:1:3', label='v', x=1.0, y=3.0, h=0)
    G.add_node('v:0:3', label='v', x=0.0, y=3.0, h=0)
    G.add_node('Q:2_1', label='Q', R=1)
    G.add_node('v:2:3', label='v', x=2.0, y=3.0, h=0)
    G.add_node('Q:2_2', label='Q', R=1)
    G.add_node('v:3:3', label='v', x=3.0, y=3.0, h=0)

    # Inner square (top-left)
    G.add_node('v:0.5:0.0', label='v', x=0.5, y=0.0, h=0)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=0)
    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=1)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.5:0.5', label='v', x=0.5, y=0.5, h=0)

    G.add_node('Q:0.25:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.75', label='Q', R=0)
    G.add_node('Q:0.25:0.75', label='Q', R=0)

    # Inner square (top-right)
    G.add_node('v:2.5:0.0', label='v', x=2.5, y=0.0, h=0)
    G.add_node('v:2.0:0.5', label='v', x=2.0, y=0.5, h=1)
    G.add_node('v:3.0:0.5', label='v', x=3.0, y=0.5, h=0)
    G.add_node('v:2.5:1.0', label='v', x=2.5, y=1.0, h=1)
    G.add_node('v:2.5:0.5', label='v', x=2.5, y=0.5, h=0)

    G.add_node('Q:2.25:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.75', label='Q', R=0)
    G.add_node('Q:2.25:0.75', label='Q', R=0)

    # Inner square (middle)
    G.add_node('v:1.5:1.0', label='v', x=1.5, y=1.0, h=1)
    G.add_node('v:1.0:1.5', label='v', x=1.0, y=1.5, h=1)
    G.add_node('v:2.0:1.5', label='v', x=2.0, y=1.5, h=1)
    G.add_node('v:1.5:2.0', label='v', x=1.5, y=2.0, h=1)
    G.add_node('v:1.5:1.5', label='v', x=1.5, y=1.5, h=0)

    G.add_node('Q:1.25:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.75', label='Q', R=0)
    G.add_node('Q:1.25:1.75', label='Q', R=0)

    # Bottom rectangle splitting into smaller square
    # Original bottom rectangle corners: (1.0,-1.0), (2.0,-1.0), (2.0,0.0), (1.0,0.0)
    # Corresponding node names we already have: 'v:1.0:-1.0', 'v:2.0:-1.0', 'v:1:0', 'v:2:0'
    G.add_node('v:1.0:-1.0', label='v', x=1.0, y=-1.0, h=0)
    G.add_node('v:2.0:-1.0', label='v', x=2.0, y=-1.0, h=0)
    # Top corners of this bottom square: v:1:0 and v:2:0 already exist above
    # Middle nodes in this bottom square
    G.add_node('v:1.5:-1.0', label='v', x=1.5, y=-1.0, h=0)
    G.add_node('v:1.0:-0.5', label='v', x=1.0, y=-0.5, h=0)
    G.add_node('v:2.0:-0.5', label='v', x=2.0, y=-0.5, h=0)
    G.add_node('v:1.5:-0.5', label='v', x=1.5, y=-0.5, h=0)
    G.add_node('v:1.5:0.0', label='v', x=1.5, y=0.0, h=1)

    # 4 Q nodes inside the bottom square
    G.add_node('Q:1.25:-0.75', label='Q', R=0)
    G.add_node('Q:1.75:-0.75', label='Q', R=0)
    G.add_node('Q:1.75:-0.25', label='Q', R=0)
    G.add_node('Q:1.25:-0.25', label='Q', R=0)

    # Connect corners to the closest Qs (bottom square)
    G.add_edge('v:1.0:-1.0', 'Q:1.25:-0.75')
    G.add_edge('v:2.0:-1.0', 'Q:1.75:-0.75')
    G.add_edge('v:2:0', 'Q:1.75:-0.25')
    G.add_edge('v:1:0', 'Q:1.25:-0.25')

    # Edges from intermediate v nodes to these Q nodes
    G.add_edge('v:1.5:-1.0', 'Q:1.25:-0.75')
    G.add_edge('v:1.5:-1.0', 'Q:1.75:-0.75')

    G.add_edge('v:1.0:-0.5', 'Q:1.25:-0.75')
    G.add_edge('v:1.0:-0.5', 'Q:1.25:-0.25')

    G.add_edge('v:2.0:-0.5', 'Q:1.75:-0.75')
    G.add_edge('v:2.0:-0.5', 'Q:1.75:-0.25')

    G.add_edge('v:1.5:0.0', 'Q:1.25:-0.25')
    G.add_edge('v:1.5:0.0', 'Q:1.75:-0.25')

    G.add_edge('v:1.5:-0.5', 'Q:1.25:-0.75')
    G.add_edge('v:1.5:-0.5', 'Q:1.75:-0.75')
    G.add_edge('v:1.5:-0.5', 'Q:1.75:-0.25')
    G.add_edge('v:1.5:-0.5', 'Q:1.25:-0.25')

    # Existing edges (from original code)
    G.add_edge('v:2.0:-1.0', 'v:2:0', label='E', B=0)
    G.add_edge('v:1.0:-1.0', 'v:1:0', label='E', B=0)
    G.add_edge('v:2.0:-1.0', 'v:1.0:-1.0', label='E', B=0)

    # Add edges for the other parts of the graph
    G.add_edge('v:0:0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:0:0', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0:0', 'Q:0.25:0.25')
    G.add_edge('v:1:0', 'v:1.5:0.0', label='E', B=0)
    G.add_edge('v:1.5:0.0', 'v:2:0', label='E', B=0)
    G.add_edge('v:1:0', 'Q:0_1')
    G.add_edge('v:1:0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:1:0', 'v:1.0:0.5', label='E', B=0)
    G.add_edge('v:1:0', 'Q:0.75:0.25')
    G.add_edge('v:1:1', 'Q:0_1')
    G.add_edge('v:1:1', 'Q:1_0')
    G.add_edge('v:1:1', 'v:1.0:0.5', label='E', B=0)
    G.add_edge('v:1:1', 'v:0.5:1.0', label='E', B=0)
    G.add_edge('v:1:1', 'Q:0.75:0.75')
    G.add_edge('v:1:1', 'v:1.5:1.0', label='E', B=0)
    G.add_edge('v:1:1', 'v:1.0:1.5', label='E', B=0)
    G.add_edge('v:1:1', 'Q:1.25:1.25')
    G.add_edge('v:0:1', 'v:0:2', label='E', B=1)
    G.add_edge('v:0:1', 'Q:1_0')
    G.add_edge('v:0:1', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0:1', 'v:0.5:1.0', label='E', B=0)
    G.add_edge('v:0:1', 'Q:0.25:0.75')
    G.add_edge('Q:0_1', 'v:2:0')
    G.add_edge('Q:0_1', 'v:2:1')
    G.add_edge('v:2:0', 'v:2.5:0.0', label='E', B=1)
    G.add_edge('v:2:0', 'v:2.0:0.5', label='E', B=0)
    G.add_edge('v:2:0', 'Q:2.25:0.25')
    G.add_edge('v:2:1', 'Q:1_2')
    G.add_edge('v:2:1', 'v:2.0:0.5', label='E', B=0)
    G.add_edge('v:2:1', 'v:2.5:1.0', label='E', B=0)
    G.add_edge('v:2:1', 'Q:2.25:0.75')
    G.add_edge('v:2:1', 'v:1.5:1.0', label='E', B=0)
    G.add_edge('v:2:1', 'v:2.0:1.5', label='E', B=0)
    G.add_edge('v:2:1', 'Q:1.75:1.25')
    G.add_edge('v:3:0', 'v:2.5:0.0', label='E', B=1)
    G.add_edge('v:3:0', 'v:3.0:0.5', label='E', B=1)
    G.add_edge('v:3:0', 'Q:2.75:0.25')
    G.add_edge('v:3:1', 'v:3:2', label='E', B=1)
    G.add_edge('v:3:1', 'Q:1_2')
    G.add_edge('v:3:1', 'v:3.0:0.5', label='E', B=1)
    G.add_edge('v:3:1', 'v:2.5:1.0', label='E', B=0)
    G.add_edge('v:3:1', 'Q:2.75:0.75')
    G.add_edge('Q:1_0', 'v:1:2')
    G.add_edge('Q:1_0', 'v:0:2')
    G.add_edge('v:1:2', 'v:0:2', label='E', B=0)
    G.add_edge('v:1:2', 'v:1:3', label='E', B=0)
    G.add_edge('v:1:2', 'Q:2_0')
    G.add_edge('v:1:2', 'Q:2_1')
    G.add_edge('v:1:2', 'v:1.0:1.5', label='E', B=0)
    G.add_edge('v:1:2', 'v:1.5:2.0', label='E', B=0)
    G.add_edge('v:1:2', 'Q:1.25:1.75')
    G.add_edge('v:0:2', 'v:0:3', label='E', B=1)
    G.add_edge('v:0:2', 'Q:2_0')
    G.add_edge('v:2:2', 'v:3:2', label='E', B=0)
    G.add_edge('v:2:2', 'Q:1_2')
    G.add_edge('v:2:2', 'v:2:3', label='E', B=0)
    G.add_edge('v:2:2', 'Q:2_1')
    G.add_edge('v:2:2', 'Q:2_2')
    G.add_edge('v:2:2', 'v:2.0:1.5', label='E', B=0)
    G.add_edge('v:2:2', 'v:1.5:2.0', label='E', B=0)
    G.add_edge('v:2:2', 'Q:1.75:1.75')
    G.add_edge('Q:1_2', 'v:3:2')
    G.add_edge('v:3:2', 'v:3:3', label='E', B=1)
    G.add_edge('v:3:2', 'Q:2_2')
    G.add_edge('Q:2_0', 'v:1:3')
    G.add_edge('Q:2_0', 'v:0:3')
    G.add_edge('v:1:3', 'v:0:3', label='E', B=1)
    G.add_edge('v:1:3', 'v:2:3', label='E', B=1)
    G.add_edge('v:1:3', 'Q:2_1')
    G.add_edge('Q:2_1', 'v:2:3')
    G.add_edge('v:2:3', 'v:3:3', label='E', B=1)
    G.add_edge('v:2:3', 'Q:2_2')
    G.add_edge('Q:2_2', 'v:3:3')

    G.add_edge('v:0.5:0.0', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.5:0.0', 'Q:0.25:0.25')
    G.add_edge('v:0.5:0.0', 'Q:0.75:0.25')
    G.add_edge('v:0.0:0.5', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.0:0.5', 'Q:0.25:0.25')
    G.add_edge('v:0.0:0.5', 'Q:0.25:0.75')
    G.add_edge('v:1.0:0.5', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:1.0:0.5', 'Q:0.75:0.25')
    G.add_edge('v:1.0:0.5', 'Q:0.75:0.75')
    G.add_edge('v:0.5:1.0', 'v:0.5:0.5', label='E', B=0)
    G.add_edge('v:0.5:1.0', 'Q:0.75:0.75')
    G.add_edge('v:0.5:1.0', 'Q:0.25:0.75')
    G.add_edge('v:0.5:0.5', 'Q:0.25:0.25')
    G.add_edge('v:0.5:0.5', 'Q:0.75:0.25')
    G.add_edge('v:0.5:0.5', 'Q:0.75:0.75')
    G.add_edge('v:0.5:0.5', 'Q:0.25:0.75')

    G.add_edge('v:2.5:0.0', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:2.5:0.0', 'Q:2.25:0.25')
    G.add_edge('v:2.5:0.0', 'Q:2.75:0.25')
    G.add_edge('v:2.0:0.5', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:2.0:0.5', 'Q:2.25:0.25')
    G.add_edge('v:2.0:0.5', 'Q:2.25:0.75')
    G.add_edge('v:3.0:0.5', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:3.0:0.5', 'Q:2.75:0.25')
    G.add_edge('v:3.0:0.5', 'Q:2.75:0.75')
    G.add_edge('v:2.5:1.0', 'v:2.5:0.5', label='E', B=0)
    G.add_edge('v:2.5:1.0', 'Q:2.75:0.75')
    G.add_edge('v:2.5:1.0', 'Q:2.25:0.75')
    G.add_edge('v:2.5:0.5', 'Q:2.25:0.25')
    G.add_edge('v:2.5:0.5', 'Q:2.75:0.25')
    G.add_edge('v:2.5:0.5', 'Q:2.75:0.75')
    G.add_edge('v:2.5:0.5', 'Q:2.25:0.75')

    G.add_edge('v:1.5:1.0', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:1.5:1.0', 'Q:1.25:1.25')
    G.add_edge('v:1.5:1.0', 'Q:1.75:1.25')
    G.add_edge('v:1.0:1.5', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:1.0:1.5', 'Q:1.25:1.25')
    G.add_edge('v:1.0:1.5', 'Q:1.25:1.75')
    G.add_edge('v:2.0:1.5', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:2.0:1.5', 'Q:1.75:1.25')
    G.add_edge('v:2.0:1.5', 'Q:1.75:1.75')
    G.add_edge('v:1.5:2.0', 'v:1.5:1.5', label='E', B=0)
    G.add_edge('v:1.5:2.0', 'Q:1.75:1.75')
    G.add_edge('v:1.5:2.0', 'Q:1.25:1.75')
    G.add_edge('v:1.5:1.5', 'Q:1.25:1.25')
    G.add_edge('v:1.5:1.5', 'Q:1.75:1.25')
    G.add_edge('v:1.5:1.5', 'Q:1.75:1.75')
    G.add_edge('v:1.5:1.5', 'Q:1.25:1.75')

    return G


def expected_graph_6():
    G = nx.Graph()

    # Add nodes with attributes
    G.add_node('v:0:0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1:0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1:1', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0:1', label='v', x=0.0, y=1.0, h=0)
    G.add_node('v:2:0', label='v', x=2.0, y=0.0, h=0)
    G.add_node('v:2:1', label='v', x=2.0, y=1.0, h=0)
    G.add_node('v:3:0', label='v', x=3.0, y=0.0, h=0)
    G.add_node('v:3:1', label='v', x=3.0, y=1.0, h=0)
    G.add_node('Q:1_0', label='Q', R=1)
    G.add_node('v:1:2', label='v', x=1.0, y=2.0, h=0)
    G.add_node('v:0:2', label='v', x=0.0, y=2.0, h=0)
    G.add_node('v:2:2', label='v', x=2.0, y=2.0, h=0)
    G.add_node('Q:1_2', label='Q', R=1)
    G.add_node('v:3:2', label='v', x=3.0, y=2.0, h=0)
    G.add_node('Q:2_0', label='Q', R=1)
    G.add_node('v:1:3', label='v', x=1.0, y=3.0, h=0)
    G.add_node('v:0:3', label='v', x=0.0, y=3.0, h=0)
    G.add_node('Q:2_1', label='Q', R=1)
    G.add_node('v:2:3', label='v', x=2.0, y=3.0, h=0)
    G.add_node('Q:2_2', label='Q', R=1)
    G.add_node('v:3:3', label='v', x=3.0, y=3.0, h=0)
    G.add_node('v:0.5:0.0', label='v', x=0.5, y=0.0, h=0)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=0)
    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=0)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.5:0.5', label='v', x=0.5, y=0.5, h=0)
    G.add_node('Q:0.25:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.75', label='Q', R=0)
    G.add_node('Q:0.25:0.75', label='Q', R=0)
    G.add_node('v:2.5:0.0', label='v', x=2.5, y=0.0, h=0)
    G.add_node('v:2.0:0.5', label='v', x=2.0, y=0.5, h=0)
    G.add_node('v:3.0:0.5', label='v', x=3.0, y=0.5, h=0)
    G.add_node('v:2.5:1.0', label='v', x=2.5, y=1.0, h=1)
    G.add_node('v:2.5:0.5', label='v', x=2.5, y=0.5, h=0)
    G.add_node('Q:2.25:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.75', label='Q', R=0)
    G.add_node('Q:2.25:0.75', label='Q', R=0)
    G.add_node('v:1.5:1.0', label='v', x=1.5, y=1.0, h=0)
    G.add_node('v:1.0:1.5', label='v', x=1.0, y=1.5, h=1)
    G.add_node('v:2.0:1.5', label='v', x=2.0, y=1.5, h=1)
    G.add_node('v:1.5:2.0', label='v', x=1.5, y=2.0, h=1)
    G.add_node('v:1.5:1.5', label='v', x=1.5, y=1.5, h=0)
    G.add_node('Q:1.25:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.75', label='Q', R=0)
    G.add_node('Q:1.25:1.75', label='Q', R=0)
    G.add_node('v:1.0:-1.0', label='v', x=1.0, y=-1.0, h=0)
    G.add_node('v:2.0:-1.0', label='v', x=2.0, y=-1.0, h=0)
    G.add_node('v:1.5:-1.0', label='v', x=1.5, y=-1.0, h=0)
    G.add_node('v:1.0:-0.5', label='v', x=1.0, y=-0.5, h=0)
    G.add_node('v:2.0:-0.5', label='v', x=2.0, y=-0.5, h=0)
    G.add_node('v:1.5:-0.5', label='v', x=1.5, y=-0.5, h=0)
    G.add_node('v:1.5:0.0', label='v', x=1.5, y=0.0, h=0)
    G.add_node('Q:1.25:-0.75', label='Q', R=0)
    G.add_node('Q:1.75:-0.75', label='Q', R=0)
    G.add_node('Q:1.75:-0.25', label='Q', R=0)
    G.add_node('Q:1.25:-0.25', label='Q', R=0)
    G.add_node('v:1.5:0.5', label='v', x=1.5, y=0.5, h=0)
    G.add_node('Q:1.25:0.25', label='Q', R=0)
    G.add_node('Q:1.25:0.75', label='Q', R=0)
    G.add_node('Q:1.75:0.25', label='Q', R=0)
    G.add_node('Q:1.75:0.75', label='Q', R=0)

    # Add edges with attributes
    # For edges with empty attributes, just add without attributes.
    # For edges with 'label': 'E', 'B': something, add those attributes as well.

    edges = [
        ('v:0:0', 'v:0.5:0.0', {'label':'E','B':1}),
        ('v:0:0', 'v:0.0:0.5', {'label':'E','B':1}),
        ('v:0:0', 'Q:0.25:0.25', {}),
        ('v:1:0', 'Q:1.25:-0.25', {}),
        ('v:1:0', 'v:1.0:-1.0', {'label':'E','B':0}),
        ('v:1:0', 'v:1.5:0.0', {'label':'E','B':0}),
        ('v:1:0', 'v:0.5:0.0', {'label':'E','B':1}),
        ('v:1:0', 'v:1.0:0.5', {'label':'E','B':0}),
        ('v:1:0', 'Q:0.75:0.25', {}),
        ('v:1:0', 'Q:1.25:0.25', {}),
        ('v:1:1', 'Q:1_0', {}),
        ('v:1:1', 'v:1.0:0.5', {'label':'E','B':0}),
        ('v:1:1', 'v:0.5:1.0', {'label':'E','B':0}),
        ('v:1:1', 'Q:0.75:0.75', {}),
        ('v:1:1', 'v:1.5:1.0', {'label':'E','B':0}),
        ('v:1:1', 'v:1.0:1.5', {'label':'E','B':0}),
        ('v:1:1', 'Q:1.25:1.25', {}),
        ('v:1:1', 'Q:1.25:0.75', {}),
        ('v:0:1', 'v:0:2', {'label':'E','B':1}),
        ('v:0:1', 'Q:1_0', {}),
        ('v:0:1', 'v:0.0:0.5', {'label':'E','B':1}),
        ('v:0:1', 'v:0.5:1.0', {'label':'E','B':0}),
        ('v:0:1', 'Q:0.25:0.75', {}),
        ('v:2:0', 'Q:1.75:-0.25', {}),
        ('v:2:0', 'v:2.0:-1.0', {'label':'E','B':0}),
        ('v:2:0', 'v:1.5:0.0', {'label':'E','B':0}),
        ('v:2:0', 'v:2.5:0.0', {'label':'E','B':1}),
        ('v:2:0', 'v:2.0:0.5', {'label':'E','B':0}),
        ('v:2:0', 'Q:2.25:0.25', {}),
        ('v:2:0', 'Q:1.75:0.25', {}),
        ('v:2:1', 'Q:1_2', {}),
        ('v:2:1', 'v:2.0:0.5', {'label':'E','B':0}),
        ('v:2:1', 'v:2.5:1.0', {'label':'E','B':0}),
        ('v:2:1', 'Q:2.25:0.75', {}),
        ('v:2:1', 'v:1.5:1.0', {'label':'E','B':0}),
        ('v:2:1', 'v:2.0:1.5', {'label':'E','B':0}),
        ('v:2:1', 'Q:1.75:1.25', {}),
        ('v:2:1', 'Q:1.75:0.75', {}),
        ('v:3:0', 'v:2.5:0.0', {'label':'E','B':1}),
        ('v:3:0', 'v:3.0:0.5', {'label':'E','B':1}),
        ('v:3:0', 'Q:2.75:0.25', {}),
        ('v:3:1', 'v:3:2', {'label':'E','B':1}),
        ('v:3:1', 'Q:1_2', {}),
        ('v:3:1', 'v:3.0:0.5', {'label':'E','B':1}),
        ('v:3:1', 'v:2.5:1.0', {'label':'E','B':0}),
        ('v:3:1', 'Q:2.75:0.75', {}),
        ('Q:1_0', 'v:1:2', {}),
        ('Q:1_0', 'v:0:2', {}),
        ('v:1:2', 'v:0:2', {'label':'E','B':0}),
        ('v:1:2', 'v:1:3', {'label':'E','B':0}),
        ('v:1:2', 'Q:2_0', {}),
        ('v:1:2', 'Q:2_1', {}),
        ('v:1:2', 'v:1.0:1.5', {'label':'E','B':0}),
        ('v:1:2', 'v:1.5:2.0', {'label':'E','B':0}),
        ('v:1:2', 'Q:1.25:1.75', {}),
        ('v:0:2', 'v:0:3', {'label':'E','B':1}),
        ('v:0:2', 'Q:2_0', {}),
        ('v:2:2', 'v:3:2', {'label':'E','B':0}),
        ('v:2:2', 'Q:1_2', {}),
        ('v:2:2', 'v:2:3', {'label':'E','B':0}),
        ('v:2:2', 'Q:2_1', {}),
        ('v:2:2', 'Q:2_2', {}),
        ('v:2:2', 'v:2.0:1.5', {'label':'E','B':0}),
        ('v:2:2', 'v:1.5:2.0', {'label':'E','B':0}),
        ('v:2:2', 'Q:1.75:1.75', {}),
        ('Q:1_2', 'v:3:2', {}),
        ('v:3:2', 'v:3:3', {'label':'E','B':1}),
        ('v:3:2', 'Q:2_2', {}),
        ('Q:2_0', 'v:1:3', {}),
        ('Q:2_0', 'v:0:3', {}),
        ('v:1:3', 'v:0:3', {'label':'E','B':1}),
        ('v:1:3', 'v:2:3', {'label':'E','B':1}),
        ('v:1:3', 'Q:2_1', {}),
        ('Q:2_1', 'v:2:3', {}),
        ('v:2:3', 'v:3:3', {'label':'E','B':1}),
        ('v:2:3', 'Q:2_2', {}),
        ('Q:2_2', 'v:3:3', {}),
        ('v:0.5:0.0', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:0.5:0.0', 'Q:0.25:0.25', {}),
        ('v:0.5:0.0', 'Q:0.75:0.25', {}),
        ('v:0.0:0.5', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:0.0:0.5', 'Q:0.25:0.25', {}),
        ('v:0.0:0.5', 'Q:0.25:0.75', {}),
        ('v:1.0:0.5', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:1.0:0.5', 'Q:0.75:0.25', {}),
        ('v:1.0:0.5', 'Q:0.75:0.75', {}),
        ('v:1.0:0.5', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:1.0:0.5', 'Q:1.25:0.25', {}),
        ('v:1.0:0.5', 'Q:1.25:0.75', {}),
        ('v:0.5:1.0', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:0.5:1.0', 'Q:0.75:0.75', {}),
        ('v:0.5:1.0', 'Q:0.25:0.75', {}),
        ('v:0.5:0.5', 'Q:0.25:0.25', {}),
        ('v:0.5:0.5', 'Q:0.75:0.25', {}),
        ('v:0.5:0.5', 'Q:0.75:0.75', {}),
        ('v:0.5:0.5', 'Q:0.25:0.75', {}),
        ('v:2.5:0.0', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:2.5:0.0', 'Q:2.25:0.25', {}),
        ('v:2.5:0.0', 'Q:2.75:0.25', {}),
        ('v:2.0:0.5', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:2.0:0.5', 'Q:2.25:0.25', {}),
        ('v:2.0:0.5', 'Q:2.25:0.75', {}),
        ('v:2.0:0.5', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:2.0:0.5', 'Q:1.75:0.25', {}),
        ('v:2.0:0.5', 'Q:1.75:0.75', {}),
        ('v:3.0:0.5', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:3.0:0.5', 'Q:2.75:0.25', {}),
        ('v:3.0:0.5', 'Q:2.75:0.75', {}),
        ('v:2.5:1.0', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:2.5:1.0', 'Q:2.75:0.75', {}),
        ('v:2.5:1.0', 'Q:2.25:0.75', {}),
        ('v:2.5:0.5', 'Q:2.25:0.25', {}),
        ('v:2.5:0.5', 'Q:2.75:0.25', {}),
        ('v:2.5:0.5', 'Q:2.75:0.75', {}),
        ('v:2.5:0.5', 'Q:2.25:0.75', {}),
        ('v:1.5:1.0', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:1.5:1.0', 'Q:1.25:1.25', {}),
        ('v:1.5:1.0', 'Q:1.75:1.25', {}),
        ('v:1.5:1.0', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:1.5:1.0', 'Q:1.25:0.75', {}),
        ('v:1.5:1.0', 'Q:1.75:0.75', {}),
        ('v:1.0:1.5', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:1.0:1.5', 'Q:1.25:1.25', {}),
        ('v:1.0:1.5', 'Q:1.25:1.75', {}),
        ('v:2.0:1.5', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:2.0:1.5', 'Q:1.75:1.25', {}),
        ('v:2.0:1.5', 'Q:1.75:1.75', {}),
        ('v:1.5:2.0', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:1.5:2.0', 'Q:1.75:1.75', {}),
        ('v:1.5:2.0', 'Q:1.25:1.75', {}),
        ('v:1.5:1.5', 'Q:1.25:1.25', {}),
        ('v:1.5:1.5', 'Q:1.75:1.25', {}),
        ('v:1.5:1.5', 'Q:1.75:1.75', {}),
        ('v:1.5:1.5', 'Q:1.25:1.75', {}),
        ('v:1.0:-1.0', 'Q:1.25:-0.75', {}),
        ('v:1.0:-1.0', 'v:2.0:-1.0', {'label':'E','B':0}),
        ('v:2.0:-1.0', 'Q:1.75:-0.75', {}),
        ('v:1.5:-1.0', 'Q:1.25:-0.75', {}),
        ('v:1.5:-1.0', 'Q:1.75:-0.75', {}),
        ('v:1.0:-0.5', 'Q:1.25:-0.75', {}),
        ('v:1.0:-0.5', 'Q:1.25:-0.25', {}),
        ('v:2.0:-0.5', 'Q:1.75:-0.75', {}),
        ('v:2.0:-0.5', 'Q:1.75:-0.25', {}),
        ('v:1.5:-0.5', 'Q:1.25:-0.75', {}),
        ('v:1.5:-0.5', 'Q:1.75:-0.75', {}),
        ('v:1.5:-0.5', 'Q:1.75:-0.25', {}),
        ('v:1.5:-0.5', 'Q:1.25:-0.25', {}),
        ('v:1.5:0.0', 'Q:1.25:-0.25', {}),
        ('v:1.5:0.0', 'Q:1.75:-0.25', {}),
        ('v:1.5:0.0', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:1.5:0.0', 'Q:1.25:0.25', {}),
        ('v:1.5:0.0', 'Q:1.75:0.25', {}),
        ('v:1.5:0.5', 'Q:1.25:0.25', {}),
        ('v:1.5:0.5', 'Q:1.25:0.75', {}),
        ('v:1.5:0.5', 'Q:1.75:0.25', {}),
        ('v:1.5:0.5', 'Q:1.75:0.75', {})
    ]

    for u,v,attr in edges:
        G.add_edge(u,v,**attr)

    return G



def expected_graph_5():
    G = nx.Graph()

    # Add nodes with attributes
    G.add_node('v:0:0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1:0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1:1', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0:1', label='v', x=0.0, y=1.0, h=0)
    G.add_node('v:2:0', label='v', x=2.0, y=0.0, h=0)
    G.add_node('v:2:1', label='v', x=2.0, y=1.0, h=0)
    G.add_node('v:3:0', label='v', x=3.0, y=0.0, h=0)
    G.add_node('v:3:1', label='v', x=3.0, y=1.0, h=0)
    G.add_node('Q:1_0', label='Q', R=1)
    G.add_node('v:1:2', label='v', x=1.0, y=2.0, h=0)
    G.add_node('v:0:2', label='v', x=0.0, y=2.0, h=0)
    G.add_node('v:2:2', label='v', x=2.0, y=2.0, h=0)
    G.add_node('Q:1_2', label='Q', R=1)
    G.add_node('v:3:2', label='v', x=3.0, y=2.0, h=0)
    G.add_node('Q:2_0', label='Q', R=1)
    G.add_node('v:1:3', label='v', x=1.0, y=3.0, h=0)
    G.add_node('v:0:3', label='v', x=0.0, y=3.0, h=0)
    G.add_node('Q:2_1', label='Q', R=1)
    G.add_node('v:2:3', label='v', x=2.0, y=3.0, h=0)
    G.add_node('Q:2_2', label='Q', R=1)
    G.add_node('v:3:3', label='v', x=3.0, y=3.0, h=0)
    G.add_node('v:0.5:0.0', label='v', x=0.5, y=0.0, h=0)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=0)
    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=0)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.5:0.5', label='v', x=0.5, y=0.5, h=0)
    G.add_node('Q:0.25:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.25', label='Q', R=0)
    G.add_node('Q:0.75:0.75', label='Q', R=0)
    G.add_node('Q:0.25:0.75', label='Q', R=0)
    G.add_node('v:2.5:0.0', label='v', x=2.5, y=0.0, h=0)
    G.add_node('v:2.0:0.5', label='v', x=2.0, y=0.5, h=0)
    G.add_node('v:3.0:0.5', label='v', x=3.0, y=0.5, h=0)
    G.add_node('v:2.5:1.0', label='v', x=2.5, y=1.0, h=1)
    G.add_node('v:2.5:0.5', label='v', x=2.5, y=0.5, h=0)
    G.add_node('Q:2.25:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.25', label='Q', R=0)
    G.add_node('Q:2.75:0.75', label='Q', R=0)
    G.add_node('Q:2.25:0.75', label='Q', R=0)
    G.add_node('v:1.5:1.0', label='v', x=1.5, y=1.0, h=0)
    G.add_node('v:1.0:1.5', label='v', x=1.0, y=1.5, h=1)
    G.add_node('v:2.0:1.5', label='v', x=2.0, y=1.5, h=1)
    G.add_node('v:1.5:2.0', label='v', x=1.5, y=2.0, h=1)
    G.add_node('v:1.5:1.5', label='v', x=1.5, y=1.5, h=0)
    G.add_node('Q:1.25:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.25', label='Q', R=0)
    G.add_node('Q:1.75:1.75', label='Q', R=0)
    G.add_node('Q:1.25:1.75', label='Q', R=0)
    G.add_node('v:1.5:0.0', label='v', x=1.5, y=0.0, h=0)
    G.add_node('v:1.5:0.5', label='v', x=1.5, y=0.5, h=0)
    G.add_node('Q:1.25:0.25', label='Q', R=0)
    G.add_node('Q:1.25:0.75', label='Q', R=0)
    G.add_node('Q:1.75:0.25', label='Q', R=0)
    G.add_node('Q:1.75:0.75', label='Q', R=0)

    edges = [
        ('v:0:0', 'v:0.5:0.0', {'label':'E','B':1}),
        ('v:0:0', 'v:0.0:0.5', {'label':'E','B':1}),
        ('v:0:0', 'Q:0.25:0.25', {}),
        ('v:1:0', 'v:0.5:0.0', {'label':'E','B':1}),
        ('v:1:0', 'v:1.0:0.5', {'label':'E','B':0}),
        ('v:1:0', 'Q:0.75:0.25', {}),
        ('v:1:0', 'v:1.5:0.0', {'label':'E','B':1}),
        ('v:1:0', 'Q:1.25:0.25', {}),
        ('v:1:1', 'Q:1_0', {}),
        ('v:1:1', 'v:1.0:0.5', {'label':'E','B':0}),
        ('v:1:1', 'v:0.5:1.0', {'label':'E','B':0}),
        ('v:1:1', 'Q:0.75:0.75', {}),
        ('v:1:1', 'v:1.5:1.0', {'label':'E','B':0}),
        ('v:1:1', 'v:1.0:1.5', {'label':'E','B':0}),
        ('v:1:1', 'Q:1.25:1.25', {}),
        ('v:1:1', 'Q:1.25:0.75', {}),
        ('v:0:1', 'v:0:2', {'label':'E','B':1}),
        ('v:0:1', 'Q:1_0', {}),
        ('v:0:1', 'v:0.0:0.5', {'label':'E','B':1}),
        ('v:0:1', 'v:0.5:1.0', {'label':'E','B':0}),
        ('v:0:1', 'Q:0.25:0.75', {}),
        ('v:2:0', 'v:2.5:0.0', {'label':'E','B':1}),
        ('v:2:0', 'v:2.0:0.5', {'label':'E','B':0}),
        ('v:2:0', 'Q:2.25:0.25', {}),
        ('v:2:0', 'v:1.5:0.0', {'label':'E','B':1}),
        ('v:2:0', 'Q:1.75:0.25', {}),
        ('v:2:1', 'Q:1_2', {}),
        ('v:2:1', 'v:2.0:0.5', {'label':'E','B':0}),
        ('v:2:1', 'v:2.5:1.0', {'label':'E','B':0}),
        ('v:2:1', 'Q:2.25:0.75', {}),
        ('v:2:1', 'v:1.5:1.0', {'label':'E','B':0}),
        ('v:2:1', 'v:2.0:1.5', {'label':'E','B':0}),
        ('v:2:1', 'Q:1.75:1.25', {}),
        ('v:2:1', 'Q:1.75:0.75', {}),
        ('v:3:0', 'v:2.5:0.0', {'label':'E','B':1}),
        ('v:3:0', 'v:3.0:0.5', {'label':'E','B':1}),
        ('v:3:0', 'Q:2.75:0.25', {}),
        ('v:3:1', 'v:3:2', {'label':'E','B':1}),
        ('v:3:1', 'Q:1_2', {}),
        ('v:3:1', 'v:3.0:0.5', {'label':'E','B':1}),
        ('v:3:1', 'v:2.5:1.0', {'label':'E','B':0}),
        ('v:3:1', 'Q:2.75:0.75', {}),
        ('Q:1_0', 'v:1:2', {}),
        ('Q:1_0', 'v:0:2', {}),
        ('v:1:2', 'v:0:2', {'label':'E','B':0}),
        ('v:1:2', 'v:1:3', {'label':'E','B':0}),
        ('v:1:2', 'Q:2_0', {}),
        ('v:1:2', 'Q:2_1', {}),
        ('v:1:2', 'v:1.0:1.5', {'label':'E','B':0}),
        ('v:1:2', 'v:1.5:2.0', {'label':'E','B':0}),
        ('v:1:2', 'Q:1.25:1.75', {}),
        ('v:0:2', 'v:0:3', {'label':'E','B':1}),
        ('v:0:2', 'Q:2_0', {}),
        ('v:2:2', 'v:3:2', {'label':'E','B':0}),
        ('v:2:2', 'Q:1_2', {}),
        ('v:2:2', 'v:2:3', {'label':'E','B':0}),
        ('v:2:2', 'Q:2_1', {}),
        ('v:2:2', 'Q:2_2', {}),
        ('v:2:2', 'v:2.0:1.5', {'label':'E','B':0}),
        ('v:2:2', 'v:1.5:2.0', {'label':'E','B':0}),
        ('v:2:2', 'Q:1.75:1.75', {}),
        ('Q:1_2', 'v:3:2', {}),
        ('v:3:2', 'v:3:3', {'label':'E','B':1}),
        ('v:3:2', 'Q:2_2', {}),
        ('Q:2_0', 'v:1:3', {}),
        ('Q:2_0', 'v:0:3', {}),
        ('v:1:3', 'v:0:3', {'label':'E','B':1}),
        ('v:1:3', 'v:2:3', {'label':'E','B':1}),
        ('v:1:3', 'Q:2_1', {}),
        ('Q:2_1', 'v:2:3', {}),
        ('v:2:3', 'v:3:3', {'label':'E','B':1}),
        ('v:2:3', 'Q:2_2', {}),
        ('Q:2_2', 'v:3:3', {}),
        ('v:0.5:0.0', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:0.5:0.0', 'Q:0.25:0.25', {}),
        ('v:0.5:0.0', 'Q:0.75:0.25', {}),
        ('v:0.0:0.5', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:0.0:0.5', 'Q:0.25:0.25', {}),
        ('v:0.0:0.5', 'Q:0.25:0.75', {}),
        ('v:1.0:0.5', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:1.0:0.5', 'Q:0.75:0.25', {}),
        ('v:1.0:0.5', 'Q:0.75:0.75', {}),
        ('v:1.0:0.5', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:1.0:0.5', 'Q:1.25:0.25', {}),
        ('v:1.0:0.5', 'Q:1.25:0.75', {}),
        ('v:0.5:1.0', 'v:0.5:0.5', {'label':'E','B':0}),
        ('v:0.5:1.0', 'Q:0.75:0.75', {}),
        ('v:0.5:1.0', 'Q:0.25:0.75', {}),
        ('v:0.5:0.5', 'Q:0.25:0.25', {}),
        ('v:0.5:0.5', 'Q:0.75:0.25', {}),
        ('v:0.5:0.5', 'Q:0.75:0.75', {}),
        ('v:0.5:0.5', 'Q:0.25:0.75', {}),
        ('v:2.5:0.0', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:2.5:0.0', 'Q:2.25:0.25', {}),
        ('v:2.5:0.0', 'Q:2.75:0.25', {}),
        ('v:2.0:0.5', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:2.0:0.5', 'Q:2.25:0.25', {}),
        ('v:2.0:0.5', 'Q:2.25:0.75', {}),
        ('v:2.0:0.5', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:2.0:0.5', 'Q:1.75:0.25', {}),
        ('v:2.0:0.5', 'Q:1.75:0.75', {}),
        ('v:3.0:0.5', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:3.0:0.5', 'Q:2.75:0.25', {}),
        ('v:3.0:0.5', 'Q:2.75:0.75', {}),
        ('v:2.5:1.0', 'v:2.5:0.5', {'label':'E','B':0}),
        ('v:2.5:1.0', 'Q:2.75:0.75', {}),
        ('v:2.5:1.0', 'Q:2.25:0.75', {}),
        ('v:2.5:0.5', 'Q:2.25:0.25', {}),
        ('v:2.5:0.5', 'Q:2.75:0.25', {}),
        ('v:2.5:0.5', 'Q:2.75:0.75', {}),
        ('v:2.5:0.5', 'Q:2.25:0.75', {}),
        ('v:1.5:1.0', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:1.5:1.0', 'Q:1.25:1.25', {}),
        ('v:1.5:1.0', 'Q:1.75:1.25', {}),
        ('v:1.5:1.0', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:1.5:1.0', 'Q:1.25:0.75', {}),
        ('v:1.5:1.0', 'Q:1.75:0.75', {}),
        ('v:1.0:1.5', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:1.0:1.5', 'Q:1.25:1.25', {}),
        ('v:1.0:1.5', 'Q:1.25:1.75', {}),
        ('v:2.0:1.5', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:2.0:1.5', 'Q:1.75:1.25', {}),
        ('v:2.0:1.5', 'Q:1.75:1.75', {}),
        ('v:1.5:2.0', 'v:1.5:1.5', {'label':'E','B':0}),
        ('v:1.5:2.0', 'Q:1.75:1.75', {}),
        ('v:1.5:2.0', 'Q:1.25:1.75', {}),
        ('v:1.5:1.5', 'Q:1.25:1.25', {}),
        ('v:1.5:1.5', 'Q:1.75:1.25', {}),
        ('v:1.5:1.5', 'Q:1.75:1.75', {}),
        ('v:1.5:1.5', 'Q:1.25:1.75', {}),
        ('v:1.5:0.0', 'v:1.5:0.5', {'label':'E','B':0}),
        ('v:1.5:0.0', 'Q:1.25:0.25', {}),
        ('v:1.5:0.0', 'Q:1.75:0.25', {}),
        ('v:1.5:0.5', 'Q:1.25:0.25', {}),
        ('v:1.5:0.5', 'Q:1.25:0.75', {}),
        ('v:1.5:0.5', 'Q:1.75:0.25', {}),
        ('v:1.5:0.5', 'Q:1.75:0.75', {})
    ]

    for u, v, attr in edges:
        G.add_edge(u, v, **attr)

    return G


def valid_graph5() -> nx.Graph:
    """7-nodes and one Q-node"""
    G = nx.Graph()
    G.add_node(
        'Q',
        label='Q',
        R=1,
    )
    G.add_node('v:0.0:0.0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1.0:0.0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1.0:1.0', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0.0:1.0', label='v', x=0.0, y=1.0, h=0)

    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=1)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=1)

    G.add_edge('v:0.0:0.0', 'v:1.0:0.0', label='E', B=0)
    G.add_edge('v:1.0:0.0', 'v:1.0:0.5', label='E', B=1)
    G.add_edge('v:1.0:0.5', 'v:1.0:1.0', label='E', B=1)
    G.add_edge('v:1.0:1.0', 'v:0.5:1.0', label='E', B=1)
    G.add_edge('v:0.5:1.0', 'v:0.0:1.0', label='E', B=1)
    G.add_edge('v:0.0:0.0', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0.0:0.5', 'v:0.0:1.0', label='E', B=1)

    G.add_edge('Q', 'v:0.0:0.0')
    G.add_edge('Q', 'v:1.0:0.0')
    G.add_edge('Q', 'v:1.0:1.0')
    G.add_edge('Q', 'v:0.0:1.0')

    return G


def valid_graph6() -> nx.Graph:
    """8-nodes and one Q-node"""
    G = nx.Graph()
    G.add_node(
        'Q',
        label='Q',
        R=1,
    )

    G.add_node('v:0.0:0.0', label='v', x=0.0, y=0.0, h=0)
    G.add_node('v:1.0:0.0', label='v', x=1.0, y=0.0, h=0)
    G.add_node('v:1.0:1.0', label='v', x=1.0, y=1.0, h=0)
    G.add_node('v:0.0:1.0', label='v', x=0.0, y=1.0, h=0)

    G.add_node('v:0.5:0.0', label='v', x=0.5, y=0.0, h=1)
    G.add_node('v:1.0:0.5', label='v', x=1.0, y=0.5, h=1)
    G.add_node('v:0.5:1.0', label='v', x=0.5, y=1.0, h=1)
    G.add_node('v:0.0:0.5', label='v', x=0.0, y=0.5, h=1)

    G.add_edge('v:0.0:0.0', 'v:0.5:0.0', label='E', B=1)
    G.add_edge('v:0.5:0.0', 'v:1.0:0.0', label='E', B=1)

    G.add_edge('v:1.0:0.0', 'v:1.0:0.5', label='E', B=1)
    G.add_edge('v:1.0:0.5', 'v:1.0:1.0', label='E', B=1)

    G.add_edge('v:1.0:1.0', 'v:0.5:1.0', label='E', B=1)
    G.add_edge('v:0.5:1.0', 'v:0.0:1.0', label='E', B=1)

    G.add_edge('v:0.0:1.0', 'v:0.0:0.5', label='E', B=1)
    G.add_edge('v:0.0:0.5', 'v:0.0:0.0', label='E', B=1)

    G.add_edge('Q', 'v:0.0:0.0')
    G.add_edge('Q', 'v:1.0:0.0')
    G.add_edge('Q', 'v:1.0:1.0')
    G.add_edge('Q', 'v:0.0:1.0')

    return G