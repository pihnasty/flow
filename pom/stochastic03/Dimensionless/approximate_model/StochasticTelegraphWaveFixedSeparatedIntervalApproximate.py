import copy

import pandas as pd

from pom.stochastic03.utils.Constants import FLOW, TIME


class StochasticTelegraphWaveFixedSeparatedIntervalApproximate:
    def __init__(self, dim, number_of_interval):
        self.dim = dim
        self.number_of_interval = number_of_interval

    def get_param(self):
        """
        Approximates the dimension flow by rule stochastic telegraph wave with fixed separated interval
        (as example, minute interval).
        :return: dimensionless flow
        """
        approximate_temp_dim = copy.copy(self.dim)
        approximate_result_dim = copy.copy(self.dim)
        dim_size = len(self.dim[FLOW])

        approximate_temp_dim['TIME_bins'] = pd.cut(approximate_temp_dim[TIME], bins=self.number_of_interval,
                                                   labels=False)

        # Group by TIME_bins and calculate mean FLOW for each group
        result = approximate_temp_dim.groupby('TIME_bins').agg({FLOW: 'mean'}).reset_index()
        result.rename(columns={FLOW: 'Mean_FLOW'}, inplace=True)

        for i in range(dim_size):
            approximate_result_dim[FLOW][i] = result['Mean_FLOW'][approximate_temp_dim['TIME_bins'][i]]

        return approximate_result_dim, approximate_result_dim[FLOW].mean(), approximate_result_dim[FLOW].std()
