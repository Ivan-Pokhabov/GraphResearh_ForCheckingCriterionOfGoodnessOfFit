from types import MappingProxyType

from scipy.stats import __dict__ as stats_dict

from .get_graph_statistics import Get_Graph_Stat


class Graph_analyzer:

    distribution = MappingProxyType(stats_dict)

    @staticmethod
    def get_avg_max_node_degrees(distribution_name, scale: float, size: int, experiments_number: int) -> float:
        result: int = 0

        for _ in range(experiments_number):
            sample: list[float] = Graph_analyzer.distribution[distribution_name].rvs(scale=scale, size=size)
            degrees_array: list[int] = Get_Graph_Stat.get_degrees(sample)
            result += len(degrees_array)

        return result / experiments_number

    @staticmethod
    def get_avg_edges_number(distribution_name, scale: float, size: int, experiments_number: int) -> float:
        edges: int = 0

        for _ in range(experiments_number):
            sample: list[float] = Graph_analyzer.distribution[distribution_name].rvs(scale=scale, size=size)
            edges += Get_Graph_Stat.get_edges_number(sample)

        return edges / experiments_number

    @staticmethod
    def get_avg_components_number(distribution_name, scale: float, size: int, experiments_number: int) -> float:
        components: int = 0

        for _ in range(experiments_number):
            sample = Graph_analyzer.distribution[distribution_name].rvs(scale=scale, size=size)
            components += Get_Graph_Stat.get_components_number(sample)

        return components / experiments_number
