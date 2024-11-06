import networkx
import scipy.stats as sps
from gen import Graph_generator


class Graph_analyzer:

    @staticmethod
    def get_avg_max_node_degrees(scale: float, size: int, experiments_number: int) -> list[float]:
        result = 0

        for _ in range(experiments_number):
            distribution = sps.uniform.rvs(scale=scale, size=size)
            dist = (max(distribution) - min(distribution)) / 10

            graph = Graph_generator(distribution, dist).generate()
            degrees_array = networkx.degree_histogram(graph)
            
            result += len(degrees_array)

        return result / experiments_number

    @staticmethod
    def get_avg_edges_number(scale: float, size: int, experiments_number: int) -> float:
        edges = 0

        for _ in range(experiments_number):
            distribution = sps.uniform.rvs(scale=scale, size=size)
            dist = (max(distribution) - min(distribution)) / 10

            graph = Graph_generator(distribution, dist).generate()

            edges += networkx.number_of_edges(graph)

        return edges / experiments_number

    @staticmethod
    def get_avg_components_number(scale: float, size: int, experiments_number: int) -> float:

        components = 0

        for _ in range(experiments_number):
            distribution = sps.norm.rvs(scale=scale, size=size)
            dist = (max(distribution) - min(distribution)) / 10

            graph = Graph_generator(distribution, dist).generate()

            components += networkx.number_connected_components(graph)

        return components / experiments_number
