import random

import pandas as pd

from io_utils.console.progress import progress
from pom.pde.Constants import NORMALIZATION_FACTOR, X, Y, DISTRIBUTION_DENSITY, NORMAL_DISTRIBUTION, MEAN, STD, \
    UNIFORM_DISTRIBUTION, MIN
from pom.pde.utils.math_util import normal_distribution, uniform_distribution


class TechnologicalRoute:

    def __init__(self, technological_route, max_operation_time, number_distribution_density_intervals,
                 number_operation_time, order_size, seed, backlogs_size):
        self.technological_route = technological_route
        self.max_operation_time = max_operation_time
        self.number_distribution_density_intervals = number_distribution_density_intervals
        self.number_operation_time = number_operation_time
        self.order_size = order_size
        self.seed = seed
        self.route_operations_times = {}
        self.backlogs_size = backlogs_size

    def fill_normalization_factor(self):
        """
        Method fills the normalization factor value for r0 parameter of the technological operation.
        """
        for i in range(1, len(self.technological_route) + 1):
            operation = self.technological_route[i]
            keys = operation.keys()
            normalization_factors_sum = 0.0
            for key in keys:
                risk = operation.get(key)
                normalization_factors_sum += risk.get(NORMALIZATION_FACTOR, 0.0)
            operation[0][NORMALIZATION_FACTOR] = 1 - normalization_factors_sum

    def generate_route_operations_times(self):
        uniform_randoms = self.initialize_ramdoms()
        operation_time_randoms = self.initialize_ramdoms()
        for i in range(1, len(self.technological_route) + 1):
            operation_times = self.initialization_operation_times()
            operation = self.technological_route[i]
            probability_risk = self.calculate_probability_risk(operation)
            for k in range(self.number_operation_time):
                value = uniform_randoms[i-1].uniform(0, 1)
                operation_time = self.generate_full_operation_time(i, operation, operation_time_randoms[i-1], probability_risk, value)
                operation_times[Y][k] = operation_time
                operation_times[X][k] = k
            self.route_operations_times[i] = operation_times
            progress(i, len(self.technological_route) + 1, "generate_route_operations_times")
        progress(len(self.technological_route) + 1, len(self.technological_route) + 1, "generate_route_operations_times")
        print()
        return self.route_operations_times

    def calculate_generated_distribution_densities(self):
        delta = self.max_operation_time / self.number_distribution_density_intervals
        generated_distribution_densities = {}
        route_operation_number = len(self.route_operations_times.keys())
        for key in self.route_operations_times.keys():
            operation_times = self.route_operations_times[key]
            line = sorted(operation_times[Y])
            operation_time = 0.0
            generated_distribution_density = self.initialization_distribution_density()

            for k in range(self.number_distribution_density_intervals):
                for i in range(len(line)):
                    if operation_time < line[i] <= operation_time + delta:
                        generated_distribution_density[Y][k] += 1.0/(delta * len(line))
                operation_time = operation_time + delta
                generated_distribution_density[X][k] = operation_time
            generated_distribution_densities[key] = generated_distribution_density
            progress(key, route_operation_number, "calculate_generated_distribution_densities")
        progress(route_operation_number, route_operation_number,"calculate_generated_distribution_densities")
        print()
        return generated_distribution_densities

    def calculate_technological_paths(self, random_step):
        technological_paths = {}
        k=self.backlogs_size  # number details into backlogs
        for n in range(self.order_size):
            technological_path = self.initialization_technological_path()
            for m in range(len(self.technological_route) + 1):
                if m == 0:
                    technological_path[Y][m] = 0
                    technological_path["Xmin"][m] = 0.0
                    if n<=k:
                        if n == 0:
                            technological_path[X][m] = 0.0
                        else:
                            technological_path[X][m] = technological_paths[n -1]["Xmin"][m + 1]
                    else:
                        technological_path[X][m] = max(technological_paths[n -1 - k]["Xmin"][m + 2], technological_paths[n -1]["Xmin"][m + 1])
                else:
                    technological_path[Y][m] = m
                    tau_m = self.route_operations_times[m][Y][n + random_step]
                    if n<=k:
                        if n == 0:
                            try:
                                technological_path["Xmin"][m] = technological_path[X][m - 1] + tau_m
                                technological_path[X][m] = technological_path["Xmin"][m]
                            except KeyError:
                                pass
                        else:
                            if m < len(self.technological_route):
                                technological_path["Xmin"][m] = technological_path[X][m - 1]  + tau_m
                                technological_path[X][m] = max(
                                    technological_path["Xmin"][m],
                                    technological_paths[n -1]["Xmin"][m + 1]
                                )
                            if m == len(self.technological_route):
                                technological_path["Xmin"][m] = technological_path[X][m - 1]  + tau_m
                                technological_path[X][m] = technological_path["Xmin"][m]
                    else:
                        if m < len(self.technological_route)-1:
                            technological_path["Xmin"][m] = technological_path[X][m - 1]  + tau_m
                            technological_path[X][m] = max(
                                technological_path["Xmin"][m],
                                technological_paths[n -1]["Xmin"][m + 1],
                                technological_paths[n -1 - k]["Xmin"][m + 2]
                            )
                        if m == len(self.technological_route)-1:
                            technological_path["Xmin"][m] = technological_path[X][m - 1]  + tau_m
                            technological_path[X][m] = max(
                                technological_path["Xmin"][m],
                                technological_paths[n -1]["Xmin"][m + 1]
                            )

                        if m == len(self.technological_route):
                            technological_path["Xmin"][m] = technological_path[X][m - 1]  + tau_m
                            technological_path[X][m] = technological_path["Xmin"][m]
            technological_paths[n] =  technological_path
        return technological_paths


    def calculate_technological_paths1(self, random_step):
        technological_paths = {}
        for n in range(self.order_size):
            technological_path = self.initialization_technological_path()
            tau_m = 0.0
            k=1
            for m in range(len(self.technological_route) + 1):
                if m == 0:
                    technological_path[Y][m] = 0
                    if n<=k:
                        if n == 0:
                            technological_path[X][m] = 0.0
                        else:
                            technological_path[X][m] = technological_paths[n -1][X][m + 1]
                    else:

                        technological_path[X][m] = max(technological_paths[n -1 - k][X][m + 2], technological_paths[n -1][X][m + 1])
                else:
                    tau_m += self.route_operations_times[m][Y][n + random_step]
                    technological_path[Y][m] = m
                    if n > k and m < len(self.technological_route) - 1:
                        try:
                            if tau_m < technological_paths[n -1 -k][X][m + 2]:
                                tau_m = technological_paths[n -1 - k][X][m + 2]
                        except KeyError:
                            raise KeyError(f"Missing key in route_operations_times for indices: m={m}, Y={Y}, n={n}, random_step={random_step}")
                    if n > 0 and m < len(self.technological_route):
                        if tau_m < technological_paths[n -1][X][m + 1]:
                            tau_m = technological_paths[n -1][X][m + 1]
                    technological_path[X][m] = tau_m
            technological_paths[n] =  technological_path
        return technological_paths


    def initialize_ramdoms(self):
        randoms = [random.Random()] * len(self.technological_route)
        count = self.seed
        for element in randoms:
            element.seed(count)
            count += 1000
        return randoms

    def generate_full_operation_time(self, i, operation, operation_time_random, probability_risk, value):
        keys = probability_risk.keys()
        operation_time = 0.0
        for key in keys:
            if value <= probability_risk[key]:
                risk = operation.get(key)
                operation_time = self.generate_operation_time(i, operation_time_random, risk)
                if key > 0:
                    risk0 = operation.get(0)
                    operation_time += self.generate_operation_time(i, operation_time_random, risk0)
                break
        return operation_time

    @staticmethod
    def generate_operation_time(i, operation_time_random, risk):
        operation_time = 0.0
        if risk.get(DISTRIBUTION_DENSITY) == NORMAL_DISTRIBUTION:
            operation_time = operation_time_random.gauss(risk[MEAN], risk[STD])
        if risk.get(DISTRIBUTION_DENSITY) == UNIFORM_DISTRIBUTION:
            operation_time = operation_time_random.uniform(risk[MIN], 2 * risk[MEAN] - risk[MIN])
        return operation_time

    def calculate_probability_risk(self, operation):
        sum_probability = 0.0
        probably_risk = {}
        keys = operation.keys()
        for key in sorted(keys):
            risk = operation.get(key)
            sum_probability += risk[NORMALIZATION_FACTOR]
            probably_risk[key] = sum_probability
        return probably_risk

    def calculate_distribution_densities(self):
        delta_tau = self.max_operation_time / self.number_distribution_density_intervals
        distribution_densities = {}
        for i in range(1, len(self.technological_route) + 1):
            operation = self.technological_route[i]
            distribution_density = self.initialization_distribution_density()
            for j in range(self.number_distribution_density_intervals):
                operation_time = j * delta_tau
                distribution_density[X][j] = operation_time
                distribution_density[Y][j] = self.calculate_distribution_density_value(operation, operation_time)
            distribution_densities[i] = distribution_density
        return distribution_densities

    def calculate_distribution_density_value(self, operation, operation_time):
        distribution_density_value = 0.0
        mean0 = operation.get(0)[MEAN]
        std0 = operation.get(0)[STD]
        for k in range(len(operation)):
            risk = operation.get(k)
            if risk is None:
                pass
            else:
                mean = risk[MEAN] + self.add_mean_risk0(k, mean0)
                std = risk[STD] + self.add_mean_risk0(k, std0)
                if risk.get(DISTRIBUTION_DENSITY) == NORMAL_DISTRIBUTION:
                    distribution_density_value \
                        += risk[NORMALIZATION_FACTOR] * normal_distribution(operation_time, mean, std)
                if risk.get(DISTRIBUTION_DENSITY) == UNIFORM_DISTRIBUTION:
                    distribution_density_value \
                        += risk[NORMALIZATION_FACTOR] * uniform_distribution(operation_time, mean,
                                                                             risk[MIN])  # ???  risk[MIN]
        return distribution_density_value

    def initialization_distribution_density(self):
        distribution_density = pd.DataFrame()
        distribution_density[X] = [0.0] * self.number_distribution_density_intervals
        distribution_density[Y] = [0.0] * self.number_distribution_density_intervals
        return distribution_density

    def initialization_operation_times(self):
        operation_times = pd.DataFrame()
        operation_times[X] = [0.0] * self.number_operation_time
        operation_times[Y] = [0.0] * self.number_operation_time
        return operation_times

    def initialization_technological_path(self):
        technological_path = pd.DataFrame()
        size = len(self.technological_route) + 1
        technological_path[X] = [0.0] * size
        technological_path["Xmin"] = [0.0] * size
        technological_path[Y] = [0.0] * size
        return technological_path

    @staticmethod
    def add_mean_risk0(k, mean0):
        return mean0 if k > 0 else 0.0

    @staticmethod
    def add_std_risk0(k, std0):
        return std0 if k > 0 else 0.0
