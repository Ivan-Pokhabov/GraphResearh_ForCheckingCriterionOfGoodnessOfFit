import networkx as nx

from ..graph_generation.graph_gen import GraphGenerator


class GetGraphStat:
    
    @staticmethod
    def _make_nx_graph(graph_file: str) -> nx.Graph:
        with open(graph_file, "r", encoding="UTF-8") as file:
            distribution, loc, scale, size = file.readline().strip().split()
            edges_list = [tuple(map(int, line.split())) for line in file]

        graph: nx.Graph = nx.Graph()
        graph.add_nodes_from(range(int(size)))
        graph.add_edges_from(edges_list)
        
        return graph

    @staticmethod
    def get_edges_number(graph_file: str) -> int:
        return nx.number_of_edges(GetGraphStat._make_nx_graph(graph_file))

    @staticmethod
    def get_degrees(graph_file: str) -> list[int]:
        return nx.degree_histogram(GetGraphStat._make_nx_graph(graph_file))

    @staticmethod
    def get_components_number(graph_file: str) -> int:
        return nx.number_connected_components(GetGraphStat._make_nx_graph(graph_file))
