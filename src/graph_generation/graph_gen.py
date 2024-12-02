class GraphGenerator:

    @staticmethod
    def generate(sample: list[float], dist: float, file_name: str) -> None:
        """Generates a graph based on the given sample and distance threshold.

        The graph is created by adding nodes and edges. An edge is added between two nodes if the
        absolute difference between their corresponding values in the sample is less than the
        specified threshold distance.

        :param sample: A list of values representing the sample of the nodes.
        :param dist: The threshold distance for connecting nodes. Nodes whose values have an absolute
                     difference less than this threshold will be connected.
        :return: A NetworkX graph where nodes are connected according to the distance condition."""

        edges = []
        path = f"./src/storage/graphs/{file_name}"

        for i in range(len(sample)):
            for j in range(i):
                if abs(sample[i] - sample[j]) < dist:
                    edges.append((j, i))

        with open(path, "w", encoding="UTF-8") as file_out:
            file_out.write("\n".join([f"{x[0]} {x[1]}" for x in edges]))
