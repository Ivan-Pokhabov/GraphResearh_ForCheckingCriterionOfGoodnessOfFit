from multiprocessing import Pool
from multiprocessing import TimeoutError as MPTimeoutError

import typer
from pathlib import Path

from .get_graph_statistics import GetGraphStat


class GraphAnalyzer:

    @staticmethod
    def _process_results(func, files_path: list[str]) -> list[int]:
        try:
            with Pool(processes=4) as pool:
                return pool.map(func, files_path)
        except MPTimeoutError:
            raise RuntimeError("The multiprocessing pool operation timed out.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing results: {e}")

    @staticmethod
    def get_avg_max_node_degrees(folder_path: str) -> float:
        try:
            files_path = list(filter(lambda x: x.is_file(), list(Path(folder_path).iterdir())))
            results = GraphAnalyzer._process_results(GetGraphStat.get_degrees, files_path)
            return sum(map(len, results)) / len(files_path)
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the average maximum node degrees: {e}")

    @staticmethod
    def get_avg_edges_number(folder_path: str) -> float:
        try:
            files_path = list(filter(lambda x: x.is_file(), list(Path(folder_path).iterdir())))
            results = GraphAnalyzer._process_results(GetGraphStat.get_edges_number, files_path)
            return sum(results) / len(files_path)
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the average maximum node degrees: {e}")

    @staticmethod
    def get_avg_components_number(folder_path: str) -> float:
        try:
            files_path = list(filter(lambda x: x.is_file(), list(Path(folder_path).iterdir())))
            results = GraphAnalyzer._process_results(GetGraphStat.get_edges_number, files_path)
            return sum(results) / len(files_path)
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the average maximum node degrees: {e}")

app = typer.Typer()


@app.command()
def avg_max_node_degrees(folder_input: str = "./src/storage/graphs", output_name: str = "max_degrees"):
    try:
        avg = GraphAnalyzer.get_avg_max_node_degrees(folder_input)
        typer.echo(f"Average maximum number of node's degree: {avg}")
        with open(f"./src/storage/stats/{output_name}.txt", "w", encoding="UTF-8") as file_out:
                file_out.write(f"folder={folder_input}, result={avg}")
    except Exception as e:
        typer.echo(f"Error: {e}")


@app.command()
def avg_edges_number(folder_input: str = "./src/storage/graphs", output_name: str = "edges"):
    try:
        avg = GraphAnalyzer.get_avg_edges_number(folder_input)
        typer.echo(f"Average number of edges: {avg}")
        with open(f"./src/storage/stats/{output_name}.txt", "w", encoding="UTF-8") as file_out:
                file_out.write(f"folder={folder_input}, result={avg}")
    except Exception as e:
        typer.echo(f"Error: {e}")


@app.command()
def avg_components_number(folder_input: str = "./src/storage/graphs", output_name: str = "components"):
    try:
        avg = GraphAnalyzer.get_avg_components_number(folder_input)
        typer.echo(f"Average number of components: {avg}")
        with open(f"./src/storage/stats/{output_name}.txt", "w", encoding="UTF-8") as file_out:
                file_out.write(f"folder={folder_input}, result={avg}")
    except Exception as e:
        typer.echo(f"Error: {e}")


if __name__ == "__main__":
    app()
