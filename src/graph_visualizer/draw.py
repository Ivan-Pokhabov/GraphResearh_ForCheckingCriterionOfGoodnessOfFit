import networkx as nx
import typer
from pyvis.network import Network
from pathlib import Path

app = typer.Typer()


class GraphDrawer:
    """
    A class for generating and visualizing graphs based on statistical distributions.
    """

    @staticmethod
    def draw(file_input: Path, folder_output: str = "./src/storage/graphs_visualization") -> None:
        with open(file_input, "r") as file:
            distribution, loc, scale, size = file.readline().strip().split()
            edges_list = [tuple(map(int, line.split())) for line in file]
            
        graph: nx.Graph = nx.Graph()
        graph.add_nodes_from(range(int(size)))
        graph.add_edges_from(edges_list)
        
        network_graph = Network()
        network_graph.from_nx(graph)
        network_graph.prep_notebook()
        network_graph.show(folder_output + f"{file_input.stem}.html")


@app.command()
def main(folder_input: str = typer.Argument("./src/storage/graphs/"), folder_output: str = typer.Argument("./src/storage/graphs_visualization/")) -> None:
    directory: Path = Path(folder_input)
    for file_path in directory.iterdir():
        if file_path.is_file():
            GraphDrawer.draw(file_path, folder_output)


if __name__ == "__main__":
    app()
