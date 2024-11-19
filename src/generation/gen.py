import networkx as nx


class GraphGenerator:

    @staticmethod
    def generate(distribution: list[float], dist: float) -> nx.Graph:
        edges = []

        for i in range(len(distribution)):
            for j in range(i):
                if abs(distribution[i] - distribution[j]) < dist:
                    edges.append((j, i))

        graph = nx.Graph()
        graph.add_nodes_from(range(distribution.size))
        graph.add_edges_from(edges)

        return graph
