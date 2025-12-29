from scipy import stats

from pom.pde.flowshop_2m.operationDelay.stat_params import StatParams


class OperationDelay:
    def __init__(self, first_operation_params: StatParams, second_operation_params: StatParams,
                 first_operation_delay: StatParams):



        mean = first_operation_params.mean - second_operation_params.mean + first_operation_delay.mean
        self.std = (first_operation_params.std ** 2 + second_operation_params.std ** 2 +  first_operation_delay.std ** 2) ** 0.5
        if self.std == 0:
            sign = 1 if mean >= 0 else -1
            self.a = 1000.0 * sign  # to avoid division by zero
        else:
            self.a = mean / self.std
        self.F = stats.norm.cdf(self.a)
        self.fi = stats.norm.pdf(self.a)

    def get_delay_mean(self):
        return self.std * (self.a * self.F + self.fi)

    def get_delay_std(self):
        delay_std_squared = - self.get_delay_mean() ** 2 + self.std ** 2 * (
                (self.a ** 2 + 1.0) * self.F + self.a * self.fi
        )
        return delay_std_squared ** 0.5

    def get_a(self):
        return self.a

def get_normalized_delay_mean(a):
    return a * stats.norm.cdf(a) + stats.norm.pdf(a)

def get_normalized_delay_std(a):
    mean = get_normalized_delay_mean(a)
    delay_std_squared = - mean ** 2 + (a ** 2 + 1.0) * stats.norm.cdf(a) + a * stats.norm.pdf(a)
    return delay_std_squared ** 0.5
