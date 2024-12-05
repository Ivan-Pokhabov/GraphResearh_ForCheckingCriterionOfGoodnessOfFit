from multiprocessing import Pool
from pathlib import Path

import matplotlib.pyplot as plt
import typer

from src.graph_experimenteter.my_funcs import MyFunctions

app = typer.Typer()


@app.command()
def main(
    input_folder: str = typer.Argument("./src/storage/graphs/"),
    distribution: str = typer.Option("norm"),
    size: int = typer.Option(100),
    title: str = typer.Option(""),
    file_save: str = typer.Option("./src/storage/graphics"),
):

    with Pool(processes=4) as pool:
        y: list[float] = pool.starmap(
            MyFunctions.check_sample_ratio_max_degrees,
            list(
                map(
                    lambda x: (distribution, x, size), filter(lambda x: x.is_file(), list(Path(input_folder).iterdir()))
                )
            ),
        )

    plt.hist(y, bins=18, color="blue", edgecolor="black", alpha=0.7)

    plt.title(title)
    plt.xlabel("Ratio: real / my_func")
    plt.ylabel("Amount of coefficients")
    plt.savefig(f"{file_save}/{title}.png")


if __name__ == "__main__":
    app()
