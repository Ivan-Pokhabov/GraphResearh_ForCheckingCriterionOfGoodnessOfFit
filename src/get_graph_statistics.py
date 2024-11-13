import networkx as nx
from gen import Graph_generator


class Get_Graph_Stat:

    @staticmethod
    def get_edges_number(sample: list[float], dist: float) -> int:
        graph: nx.Graph = Graph_generator(sample, dist).generate()
        return nx.number_of_edges(graph)

    @staticmethod
    def get_degrees(sample: list[float], dist: float) -> list[int]:
        graph: nx.Graph = Graph_generator(sample, dist).generate()
        return nx.degree_histogram(graph)

    @staticmethod
    def get_components_number(sample: list[float], dist: float) -> int:
        graph: nx.Graph = Graph_generator(sample, dist).generate()
        return nx.number_connected_components(graph)
