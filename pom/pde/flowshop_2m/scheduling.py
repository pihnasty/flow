from scipy import stats
from maths.math_util import init_by_data_frame, init_by
from pom.pde.Constants import MEAN, STD, NORMALIZATION_FACTOR
from pom.pde.flowshop_2m.operationDelay.operation_delay import OperationDelay, get_normalized_delay_mean, \
    get_normalized_delay_std
from pom.pde.flowshop_2m.operationDelay.stat_params import StatParams


class Scheduling:

    def __init__(self, route):
        self.route = route
        self.number_of_operations = len(self.route)
        self.number_of_risks = len(self.route[1])

    def calculate_operation_delays(self):
        means_operation_delays = [0] * self.number_of_operations
        stds_operation_delays = [0] * self.number_of_operations
        weights_for_operation = [None] * self.number_of_operations
        a_s = [None] * self.number_of_operations

        mean_operation_delay_by_risks_with_weights = [None] * self.number_of_operations
        stdxx2_operation_delay_by_risks_with_weights = [None] * self.number_of_operations

        mean_operation_delay_by_risks_without_weights = [None] * self.number_of_operations
        std_operation_delay_by_risks_without_weights = [None] * self.number_of_operations
        first_operation_delays \
            = init_by_data_frame({MEAN: 0.0, STD: 0.0}, self.number_of_operations, self.number_of_risks)

        for i in range(1, self.number_of_operations):
            first_operation = self.route[i]
            second_operation = self.route[i + 1]
            prev_first_operation_delay = first_operation_delays[i-1]
            current_first_operation_delay = first_operation_delays[i]

            means = init_by(0.0,self.number_of_risks)
            stds = init_by(0.0,self.number_of_risks)
            weight = init_by(0.0,self.number_of_risks)
            a = init_by(0.0,self.number_of_risks)
            means_with_weight = init_by(0.0,self.number_of_risks)
            stdsxx2_with_weight = init_by(0.0,self.number_of_risks)
            stdsxx2_operation_delay = 0.0
            for r1 in range(self.number_of_risks):
                if r1 in first_operation is not None:
                    for r2 in range(self.number_of_risks):
                        if r2 in second_operation:
                            operation_delay = OperationDelay(
                                StatParams(self.mean(first_operation, r1), self.std(first_operation, r1)),
                                StatParams(self.mean(second_operation, r2), self.std(second_operation, r2)),
                                StatParams(prev_first_operation_delay[r1][r2][MEAN], prev_first_operation_delay[r1][r2][STD])
                            )

                            current_first_operation_delay[r1][r2][MEAN] = operation_delay.get_delay_mean()
                            current_first_operation_delay[r1][r2][STD] = operation_delay.get_delay_std()
                            means[r1][r2] = current_first_operation_delay[r1][r2][MEAN]
                            stds[r1][r2] = current_first_operation_delay[r1][r2][STD]

                            weight[r1][r2] = self.weight(first_operation, second_operation, r1, r2)
                            means_with_weight[r1][r2] = weight[r1][r2] * means[r1][r2]
                            stdsxx2_with_weight[r1][r2] = weight[r1][r2] * (stds[r1][r2] ** 2.0 + means[r1][r2] ** 2.0)
                            a[r1][r2]=operation_delay.get_a()
                            means_operation_delays[i] += means_with_weight[r1][r2]
                            stdsxx2_operation_delay += stdsxx2_with_weight[r1][r2]

            mean_operation_delay_by_risks_without_weights[i]=means
            std_operation_delay_by_risks_without_weights[i] = stds
            weights_for_operation[i] = weight
            mean_operation_delay_by_risks_with_weights[i] = means_with_weight
            stdxx2_operation_delay_by_risks_with_weights[i] = stdsxx2_with_weight
            a_s[i] = a
            stds_operation_delays[i] = (stdsxx2_operation_delay - means_operation_delays[i] ** 2) ** 0.5
            first_operation_delays[i] = current_first_operation_delay

        print(f"Operation delay mean: ")
        return {
            'mean_operation_delay_by_risks_without_weights': mean_operation_delay_by_risks_without_weights,
            'std_operation_delay_by_risks_without_weights': std_operation_delay_by_risks_without_weights,
            'weights_for_operation': weights_for_operation,
            'mean_operation_delay_by_risks_with_weights': mean_operation_delay_by_risks_with_weights,
            'stdxx2_operation_delay_by_risks_with_weights': stdxx2_operation_delay_by_risks_with_weights,
            'a_s': a_s,
            'means_operation_delays': means_operation_delays,
            'stds_operation_delays': stds_operation_delays
        }

    def calculate_statistical_characteristics_operation_times(self):
        mean_operation_times_by_risks_without_weights = [None] * self.number_of_operations
        std_operation_times_by_risks_without_weights = [None] * self.number_of_operations

        mean_operation_times_by_risks_with_weights = [None] * self.number_of_operations
        stdxx2_operation_times_by_risks_with_weights = [None] * self.number_of_operations

        mean_operation_time = [0.0] * self.number_of_risks
        std_operation_time = [0.0] * self.number_of_risks
        sum_mean_operation_time = [0.0] * self.number_of_risks
        sum_std_operation_time = [0.0] * self.number_of_risks

        for i in range(0, self.number_of_operations):
            operation = self.route[i+1]
            mean_r = [0.0] * self.number_of_risks
            std_r = [0.0] * self.number_of_risks
            mean_r_with_weight = [0.0] * self.number_of_risks
            stdxx2_with_weights = [0.0] * self.number_of_risks
            stdxx2_operation_time = 0.0
            for r in range(self.number_of_risks):
                if r in operation is not None:
                    mean_r[r] = self.mean(operation, r)
                    std_r[r] = self.std(operation, r)

                    weight = operation[r][NORMALIZATION_FACTOR]

                    mean_r_with_weight[r] = weight * mean_r[r]
                    stdxx2_with_weights[r] = weight * (std_r[r] ** 2 + mean_r[r] ** 2)

                    mean_operation_time[i] += mean_r_with_weight[r]
                    stdxx2_operation_time += stdxx2_with_weights[r]

            mean_operation_times_by_risks_without_weights[i] = mean_r
            std_operation_times_by_risks_without_weights[i] = std_r

            mean_operation_times_by_risks_with_weights[i] = mean_r_with_weight
            stdxx2_operation_times_by_risks_with_weights[i] = stdxx2_with_weights
            std_operation_time[i] = (stdxx2_operation_time - mean_operation_time[i] **2) ** 0.5

        sum_mean_operation_time[0] = mean_operation_time[0]
        sum_std_operation_time[0] = std_operation_time[0]
        for i in range(1,self.number_of_operations):
            sum_mean_operation_time[i] = sum_mean_operation_time[i-1] + mean_operation_time[i]
            sum_std_operation_time[i] = (sum_std_operation_time[i-1]**2 +std_operation_time[i]**2)**0.5


        print(f"Calculate statistical characteristics operation_times.")
        return {
            'mean_operation_times_by_risks_without_weights': mean_operation_times_by_risks_without_weights,
            'std_operation_times_by_risks_without_weights': std_operation_times_by_risks_without_weights,
            'mean_operation_times_by_risks_with_weights': mean_operation_times_by_risks_with_weights,
            'stdxx2_operation_times_by_risks_with_weights': stdxx2_operation_times_by_risks_with_weights,
            'mean_operation_time': mean_operation_time,
            'std_operation_time': std_operation_time,
            'sum_mean_operation_time': sum_mean_operation_time,
            'sum_std_operation_time': sum_std_operation_time
        }

    def calculate_dimless_to_std_delay_operation_delays(self):
        length = 200
        fi = [0.0] * length
        F = [0.0] * length
        mean = [0.0] * length
        std = [0.0] * length
        a_s = [0.0] * length
        a = -10.0
        delta_a =  2.0 * abs(a)/ length

        for i in range(length):
            a_s[i] = a
            fi[i] = stats.norm.pdf(a)
            F[i] = stats.norm.cdf(a)
            mean[i] = get_normalized_delay_mean(a)
            std[i] = get_normalized_delay_std(a)
            a += delta_a

        return {
            'a_s': a_s,
            'fi': fi,
            'F': F,
            'mean': mean,
            'std': std
        }


    @staticmethod
    def weight(first_operation, second_operation, r1, r2):
        return first_operation[r1][NORMALIZATION_FACTOR] * second_operation[r2][NORMALIZATION_FACTOR]

    @staticmethod
    def mean(operation, r):
        return operation[r][MEAN] + (operation[0][MEAN] if r > 0 else 0)

    @staticmethod
    def std(operation, r):
        return operation[r][STD]
        # return (
        #         operation[r][STD] ** 2 + (operation[0][STD] if r > 0 else 0) ** 2
        # ) ** 0.5

