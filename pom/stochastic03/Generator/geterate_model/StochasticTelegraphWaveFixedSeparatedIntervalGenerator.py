import random

import pandas as pd

from constants.flow_constants import FLOW, TIME
from io_utils.console.progress import progress


class StochasticTelegraphWaveFixedSeparatedIntervalGenerator:

    def __init__(self, dim: object, long_number_examples, approximate_number_of_intervals):
        self.dim = dim
        self.long_number_examples = long_number_examples
        self.approximate_number_of_intervals = approximate_number_of_intervals
        self.dim_number_examples = len(dim[FLOW])

    def get_param(self):
        """
        Generates the dimension flow by rule stochastic telegraph wave.
        :return: generated dimensionless flow.
        """
        flow_mean = self.dim[FLOW].mean()
        flow_std = self.dim[FLOW].std()
        flow_max = self.dim[FLOW].max()
        flow_min = self.dim[FLOW].min()

        # https://docs.python.org/3/library/random.html
        temp = pd.DataFrame()
        temp[TIME] = [0.0] * self.long_number_examples
        temp[FLOW] = [0.0] * self.long_number_examples

        random_flow = random
        random_flow.seed(50)  # (num_random.randint)
        generated_delta_tau = (self.dim[TIME].max() - self.dim[TIME].min()) / self.approximate_number_of_intervals

        tau = self.dim[TIME][0]
        tau_generated_sum = tau + generated_delta_tau
        flow_generated_value = random_flow.gauss(flow_mean, flow_std)

        delta_tau = (max(self.dim[TIME]) - min(self.dim[TIME])) / (self.dim_number_examples - 1)

        for num in range(self.long_number_examples):
            tau = self.dim[TIME][num] if num < self.dim_number_examples else tau + delta_tau

            if tau > tau_generated_sum:
                tau_generated_sum = tau_generated_sum + generated_delta_tau
                flow_generated_value = random_flow.gauss(flow_mean, flow_std)
                while not (flow_min <= flow_generated_value <= flow_max):
                    flow_generated_value = random_flow.gauss(flow_mean, flow_std)

            temp[TIME][num] = tau
            temp[FLOW][num] = flow_generated_value

            progress(num, self.long_number_examples, 'generate_stochastic_telegraph_wave_fixed_separated_interval')
        progress(self.long_number_examples, self.long_number_examples,
                 'generate_stochastic_telegraph_wave_fixed_separated_interval\n')
        return temp, temp[FLOW].mean(), temp.std()
