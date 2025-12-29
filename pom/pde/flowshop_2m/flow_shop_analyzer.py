import pandas as pd

from io_utils.csv.csv_writer import write_multiple_matrices_to_csv, formated_write_csv
from pom.pde.Constants import RESULT_DATA, INITIAL_DATA
from pom.pde.flowshop_2m.scheduling import Scheduling
from time_utils import current_timestamp_suffix


class FlowShopAnalyzer:

    def __init__(self, route, result_data_structure, file_name):
        self.scheduling = Scheduling(route)
        self.csv_output_data_path = result_data_structure[RESULT_DATA] + '/' + file_name + '/' + result_data_structure[INITIAL_DATA]

    def calculate_operation_delays(self):
        stat_characteristics_operation_delays = self.scheduling.calculate_operation_delays()
        self.__write_stat_characteristics_operation_delays_to_csv(stat_characteristics_operation_delays)
        stat_characteristics_operation_times = self.scheduling.calculate_statistical_characteristics_operation_times()
        self.__write_stat_characteristics_operation_times_to_csv(stat_characteristics_operation_times)

        full_mean_operation_time = [0] * self.scheduling.number_of_operations
        for i in range(self.scheduling.number_of_operations):
            full_mean_operation_time[i] = stat_characteristics_operation_times['mean_operation_time'][i] + \
                                          stat_characteristics_operation_delays['means_operation_delays'][i]


        df_delays = pd.DataFrame({
            'mean_delay': stat_characteristics_operation_delays['means_operation_delays'],
            'std_delay': stat_characteristics_operation_delays['stds_operation_delays'],
            'mean_operation': stat_characteristics_operation_times['mean_operation_time'],
            'full_mean_oper': full_mean_operation_time,
            'std_operation': stat_characteristics_operation_times['std_operation_time'],
            'sum_mean_oper': stat_characteristics_operation_times['sum_mean_operation_time'],
            'sum_std_oper': stat_characteristics_operation_times['sum_std_operation_time']
        })

        path = self.csv_output_data_path + '/stat_for_plot'
        formated_write_csv(df_delays, path + "/means_final_operation_delays.csv")

        calculate_dimless_to_std_delay_operation_delays \
            = self.scheduling.calculate_dimless_to_std_delay_operation_delays()
        df_functions_of_a = pd.DataFrame({
            'a_s': calculate_dimless_to_std_delay_operation_delays['a_s'],
            'fi': calculate_dimless_to_std_delay_operation_delays['fi'],
            'F': calculate_dimless_to_std_delay_operation_delays['F'],
            'mean': calculate_dimless_to_std_delay_operation_delays['mean'],
            'std': calculate_dimless_to_std_delay_operation_delays['std']
        })

        path = self.csv_output_data_path + '/stat_for_plot'
        formated_write_csv(df_functions_of_a, path + "/df_functions_of_a.csv")

    def __write_stat_characteristics_operation_delays_to_csv(self, data):
        suf = current_timestamp_suffix()+".csv"
        path = self.csv_output_data_path + '/stat_characteristics_operation_delays'
        write_multiple_matrices_to_csv(
            data['mean_operation_delay_by_risks_without_weights'],
            path + "/mean_operation_delay_by_risks_without_weights" + suf,
        )
        write_multiple_matrices_to_csv(
            data['std_operation_delay_by_risks_without_weights'],
            path + "/std_operation_delay_by_risks_without_weights" + suf,
        )
        write_multiple_matrices_to_csv(
            data['weights_for_operation'],
            path + "/weights_for_operation" + suf,
        )
        write_multiple_matrices_to_csv(
            data['mean_operation_delay_by_risks_with_weights'],
            path + "/mean_operation_delay_by_risks_with_weights" + suf
        )
        write_multiple_matrices_to_csv(
            data['stdxx2_operation_delay_by_risks_with_weights'],
            path + "/stdxx2_operation_delay_by_risks_with_weights" + suf
        )
        write_multiple_matrices_to_csv(
            data['a_s'],
            path + "/a_s" + suf
        )

    def __write_stat_characteristics_operation_times_to_csv(self, data):
        suf = current_timestamp_suffix()+".csv"
        path = self.csv_output_data_path + '/stat_characteristics_operation_times'
        write_multiple_matrices_to_csv(
            [data['mean_operation_times_by_risks_without_weights']],
            path + "/mean_operation_times_by_risks_without_weights" + suf,
        )

        write_multiple_matrices_to_csv(
            [data['std_operation_times_by_risks_without_weights']],
            path + "/std_operation_times_by_risks_without_weights" + suf,
        )

        write_multiple_matrices_to_csv(
            [data['mean_operation_times_by_risks_with_weights']],
            path + "/mean_operation_times_by_risks_with_weights" + suf,
        )

        write_multiple_matrices_to_csv(
            [data['stdxx2_operation_times_by_risks_with_weights']],
            path + "/stdxx2_operation_times_by_risks_with_weights" + suf,
        )
