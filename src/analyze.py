import networkx
import scipy.stats as sps
from get_graph_statistics import Get_Graph_Stat


class Graph_analyzer:

    @staticmethod
    def get_avg_max_node_degrees(scale: float, size: int, experiments_number: int) -> float:
        result: int = 0

        for _ in range(experiments_number):
            sample: list[float] = sps.uniform.rvs(scale=scale, size=size)
            dist: float = (max(sample) - min(sample)) / 10

            degrees_array: list[int] = Get_Graph_Stat.get_degrees(sample, dist)

            result += len(degrees_array)

        return result / experiments_number

    @staticmethod
    def get_avg_edges_number(scale: float, size: int, experiments_number: int) -> float:
        edges: int = 0

        for _ in range(experiments_number):
            sample: list[float] = sps.uniform.rvs(scale=scale, size=size)
            dist: float = (max(sample) - min(sample)) / 10

            edges += networkx.number_of_edges(sample, dist)

        return edges / experiments_number

    @staticmethod
    def get_avg_components_number(scale: float, size: int, experiments_number: int) -> float:

        components = 0

        for _ in range(experiments_number):
            sample = sps.norm.rvs(scale=scale, size=size)
            dist = (max(sample) - min(sample)) / 10

            components += Get_Graph_Stat.get_components_number(sample, dist)

        return components / experiments_number
