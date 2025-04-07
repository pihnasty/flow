import copy
import math
import numpy as np
from copy import deepcopy

import pandas as pd
from numpy import std, mean

from pom.stochastic03.utils import MathUtil
from pom.stochastic03.utils.Constants import FLOW, TIME


class SpectrumWithMoreRealizationApproximate:
    def __init__(self, dim, number_of_spectrum_split_parts, number_of_harmonics):
        self.dim = dim
        self.number_of_spectrum_split_parts = number_of_spectrum_split_parts
        self.number_of_harmonics = number_of_harmonics

    def __get_harmonic_values(self, dim_parts):
        cos_harmonic_values = [[0] * self.number_of_harmonics] * self.number_of_spectrum_split_parts
        sin_harmonic_values = [[0] * self.number_of_harmonics] * self.number_of_spectrum_split_parts
        for n in range(self.number_of_spectrum_split_parts):
            cos_harmonic_values[n], sin_harmonic_values[n] \
                = MathUtil.numeric_calculate_fourier_series(dim_parts[n][FLOW], dim_parts[n][TIME],
                                                            self.number_of_harmonics)
        transposed_matrix_cos = [[cos_harmonic_values[k][m] for k in range(len(cos_harmonic_values))]
                             for m in range(len(cos_harmonic_values[0]))]
        transposed_matrix_sin = [[sin_harmonic_values[k][m] for k in range(len(sin_harmonic_values))]
                                 for m in range(len(sin_harmonic_values[0]))]
        return cos_harmonic_values, sin_harmonic_values, transposed_matrix_cos, transposed_matrix_sin

    def get_param(self):
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values, transposed_matrix_cos, transposed_matrix_sin = self.__get_harmonic_values(dim_parts)
        mean_value = 0.0
        std2 = 0.0
        k_sin = 0
        for row in transposed_matrix_cos:
            std2 = std2 + 0.5 * std(row) ** 2 + 0.5 * std(transposed_matrix_sin[k_sin])**2 # / len(dim_parts)
            k_sin=k_sin+1
        mean_value = mean_value + mean(transposed_matrix_cos[0])

        approximate_dim_parts = MathUtil.calculate_function(dim_parts, cos_harmonic_values, sin_harmonic_values)
        approximate_array_dim = np.concatenate(approximate_dim_parts)
        approximate_dim = pd.DataFrame(approximate_array_dim, columns=[TIME, FLOW])
        return approximate_dim, mean_value, math.sqrt(std2)

    def get_transposed_matrix(self):
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values, transposed_matrix_cos, transposed_matrix_sin\
            = self.__get_harmonic_values(dim_parts)
        return transposed_matrix_cos, transposed_matrix_sin

    def get_mean_by_row_of_transposed_matrix(self):
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values, transposed_matrix_cos, transposed_matrix_sin \
            = self.__get_harmonic_values(dim_parts)
        return np.mean(transposed_matrix_cos, axis=1), np.mean(transposed_matrix_sin, axis=1)

    def get_mean_approximate_dim(self):
        dim_parts = np.array_split(self.dim, self.number_of_spectrum_split_parts)
        cos_harmonic_values, sin_harmonic_values = self.get_mean_by_row_of_transposed_matrix()
        approximate_dim_parts\
            = MathUtil.calculate_function_by_mean_harmonic_values(dim_parts, cos_harmonic_values, sin_harmonic_values)
        approximate_array_dim = np.concatenate(approximate_dim_parts)
        approximate_dim = pd.DataFrame(approximate_array_dim, columns=[TIME, FLOW])
        return approximate_dim

