import copy

from pom.stochastic03.Dimensionless.ApproximateType import ApproximateType
from pom.stochastic03.utils.Constants import FLOW, TIME


class ApproximateDimension:

    def __init__(self, dim, approximate_type):
        self.dim = dim
        self.dim_flow_mean = dim[FLOW].mean()
        self.dim_flow_std = dim[FLOW].std()

        if approximate_type == ApproximateType.STOCHASTIC_TELEGRAPH_WAVE:
            self.approximate_dim, self.approximate_dim_mean, self.approximate_dim_std\
                = self.approximate_stochastic_telegraph_wave()
        elif approximate_type == ApproximateType.NONE:
            self.approximate_dim, self.approximate_dim_mean, self.approximate_dim_std= self.approximate_none()

        self.error_approximate_dim, self.error_approximate_dim_mean, self.error_approximate_dim_std = self.error_approximate()
        self.tau_sequence = self.create_tau_sequence_for_discrete_flow()
    def approximate_stochastic_telegraph_wave(self):
        """
        Approximates the dimension flow by rule stochastic telegraph wave.
        :return: dimensionless flow
        """
        approximate_dim = copy.copy(self.dim)
        for i in range(len(self.dim[FLOW])):
            if self.dim[FLOW][i] > self.dim_flow_mean:
                approximate_dim[FLOW][i] = self.dim_flow_mean + self.dim_flow_std
            else:
                approximate_dim[FLOW][i] = self.dim_flow_mean - self.dim_flow_std
        return approximate_dim, approximate_dim[FLOW].mean(), approximate_dim[FLOW].std()

    def approximate_none(self):
        """
        Return flow as is as.
        :return: dimensionless flow
        """
        return self.dim, self.dim[FLOW].mean(), self.dim[FLOW].std()

    def error_approximate(self):
        """
        Return flow as is as.
        :return: dimensionless flow
        """
        error_approximate_dim = copy.copy(self.approximate_dim)
        error_approximate_dim[FLOW] = self.approximate_dim[FLOW] -  self.dim[FLOW]
        return error_approximate_dim, error_approximate_dim[FLOW].mean(), error_approximate_dim[FLOW].std()

    def create_tau_sequence_for_discrete_flow(self):
        """
        Creates tau sequence for the flow.
        :return: tau sequence for the flow.
        """
        temp_tau_sequence = copy.copy(self.approximate_dim[FLOW])
        count = 0
        temp_tau_sequence[count] = self.approximate_dim[TIME][0]
        for i in range(1, len(self.approximate_dim[FLOW])):
            if self.approximate_dim[FLOW][i] != self.approximate_dim[FLOW][i-1]:
                count += 1
                temp_tau_sequence[count] = self.approximate_dim[TIME][i]

        tau_sequence = [0.0] * count
        for i in range(count):
            tau_sequence[i] = temp_tau_sequence[i+1]-temp_tau_sequence[i]
        return tau_sequence

    def get_approximate_dim(self) -> object:
        """
        Returns approximate flow.
        :return: approximate flow.
        """
        return self.approximate_dim

    def get_error_approximate_dim(self) -> object:
        """
        Returns error approximate of the flow.
        :return: error approximate of the flow.
        """
        return self.error_approximate_dim

    def get_tau_sequence(self) -> object:
        """
        Returns tau sequence for the flow.
        :return: tau sequence for the flow.
        """
        return self.tau_sequence
