import networkx
from get_graph_statistics import Get_Graph_Stat


class Graph_analyzer:

    @staticmethod
    def get_avg_max_node_degrees(distribution, scale: float, size: int, experiments_number: int) -> float:
        result: int = 0

        for _ in range(experiments_number):
            sample: list[float] = distribution.rvs(scale=scale, size=size)
            degrees_array: list[int] = Get_Graph_Stat.get_degrees(sample)
            result += len(degrees_array)

        return result / experiments_number

    @staticmethod
    def get_avg_edges_number(distribution, scale: float, size: int, experiments_number: int) -> float:
        edges: int = 0

        for _ in range(experiments_number):
            sample: list[float] = distribution.rvs(scale=scale, size=size)
            edges += networkx.number_of_edges(sample)

        return edges / experiments_number

    @staticmethod
    def get_avg_components_number(distribution, scale: float, size: int, experiments_number: int) -> float:
        components: int = 0

        for _ in range(experiments_number):
            sample = distribution.rvs(scale=scale, size=size)
            components += Get_Graph_Stat.get_components_number(sample)

        return components / experiments_number
