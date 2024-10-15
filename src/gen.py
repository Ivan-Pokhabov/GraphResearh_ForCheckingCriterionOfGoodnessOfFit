import networkx as nx


class Graph_generator:

    def __init__(self, distribution: list[float], dist: int) -> None:
        self.distribution = distribution
        self.dist = dist

    def generate(self) -> nx.Graph:
        edges = []

        for i in range(len(self.distribution)):
            for j in range(i):
                if abs(self.distribution[i] - self.distribution[j]) < self.dist:
                    edges.append((j, i))

        graph = nx.Graph()
        graph.add_nodes_from(range(self.distribution.size))
        graph.add_edges_from(edges)

        return graph
