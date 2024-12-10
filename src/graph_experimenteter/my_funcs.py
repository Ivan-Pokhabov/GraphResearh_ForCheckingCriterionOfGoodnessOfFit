from src.graph_analyzer.get_graph_statistics import GetGraphStat
from src.graph_generator.graph_gen import GraphGenerator


class MyFunctions:

    @staticmethod
    def check_sample_ratio_edges(distribution_name: str, sample: list[int]) -> float:
        func_dict = {
            "norm": MyFunctions.__norm_graph_edges,
            "uniform": MyFunctions.__uniform_graph_edges,
            "expon": MyFunctions.__expon_graph_edges,
        }

        dist: float = (max(sample) - min(sample)) / 10
        real_edges: int = GetGraphStat.get_edges_number(GraphGenerator.generate(sample, dist), len(sample))
        my_edges = func_dict[distribution_name](len(sample))
        return real_edges / my_edges

    @staticmethod
    def check_sample_ratio_max_degrees(distribution_name: str, sample: list[int]) -> float:
        func_dict = {
            "norm": MyFunctions.__norm_graph_max_degree,
            "uniform": MyFunctions.__uniform_graph_max_degree,
            "expon": MyFunctions.__expon_graph_max_degree,
        }

        dist: float = (max(sample) - min(sample)) / 10
        real_max_degree: int = len(GetGraphStat.get_degrees(GraphGenerator.generate(sample, dist), len(sample)))
        my_max_degree = func_dict[distribution_name](len(sample))
        return real_max_degree / my_max_degree

    @staticmethod
    def check_sample_ratio_components(distribution_name: str, sample: list[int]) -> float:
        func_dict = {
            "norm": MyFunctions.__norm_graph_components,
            "uniform": MyFunctions.__uniform_graph_components,
            "expon": MyFunctions.__expon_graph_components,
        }

        dist: float = (max(sample) - min(sample)) / 10
        real_components: int = GetGraphStat.get_components_number(GraphGenerator.generate(sample, dist), len(sample))
        my_components = func_dict[distribution_name](len(sample))
        return real_components / my_components

    @staticmethod
    def __norm_graph_edges(size: int) -> float:
        return 0.202 * size**2 - 32.51 * size + 5900

    @staticmethod
    def __expon_graph_edges(size: int) -> float:
        return 0.3042 * size**2 - 55.89 * size + 1.063e04

    @staticmethod
    def __uniform_graph_edges(size: int) -> float:
        return 0.09483 * size**2 + 0.1351 * size - 152.8

    @staticmethod
    def __norm_graph_max_degree(size: int) -> float:
        return 0.5266 * size - 29.81

    @staticmethod
    def __expon_graph_max_degree(size: int) -> float:
        return 0.8125 * size - 37.07

    @staticmethod
    def __uniform_graph_max_degree(size: int) -> float:
        return 0.2146 * size + 10.04

    @staticmethod
    def __norm_graph_components(size: int) -> float:
        return 0.1724 * size**2 - 5.372 * size + 143.7

    @staticmethod
    def __expon_graph_components(size: int) -> float:
        return 0.2649 * size**2 - 10.88 * size + 376.2

    @staticmethod
    def __uniform_graph_components(size: int) -> float:
        return 0.09514 * size**2 - 0.279 * size - 2.282
