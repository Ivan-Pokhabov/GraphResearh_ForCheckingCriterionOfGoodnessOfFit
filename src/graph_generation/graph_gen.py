class GraphGenerator:

    @staticmethod
    def generate(sample: list[float], dist: float, file_name: str) -> None:
        edges = []
        path = f"./src/storage/graphs/{file_name}"

        for i in range(len(sample)):
            for j in range(i):
                if abs(sample[i] - sample[j]) < dist:
                    edges.append((j, i))

        with open(path, "a", encoding="UTF-8") as file_out:
            file_out.write("\n".join([f"{x[0]} {x[1]}" for x in edges]))
