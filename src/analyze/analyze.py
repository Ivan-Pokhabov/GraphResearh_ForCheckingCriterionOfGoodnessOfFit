from multiprocessing import Pool
from multiprocessing import TimeoutError as MPTimeoutError
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
        try:
            with Pool(processes=4) as pool:
                return pool.starmap(
                    GraphAnalyzer.distribution[distribution_name].rvs, [(loc, scale, size)] * experiments_number
                )
        except KeyError:
            raise ValueError(
                f"Invalid distribution name: {distribution_name}. Please use a valid distribution from scipy.stats."
            )
        except MPTimeoutError:
            raise RuntimeError("The multiprocessing pool operation timed out.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while generating samples: {e}")

    @staticmethod
    def _process_results(func, samples: list[list[float]]) -> list[int]:
        """
        Process the results of the samples using the given function.

        :param func: The function to process each sample
        :param samples: The list of samples to process

        :return: The processed results
        """
        try:
            with Pool(processes=4) as pool:
                return pool.map(func, samples)
        except MPTimeoutError:
            raise RuntimeError("The multiprocessing pool operation timed out.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing results: {e}")

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
        try:
            samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
            results = GraphAnalyzer._process_results(Get_Graph_Stat.get_degrees, samples)
            return sum(map(len, results)) / experiments_number
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the average maximum node degrees: {e}")

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
        try:
            samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
            results = GraphAnalyzer._process_results(Get_Graph_Stat.get_edges_number, samples)
            return sum(results) / experiments_number
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the average number of edges: {e}")

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
        try:
            samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
            results = GraphAnalyzer._process_results(Get_Graph_Stat.get_edges_number, samples)
            return sum(results) / experiments_number
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the average number of components: {e}")


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
    try:
        avg = GraphAnalyzer.get_avg_max_node_degrees(distribution_name, loc, scale, size, experiments_number)
        typer.echo(f"Average maximum number of nodes: {avg}")
    except Exception as e:
        typer.echo(f"Error: {e}")


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
    try:
        avg = GraphAnalyzer.get_avg_edges_number(distribution_name, loc, scale, size, experiments_number)
        typer.echo(f"Average number of edges: {avg}")
    except Exception as e:
        typer.echo(f"Error: {e}")


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
    try:
        avg = GraphAnalyzer.get_avg_components_number(distribution_name, loc, scale, size, experiments_number)
        typer.echo(f"Average number of components: {avg}")
    except Exception as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
