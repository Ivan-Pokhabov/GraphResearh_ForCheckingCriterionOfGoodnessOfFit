import scipy.stats as sps
from gen import Graph_generator
from pyvis.network import Network


def main() -> None:
    size = 20

    for i in range(size):
        distribution = sps.uniform.rvs(loc=0, scale=3, size=200)
        dist = distribution.var() / 30
        res = Graph_generator(distribution, dist)
        graph = res.generate()
        nt = Network()
        nt.from_nx(graph)
        nt.prep_notebook()
        nt.show(f"./dataset/uniform_graph{i}.html")


if __name__ == "__main__":
    main()
