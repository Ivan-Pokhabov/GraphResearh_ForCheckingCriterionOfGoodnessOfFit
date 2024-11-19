from multiprocessing import Pool
from types import MappingProxyType

import typer
from scipy.stats import __dict__ as stats_dict

from .get_graph_statistics import Get_Graph_Stat


class GraphAnalyzer:

    distribution: dict = MappingProxyType(stats_dict)

    @staticmethod
    def _get_samples(
        distribution_name: str, loc: float, scale: float, size: int, experiments_number: int
    ) -> list[list[float]]:
        with Pool(processes=4) as pool:
            return pool.starmap(
                GraphAnalyzer.distribution[distribution_name].rvs, [(loc, scale, size)] * experiments_number
            )

    @staticmethod
    def _process_results(func, samples: list[list[float]]) -> list[int]:
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
        samples = GraphAnalyzer._get_samples(distribution_name, loc, scale, size, experiments_number)
        results = GraphAnalyzer._process_results(Get_Graph_Stat.get_edges_number, samples)
        return sum(results) / experiments_number


app = typer.Typer()


@app.command()
def avg_max_node_degrees(
    distribution_name: str = "norm", loc: float = 0, scale: float = 1, size: int = 200, experiments_number: int = 100
):
    avg = GraphAnalyzer.get_avg_max_node_degrees(distribution_name, loc, scale, size, experiments_number)
    typer.echo(f"Среднее максимальное число узлов: {avg}")


@app.command()
def avg_edges_number(
    distribution_name: str = "norm", loc: float = 0, scale: float = 1, size: int = 200, experiments_number: int = 100
):
    avg = GraphAnalyzer.get_avg_edges_number(distribution_name, loc, scale, size, experiments_number)
    typer.echo(f"Среднее количество рёбер: {avg}")


@app.command()
def avg_components_number(
    distribution_name: str = "norm", loc: float = 0, scale: float = 1, size: int = 200, experiments_number: int = 100
):
    avg = GraphAnalyzer.get_avg_components_number(distribution_name, loc, scale, size, experiments_number)
    typer.echo(f"Среднее количество компонент: {avg}")


if __name__ == "__main__":
    app()
