import networkx as nx
import typer
from pyvis.network import Network
from scipy.stats import __dict__ as stats_dict

from ..generation import gen

app = typer.Typer()


class GraphDrawer:
    """
    A class for generating and visualizing graphs based on statistical distributions.
    """

    @staticmethod
    def draw(
        distribution,
        graphs_number: int = 10,
        loc: float = 0,
        scale: float = 1,
        size: int = 200,
        file_path: str = "./graph_view/graph",
    ):
        """
        Generate and visualize graphs based on the specified distribution.

        :param distribution: A distribution from scipy.stats
        :param graphs_number: The number of graphs to generate
        :param loc: The mean (loc) for the distribution
        :param scale: The standard deviation (scale) for the distribution
        :param size: The sample size for each graph
        :param file_path: The file path to save the graph visualizations
        """
        for i in range(graphs_number):
            sample: list[float] = distribution.rvs(loc=loc, scale=scale, size=size)
            dist: float = max(sample) - min(sample)

            res: gen.GraphGenerator = gen.GraphGenerator.generate(sample, dist)
            graph: nx.Graph = res.generate()

            network_graph = Network()
            network_graph.from_nx(graph)
            network_graph.prep_notebook()
            network_graph.show(file_path + f"{i}.html")


@app.command()
def main(
    distribution: str = typer.Argument(
        ..., help="The name of the distribution from scipy.stats (e.g., norm, uniform)."
    ),
    graphs_number: int = typer.Option(10, help="The number of graphs to generate."),
    loc: float = typer.Option(0, help="The mean (loc) for the distribution."),
    scale: float = typer.Option(1, help="The standard deviation (scale) for the distribution."),
    size: int = typer.Option(200, help="The sample size."),
    file_path: str = typer.Option("./graph_view/graph", help="The file path to save the graph visualizations."),
):
    """
    Main function to handle arguments and call the draw method.
    """
    try:
        distribution_instance = stats_dict[distribution]
    except KeyError:
        raise typer.BadParameter(f"The distribution '{distribution}' was not found in scipy.stats.")

    GraphDrawer.draw(
        distribution=distribution_instance,
        graphs_number=graphs_number,
        loc=loc,
        scale=scale,
        size=size,
        file_path=file_path,
    )


if __name__ == "__main__":
    app()
