import numpy as np


def normal_distribution(x, mean, std):
    return 1. / std / np.sqrt(2 * np.pi) * np.exp(-((x - mean) ** 2) / 2. / std ** 2)


def uniform_distribution(x, mean, _min):
    delta = mean - _min
    result = 0.0
    if mean - delta <= x <= mean + delta:
        result = 1.0 / (2.0 * delta)
    return result
