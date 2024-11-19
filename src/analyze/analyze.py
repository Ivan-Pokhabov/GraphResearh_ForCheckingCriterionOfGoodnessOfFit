from multiprocessing import Pool
from types import MappingProxyType

import typer
from scipy.stats import __dict__ as stats_dict

from .get_graph_statistics import Get_Graph_Stat


class GraphAnalyzer:
    """
    A class for graph analysis using statistical distributions.
    """

    distribution: dict = MappingProxyType(stats_dict)

    @staticmethod
    def _get_samples(
        distribution_name: str, loc: float, scale: float, size: int, experiments_number: int
    ) -> list[list[float]]:
        """
        Generate samples based on the specified distribution.

        :param distribution_name: The name of the distribution from scipy.stats
        :param loc: The mean (loc) for the distribution
        :param scale: The standard deviation (scale) for the distribution
        :param size: The sample size
        :param experiments_number: The number of experiments

        :return: The generated samples
        """
        with Pool(processes=4) as pool:
            return pool.starmap(
                GraphAnalyzer.distribution[distribution_name].rvs, [(loc, scale, size)] * experiments_number
            )

    @staticmethod
    def _process_results(func, samples: list[list[float]]) -> list[int]:
        """
        Process the results of the samples using the given function.

        :param func: The function to process each sample
        :param samples: The list of samples to process

        :return: The processed results
        """
        with Pool(processes=4) as pool:
            return pool.map(func, samples)

    @staticmethod
    def get_avg_max_node_degrees(
        distribution_name: str = "norm",
        loc: float = 0,
        scale: float = 1,
        size: int = 200,
        experiments_number: int = 100,
    ) -> float:
        """
        Compute the average maximum degree of nodes in the graphs.

        :param distribution_name: The name of the distribution from scipy.stats
        :param loc: The mean (loc) for the distribution
        :param scale: The standard deviation (scale) for the distribution
        :param size: The sample size
        :param experiments_number: The number of experiments

        :return: The average maximum degree of nodes
        """
        samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
        results = GraphAnalyzer._process_results(Get_Graph_Stat.get_degrees, samples)
        return sum(map(len, results)) / experiments_number

    @staticmethod
    def get_avg_edges_number(
        distribution_name: str = "norm",
        loc: float = 0,
        scale: float = 1,
        size: int = 200,
        experiments_number: int = 100,
    ) -> float:
        """
        Compute the average number of edges in the graphs.

        :param distribution_name: The name of the distribution from scipy.stats
        :param loc: The mean (loc) for the distribution
        :param scale: The standard deviation (scale) for the distribution
        :param size: The sample size
        :param experiments_number: The number of experiments

        :return: The average number of edges
        """
        samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
        results = GraphAnalyzer._process_results(Get_Graph_Stat.get_edges_number, samples)
        return sum(results) / experiments_number

    @staticmethod
    def get_avg_components_number(
        distribution_name: str = "norm",
        loc: float = 0,
        scale: float = 1,
        size: int = 200,
        experiments_number: int = 100,
    ) -> float:
        """
        Compute the average number of components in the graphs.

        :param distribution_name: The name of the distribution from scipy.stats
        :param loc: The mean (loc) for the distribution
        :param scale: The standard deviation (scale) for the distribution
        :param size: The sample size
        :param experiments_number: The number of experiments

        :return: The average number of components
        """
        samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
        results = GraphAnalyzer._process_results(Get_Graph_Stat.get_edges_number, samples)
        return sum(results) / experiments_number


app = typer.Typer()


@app.command()
def avg_max_node_degrees(
    distribution_name: str = "norm", loc: float = 0, scale: float = 1, size: int = 200, experiments_number: int = 100
):
    """
    Get the average maximum degree of nodes in the graphs.

    :param distribution_name: The name of the distribution
    :param loc: The mean value
    :param scale: The standard deviation
    :param size: The sample size
    :param experiments_number: The number of experiments
    """
    avg = GraphAnalyzer.get_avg_max_node_degrees(distribution_name, loc, scale, size, experiments_number)
    typer.echo(f"Average maximum number of nodes: {avg}")


@app.command()
def avg_edges_number(
    distribution_name: str = "norm", loc: float = 0, scale: float = 1, size: int = 200, experiments_number: int = 100
):
    """
    Get the average number of edges in the graphs.

    :param distribution_name: The name of the distribution
    :param loc: The mean value
    :param scale: The standard deviation
    :param size: The sample size
    :param experiments_number: The number of experiments
    """
    avg = GraphAnalyzer.get_avg_edges_number(distribution_name, loc, scale, size, experiments_number)
    typer.echo(f"Average number of edges: {avg}")


@app.command()
def avg_components_number(
    distribution_name: str = "norm", loc: float = 0, scale: float = 1, size: int = 200, experiments_number: int = 100
):
    """
    Get the average number of components in the graphs.

    :param distribution_name: The name of the distribution
    :param loc: The mean value
    :param scale: The standard deviation
    :param size: The sample size
    :param experiments_number: The number of experiments
    """
    avg = GraphAnalyzer.get_avg_components_number(distribution_name, loc, scale, size, experiments_number)
    typer.echo(f"Average number of components: {avg}")


if __name__ == "__main__":
    app()
