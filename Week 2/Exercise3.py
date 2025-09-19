import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict, List, Tuple

def create_star_graph(n: int) -> nx.Graph:
    """ Create a star graph with n nodes (1 hub + n-1 leaves)"""
    G = nx.Graph()
    G.add_node(0)  # hub node
    for i in range(1, n):
        G.add_edge(0, i)
    return G

def add_node_barabasi_albert(G: nx.Graph, M: int) -> None:
    """ Add one new node to G connecting to M existing nodes with probability proportional to their degree."""
    new_node = max(G.nodes) + 1
    degrees = dict(G.degree())
    total_degree = sum(degrees.values())
    probs = [degrees[node] / total_degree for node in G.nodes()]
    
    # Choose M unique nodes based on degree probability
    targets = set()
    while len(targets) < M:
        chosen = random.choices(list(G.nodes()), weights=probs, k=1)[0]
        if chosen != new_node:
            targets.add(chosen)
    for target in targets:
        G.add_edge(new_node, target)

def build_barabasi_albert_network(n_init: int, n_total: int, M: int) -> nx.Graph:
    """
    Build Barabasi-Albert network starting from star graph with n_init nodes,
    adding nodes until total n_total nodes, each new node connects to M existing nodes.
    """
    G = create_star_graph(n_init)
    while len(G.nodes) < n_total:
        add_node_barabasi_albert(G, M)
    return G

def simulate_pagerank(G: nx.Graph, alpha: float, T: int) -> Dict[int, float]:
    """
    Simulate PageRank by random surfing on undirected graph G.
    alpha: probability to follow a link
    T: total number of steps
    Returns estimated PageRank as visit frequency.
    """
    nodes = list(G.nodes)
    current = random.choice(nodes)
    visits = defaultdict(int)
    
    for _ in range(T):
        visits[current] += 1
        neighbors = list(G.neighbors(current))
        if neighbors and random.random() < alpha:
            current = random.choice(neighbors)
        else:
            current = random.choice(nodes)
    # Normalize visits to probabilities
    pagerank = {node: visits[node] / T for node in nodes}
    return pagerank

def plot_network(G: nx.Graph, title: str) -> None:
    """ Plot the network graph"""
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, node_size=50, node_color='blue', edge_color='gray', with_labels=False)
    plt.title(title)
    plt.show()

def plot_pagerank_distribution(pagerank: Dict[int, float], title: str) -> None:
    """
    Plot histogram of PageRank probabilities.
    """
    plt.figure(figsize=(8,6))
    plt.hist(pagerank.values(), bins=30, color='green', edgecolor='black')
    plt.title(title)
    plt.xlabel('PageRank Probability')
    plt.ylabel('Frequency')
    plt.show()

# Parameters
n_init = 5      # initial star graph nodes
n_total = 400   # total nodes
M = 4           # links per new node
alpha = 0.85    # probability to follow a link
T = 100000      # number of surfing steps

# Build network and simulate PageRank
G_undirected = build_barabasi_albert_network(n_init, n_total, M)
pagerank_undirected = simulate_pagerank(G_undirected, alpha, T)

# Visualize
plot_network(G_undirected, "Barabasi-Albert Network (Undirected)")
plot_pagerank_distribution(pagerank_undirected, "PageRank Distribution (Undirected)")

