class GraphGenerator:

    @staticmethod
    def generate(sample: list[float], dist: float) -> list[(int, int)]:
        edges = []

        for i in range(len(sample)):
            for j in range(i):
                if abs(sample[i] - sample[j]) < dist:
                    edges.append((j, i))

        return edges
