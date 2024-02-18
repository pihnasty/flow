import copy
from statistics import mean

import pandas as pd
import random

from pom.stochastic03.Dimensionless.ApproximateDimension import ApproximateDimension
from pom.stochastic03.Dimensionless.ApproximateType import ApproximateType
from pom.stochastic03.utils.Constants import FLOW, TIME
from pom.stochastic03.utils.progress import progress


class Generator:

    def __init__(self, dim: object, approximate_type: object, number_of_initial_intervals_to_generate):
        self.dim = dim
        self.dim_flow_mean = dim[FLOW].mean()
        self.dim_flow_std = dim[FLOW].std()
        self.dim_number_examples = len(dim[FLOW])
        self.long_number_examples = number_of_initial_intervals_to_generate * self.dim_number_examples

        if approximate_type == ApproximateType.STOCHASTIC_TELEGRAPH_WAVE:
            self.generated_dim, self.generated_dim_mean, self.generated_dim_std\
                = self.generate_stochastic_telegraph_wave()
        elif approximate_type == ApproximateType.NONE:
            self.generated_dim, self.generated_dim_mean, self.generated_dim_std = self.generate_none()

        self.tau_sequence = self.create_tau_sequence_for_discrete_flow(self.generated_dim)

    def generate_stochastic_telegraph_wave(self):
        """
        Generates the dimension flow by rule stochastic telegraph wave.
        :return: generated dimensionless flow.
        """
        approximate_dimension = ApproximateDimension(self.dim, ApproximateType.STOCHASTIC_TELEGRAPH_WAVE)
        tau_mean = mean(approximate_dimension.get_tau_sequence())

        # https://docs.python.org/3/library/random.html
        temp = pd.DataFrame()
        temp[TIME] = [0.0] * self.long_number_examples
        temp[FLOW] = [0.0] * self.long_number_examples

        random_time = random
        random_time.seed(10)  # (num_random.randint)

        tau = self.dim[TIME][0]
        tau_generated_sum = tau + random_time.expovariate(1.0 / tau_mean)
        flow_generated_value = self.dim_flow_std

        delta_tau = (max(self.dim[TIME]) - min(self.dim[TIME])) / (self.dim_number_examples -1)

        for num in range(self.long_number_examples):
            tau = self.dim[TIME][num] if num < self.dim_number_examples else tau + delta_tau

            if tau > tau_generated_sum:
                tau_generated_sum = tau_generated_sum + random_time.expovariate(1.0 / tau_mean)
                flow_generated_value = - flow_generated_value

            temp[TIME][num] = tau
            temp[FLOW][num] = flow_generated_value

            progress(num, self.long_number_examples, 'generate_stochastic_telegraph_wave')
        progress(self.long_number_examples, self.long_number_examples, 'generate_stochastic_telegraph_wave\n')
        return temp, temp[FLOW].mean(), temp.std()

    def generate_none(self):
        """
        Return flow as is as.
        :return: dimensionless flow
        """
        return self.dim, self.dim[FLOW].mean(), self.dim[FLOW].std()

    def create_tau_sequence_for_discrete_flow(self, source):
        """
        Creates tau sequence for the flow.
        :return: tau sequence for the flow.
        """
        temp_tau_sequence = copy.copy(source[FLOW])
        count = 0
        temp_tau_sequence[count] = source[TIME][0]
        for i in range(1, len(source[FLOW])):
            if source[FLOW][i] != source[FLOW][i-1]:
                count += 1
                temp_tau_sequence[count] = source[TIME][i]

        tau_sequence = [0.0] * count
        for i in range(count):
            tau_sequence[i] = temp_tau_sequence[i+1]-temp_tau_sequence[i]
        return tau_sequence

    def get_generated_dim(self) -> object:
        """
        Returns approximate flow.
        :return: approximate flow.
        """
        return self.generated_dim

    def get_tau_sequence(self) -> object:
        """
        Returns tau sequence for the flow.
        :return: tau sequence for the flow.
        """
        return self.tau_sequence

