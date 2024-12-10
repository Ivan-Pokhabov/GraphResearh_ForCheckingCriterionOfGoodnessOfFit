from multiprocessing import Pool

import matplotlib.pyplot as plt
import typer

from src.graph_experimenteter.my_funcs import MyFunctions
from src.graph_generator.sample_gen import SampleGenerator

app = typer.Typer()


@app.command()
def main(
    graphs_number: int = typer.Option(1000),
    distribution: str = typer.Option("norm"),
    loc: float = typer.Option(0),
    scale: float = typer.Option(1),
    size: int = typer.Option(100),
    title: str = typer.Option(""),
    file_save: str = typer.Option("./src/storage/graphics"),
):

    with Pool(processes=4) as pool:
        samples: list[list[float]] = pool.starmap(
            SampleGenerator.generate, [(distribution, loc, scale, size) for _ in range(graphs_number)]
        )
        y: list[float] = pool.starmap(
            MyFunctions.check_sample_ratio_max_degrees, zip([distribution] * graphs_number, samples)
        )

    plt.hist(y, bins=18, color="blue", edgecolor="black", alpha=0.7)

    plt.title(title)
    plt.xlabel("Ratio: real / my_func")
    plt.ylabel("Amount of coefficients")
    plt.savefig(f"{file_save}/{title}.png")


if __name__ == "__main__":
    app()
