from scipy.stats import __dict__ as stats_dict


class SampleGenerator:

    @staticmethod
    def generate(distribution: str, loc: float, scale: float, size: int):
        return stats_dict[distribution].rvs(scale=scale, loc=loc, size=size)
