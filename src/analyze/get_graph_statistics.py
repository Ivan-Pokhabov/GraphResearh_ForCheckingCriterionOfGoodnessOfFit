import networkx as nx

from ..generation import gen


class Get_Graph_Stat:

    @staticmethod
    def get_edges_number(sample: list[float]) -> int:
        dist: float = (max(sample) - min(sample)) / 10
        graph: nx.Graph = gen.Graph_generator(sample, dist).generate()
        return nx.number_of_edges(graph)

    @staticmethod
    def get_degrees(sample: list[float]) -> list[int]:
        dist: float = (max(sample) - min(sample)) / 10
        graph: nx.Graph = gen.Graph_generator(sample, dist).generate()
        return nx.degree_histogram(graph)

    @staticmethod
    def get_components_number(sample: list[float]) -> int:
        dist: float = (max(sample) - min(sample)) / 10
        graph: nx.Graph = gen.Graph_generator(sample, dist).generate()
        return nx.number_connected_components(graph)
