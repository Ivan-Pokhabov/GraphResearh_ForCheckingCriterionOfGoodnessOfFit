import typer

from .graph_gen import GraphGenerator
from .sample_gen import SampleGenerator


class Generator:

    @staticmethod
    def generate(distribution: str, graphs_number: int, loc: float, scale: float, size: int, file_name: str) -> None:
        for i in range(graphs_number):
            sample: list[float] = SampleGenerator.generate(distribution, loc, scale, size)
            dist: float = (max(sample) - min(sample)) / 10
            GraphGenerator.generate(sample, dist, f"{file_name}{i}")


app = typer.Typer()


@app.command()
def main(
    distribution: str = typer.Argument(
        ..., help="The name of the distribution from scipy.stats (e.g., norm, uniform)."
    ),
    graphs_number: int = typer.Option(10, help="The number of graphs to generate."),
    loc: float = typer.Option(0, help="The mean (loc) for the distribution."),
    scale: float = typer.Option(1, help="The standard deviation (scale) for the distribution."),
    size: int = typer.Option(200, help="The sample size."),
    file_name: str = typer.Option("graph", help="The file path to save the graphs."),
):

    Generator.generate(
        distribution=distribution,
        graphs_number=graphs_number,
        loc=loc,
        scale=scale,
        size=size,
        file_name=file_name,
    )


if __name__ == "__main__":
    app()
