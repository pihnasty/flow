import copy

from pom.stochastic03.Dimensionless.DimensionlessType import DimensionlessType
from pom.stochastic03.utils.Constants import FLOW, TIME

class Dimensionless:

    def __init__(self, dim, dim_type):
        self.dim = dim
        self.dim_time_min = dim[TIME].min()
        self.dim_time_max = dim[TIME].max()
        self.dim_flow_mean = dim[FLOW].mean()
        self.dim_flow_std = dim[FLOW].std()

        if dim_type == DimensionlessType.STD_TIME_M1_1:
            self.dim_less, self.dim_less_mean, self.dim_less_std = self.transform_dim_to_dim_less_by_sdt()
        elif dim_type == DimensionlessType.MEAN_TIME_M1_1:
            self.dim_less, self.dim_less_mean, self.dim_less_std = self.transform_dim_to_dim_less_by_mean()

    def transform_dim_to_dim_less_by_sdt(self, min_time=-1.0, max_time=1.0):
        """
        Makes transform the dimension flow to the dimensionless flow using given rules std and time.
        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimensionless flow
        """
        dim_less = copy.copy(self.dim)
        dim_less[FLOW] = self.dim[FLOW] / self.dim_flow_std
        dim_less[TIME] = self.get_dim_less_time_on_interval(min_time, max_time)
        return dim_less, dim_less[FLOW].mean(), dim_less[FLOW].std()

    def transform_dim_to_dim_less_by_mean(self, min_time=-1.0, max_time=1.0):
        """
        Makes transform the dimension flow to the dimensionless flow using given rules mean and time.
        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimensionless flow
        """
        dim_less = copy.copy(self.dim)
        dim_less[FLOW] = self.dim[FLOW] / self.dim_flow_mean
        dim_less[TIME] = self.get_dim_less_time_on_interval(min_time, max_time)
        return dim_less, dim_less[FLOW].mean(), dim_less[FLOW].std()

    def get_dim_less_time_on_interval(self, min_time, max_time):
        """
        Creates dimension less time for the flow.

        :param min_time: The min value of the dimensionless time.
        :param max_time: The max value of the dimensionless time
        :return: dimension less time for the flow.
        """
        dim_less_time = (self.dim[TIME] - self.dim_time_min) / (self.dim_time_max - self.dim_time_min)
        return dim_less_time * (max_time + 1) + min_time

    def get_centred_dim_less(self) -> object:
        centred_dim_less = copy.copy(self.dim_less)
        centred_dim_less[FLOW] = self.dim_less[FLOW] - self.dim_less[FLOW].mean()
        return centred_dim_less

    def get_dim_less(self) -> object:
        return self.dim_less
