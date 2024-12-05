import networkx as nx


class GetGraphStat:

    @staticmethod
    def _make_nx_graph(edges_list: list[(int, int)], nodes_number: int) -> nx.Graph:
        graph: nx.Graph = nx.Graph()
        graph.add_nodes_from(range(int(nodes_number)))
        graph.add_edges_from(edges_list)

        return graph

    @staticmethod
    def get_edges_number(edges_list: list[(int, int)], nodes_number: int) -> int:
        return nx.number_of_edges(GetGraphStat._make_nx_graph(edges_list, nodes_number))

    @staticmethod
    def get_degrees(edges_list: list[(int, int)], nodes_number: int) -> list[int]:
        return nx.degree_histogram(GetGraphStat._make_nx_graph(edges_list, nodes_number))

    @staticmethod
    def get_components_number(edges_list: list[(int, int)], nodes_number: int) -> int:
        return nx.number_connected_components(GetGraphStat._make_nx_graph(edges_list, nodes_number))
