import networkx as nx
import typer
from pyvis.network import Network
from scipy.stats import __dict__ as stats_dict

from ..generation import gen

app = typer.Typer()


class Graph_drawer:

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
        Генерация графов из заданного распределения.

        :param distribution: Распределение из scipy.stats
        :param graphs_number: Количество графов для генерации
        :param loc: Среднее значение (loc) для распределения
        :param scale: Стандартное отклонение (scale) для распределения
        :param size: Размер выборки
        :param file_path: Путь для сохранения графов
        """
        for i in range(graphs_number):
            sample: list[float] = distribution.rvs(loc=loc, scale=scale, size=size)
            dist: float = max(sample) - min(sample)

            res: gen.Graph_generator = gen.Graph_generator(sample, dist)
            graph: nx.Graph = res.generate()

            network_graph = Network()
            network_graph.from_nx(graph)
            network_graph.prep_notebook()
            network_graph.show(file_path + f"{i}.html")


@app.command()
def main(
    distribution: str = typer.Argument(..., help="Имя распределения из scipy.stats (например, norm, uniform)."),
    graphs_number: int = typer.Option(10, help="Количество графов для генерации."),
    loc: float = typer.Option(0, help="Среднее значение (loc) для распределения."),
    scale: float = typer.Option(1, help="Стандартное отклонение (scale) для распределения."),
    size: int = typer.Option(200, help="Размер выборки."),
    file_path: str = typer.Option("./graph_view/graph", help="Путь для сохранения графов."),
):
    """
    Основная функция для обработки аргументов и вызова draw.
    """
    try:
        distribution_instance = stats_dict[distribution]
    except KeyError:
        raise typer.BadParameter(f"Распределение {distribution} не найдено в scipy.stats.")

    Graph_drawer.draw(
        distribution=distribution_instance,
        graphs_number=graphs_number,
        loc=loc,
        scale=scale,
        size=size,
        file_path=file_path,
    )


if __name__ == "__main__":
    app()
