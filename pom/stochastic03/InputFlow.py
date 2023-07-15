import math

from pom.stochastic03.InitData.inizialize_data02 import experiments
import pandas as pd
import pom.stochastic03.utils.show as show
import copy
from pom.stochastic03.utils.progress import progress

class InputFlow:
    def __init__(self, experiment_name):
        self.experiment = experiments[experiment_name] # experiment: experiment conditions.
        self.create_project_structure()
        self.initial_dimension_flow = self.load_data()

        self.check_outliers()

        self.numberExamples = self.initial_dimension_flow.shape[0]
        self.transform_initial_dimension_to_dimensionless()
        self.transform_initial_dimension_to_dimensionless2()
        self.gamma1_multiply_gamma2()

        self.transform_initial_dimension_to_dimensionless2_correct()
        self.gamma1_multiply_gamma2_correct()
        self.paremeter_model_save()

    def create_project_structure(self):
        project_structure = self.experiment["project_structure"]
        self.file_name = project_structure["file_name"]
        self.files_category = project_structure["files_category"] + '/'
        self.result_data_structure = project_structure["result_data_structure"]

    def load_data(self):
        return pd.read_csv(self.files_category + self.file_name, sep=";", decimal=',')

    def check_outliers(self):
        initial_dimension_flow_mean = self.initial_dimension_flow['flow'].mean()
        for n in range(len(self.initial_dimension_flow['flow'])):
            value = self.initial_dimension_flow['flow'][n]
            if(value < initial_dimension_flow_mean * 0.2):
                self.initial_dimension_flow['flow'][n] = initial_dimension_flow_mean

    def transform_initial_dimension_to_dimensionless(self):
        tMin = self.initial_dimension_flow['time'].min()
        tMax = self.initial_dimension_flow['time'].max()

        self.initial_dimension_flow_mean = self.initial_dimension_flow['flow'].mean()
        self.initial_dimension_flow_std = self.initial_dimension_flow['flow'].std()
        self.initial_dimensionless_flow = copy.copy(self.initial_dimension_flow)
        self.initial_dimensionless_flow['flow'] = (self.initial_dimension_flow['flow']) / self.initial_dimension_flow_mean
        self.initial_dimensionless_flow['time'] = (self.initial_dimension_flow['time'] - tMin) / (tMax - tMin)

    def transform_initial_dimension_to_dimensionless2(self):
        print ("\ntransform_initial_dimension_to_dimensionless2 ")

        tMin = self.initial_dimension_flow['time'].min()
        tMax = self.initial_dimension_flow['time'].max()

        initial_dimension_flow_mean = self.initial_dimension_flow['flow'].mean()
        initial_dimension_flow_std = self.initial_dimension_flow['flow'].std()
        self.initial_dimensionless_flow2 = copy.copy(self.initial_dimension_flow)
        self.initial_dimensionless_flow2['time'] =  copy.copy((self.initial_dimension_flow['time'] - tMin) / (tMax - tMin) *2.0)
        self.initial_dimensionless_flow2['flow'] =  copy.copy(self.initial_dimension_flow['flow'] / initial_dimension_flow_mean)

        self.dimensionless_flow2_mean = self.initial_dimensionless_flow2['flow'].mean()
        self.dimensionless_flow2_std = self.initial_dimensionless_flow2['flow'].std()

        # == initial_dimensionless_flow2_first_part ===============================================================
        self.initial_dimensionless_flow2_first_part = pd.DataFrame()
        size = round(len(self.initial_dimensionless_flow2["time"])/2 - 1)
        self.initial_dimensionless_flow2_first_part["flow"]= [0.0] * size
        self.initial_dimensionless_flow2_first_part["time"]= [0.0] * round(size)

        for n in range( len(self.initial_dimensionless_flow2_first_part["time"])):
            self.initial_dimensionless_flow2_first_part["flow"][n] = self.initial_dimensionless_flow2['flow'][n]
            self.initial_dimensionless_flow2_first_part["time"][n] = self.initial_dimensionless_flow2['time'][n]

        self.initial_dimensionless_flow2_first_part_mean = self.initial_dimensionless_flow2_first_part["flow"].mean()
        self.initial_dimensionless_flow2_first_part_std = self.initial_dimensionless_flow2_first_part["flow"].std()

        # == initial_dimensionless_flow2_second_part ===============================================================
        self.initial_dimensionless_flow2_second_part = pd.DataFrame()
        self.initial_dimensionless_flow2_second_part["flow"]= [0.0] * round(size)
        self.initial_dimensionless_flow2_second_part["time"]= [0.0] * round(size)

        for n in range( len(self.initial_dimensionless_flow2_second_part["time"])):
            self.initial_dimensionless_flow2_second_part["flow"][n] = self.initial_dimensionless_flow2['flow'][n + size]
            self.initial_dimensionless_flow2_second_part["time"][n] = self.initial_dimensionless_flow2['time'][n + size]

        self.initial_dimensionless_flow2_second_part_mean = self.initial_dimensionless_flow2_second_part["flow"].mean()
        self.initial_dimensionless_flow2_second_part_std = self.initial_dimensionless_flow2_second_part["flow"].std()

    def transform_initial_dimension_to_dimensionless2_correct(self):
        print ("\ntransform_initial_dimension_to_dimensionless2_correction ")
        self.initial_dimensionless_flow2_correct = copy.copy(self.initial_dimensionless_flow2)

        size_initial_dimensionless_flow2 = len(self.initial_dimensionless_flow2["time"])

        self.b1_corect = (self.initial_dimensionless_flow2_first_part_mean - self.dimensionless_flow2_mean) *math.pi /2.0

        # self.b1_corect = 0.0
        # self.a1_corect = 0.0
        # delta_tau = (self.initial_dimensionless_flow2["time"].max() - self.initial_dimensionless_flow2["time"].min()) / size_initial_dimensionless_flow2
        # for n in range(size_initial_dimensionless_flow2):
        #     tau = self.initial_dimensionless_flow2['time'][n]
        #     self.b1_corect = self.b1_corect + self.initial_dimensionless_flow2['flow'][n] * math.sin(math.pi * tau) * delta_tau
        #     self.a1_corect = self.a1_corect + self.initial_dimensionless_flow2['flow'][n] * math.cos(math.pi * tau) * delta_tau

        g_g = 0.0
        g_cos = 0.0

        size_correction = round((size_initial_dimensionless_flow2 - 1) / 2)
        for n in range(size_correction):
            tau_first = self.initial_dimensionless_flow2['time'][n]
            g_first = self.initial_dimensionless_flow2['flow'][n] - self.dimensionless_flow2_mean - self.b1_corect * math.sin(math.pi *tau_first)

            tau_second = self.initial_dimensionless_flow2['time'][n + size_correction]
            g_second = self.initial_dimensionless_flow2['flow'][n + size_correction] - self.dimensionless_flow2_mean - self.b1_corect * math.sin(math.pi * tau_second)

            g_g = g_g + g_first * g_first - g_second * g_second
            g_cos = g_cos + ( g_first * math.cos( math.pi *tau_first) - g_second * math.cos(math.pi *tau_second) )

        self.a1_corect = g_g / g_cos / 2
        # ========================================================================================================
        # self.a1_corect = 0.0
        # ========================================================================================================
        for n in range(size_initial_dimensionless_flow2):
            tau = self.initial_dimensionless_flow2['time'][n]
            self.initial_dimensionless_flow2_correct['flow'][n] = self.initial_dimensionless_flow2_correct['flow'][n] \
                  - self.a1_corect * math.cos( math.pi *tau) - self.b1_corect * math.sin(math.pi *tau)

        self.dimensionless_flow2_correct_mean = self.initial_dimensionless_flow2_correct['flow'].mean()
        self.dimensionless_flow2_correct_std = self.initial_dimensionless_flow2_correct['flow'].std()

        # == initial_dimensionless_flow2_first_part_correct ============================================================
        self.initial_dimensionless_flow2_first_part_correct = pd.DataFrame()
        size = round(len(self.initial_dimensionless_flow2_correct["time"])/2 - 1)
        self.initial_dimensionless_flow2_first_part_correct["flow"]= [0.0] * size
        self.initial_dimensionless_flow2_first_part_correct["time"]= [0.0] * size

        for n in range( len(self.initial_dimensionless_flow2_first_part_correct["time"])):
            self.initial_dimensionless_flow2_first_part_correct["flow"][n] = self.initial_dimensionless_flow2_correct['flow'][n]
            self.initial_dimensionless_flow2_first_part_correct["time"][n] = self.initial_dimensionless_flow2_correct['time'][n]

        self.initial_dimensionless_flow2_first_part_correct_mean = self.initial_dimensionless_flow2_first_part_correct["flow"].mean()
        self.initial_dimensionless_flow2_first_part_correct_std = self.initial_dimensionless_flow2_first_part_correct["flow"].std()

        # == initial_dimensionless_flow2_second_part_correct ===========================================================
        self.initial_dimensionless_flow2_second_part_correct = pd.DataFrame()
        self.initial_dimensionless_flow2_second_part_correct["flow"]= [0.0] * size
        self.initial_dimensionless_flow2_second_part_correct["time"]= [0.0] * size

        for n in range( len(self.initial_dimensionless_flow2_second_part_correct["time"])):
            self.initial_dimensionless_flow2_second_part_correct["flow"][n] = self.initial_dimensionless_flow2_correct['flow'][n + size]
            self.initial_dimensionless_flow2_second_part_correct["time"][n] = self.initial_dimensionless_flow2_correct['time'][n + size]

        self.initial_dimensionless_flow2_second_part_correct_mean = self.initial_dimensionless_flow2_second_part_correct["flow"].mean()
        self.initial_dimensionless_flow2_second_part_correct_std = self.initial_dimensionless_flow2_second_part_correct["flow"].std()

    def gamma1_multiply_gamma2(self):
        print ("gamma1_multiply_gamma2 ")
        period = self.experiment["period"]
        self.gamma1_gamma2 = pd.DataFrame()
        self.gamma1_gamma2['time'] = [0.0] * round((self.numberExamples/2-1)/period)
        self.gamma1_gamma2['gg1'] = [0.0] * round((self.numberExamples/2-1)/period)

        size = len(self.initial_dimensionless_flow2['time'])
        tau_max = self.initial_dimensionless_flow2['time'].max()
        tau_min = self.initial_dimensionless_flow2['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.gamma1_gamma2['time'])
        count_2 = round((size-1)/2)

        for n_v in range(count_1):
            value = 0.0
            tau = self.initial_dimensionless_flow2['time'][n_v * period]
            for n_tau in range(count_2):
                g1 = self.initial_dimensionless_flow2['flow'][n_tau]
                g2 = self.initial_dimensionless_flow2['flow'][n_tau + n_v *period]
                value = value + g1 * g2 * delta_tau
            self.gamma1_gamma2['time'][n_v] = tau
            self.gamma1_gamma2['gg1'][n_v] = value
            progress(n_v, count_1)
        progress(count_1, count_1)

    def gamma1_multiply_gamma2_correct(self):
        print ("gamma1_multiply_gamma2_correct ")
        period = self.experiment["period"]
        self.gamma1_gamma2_correct = pd.DataFrame()
        self.gamma1_gamma2_correct['time'] = [0.0] * round((self.numberExamples/2-1)/period)
        self.gamma1_gamma2_correct['gg1'] = [0.0] * round((self.numberExamples/2-1)/period)

        size = len(self.initial_dimensionless_flow2_correct['time'])
        tau_max = self.initial_dimensionless_flow2_correct['time'].max()
        tau_min = self.initial_dimensionless_flow2_correct['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.gamma1_gamma2_correct['time'])
        count_2 = round((size-1)/2)

        for n_v in range(count_1):
            value = 0.0
            tau = self.initial_dimensionless_flow2_correct['time'][n_v * period]
            for n_tau in range(count_2):
                g1 = self.initial_dimensionless_flow2_correct['flow'][n_tau]
                g2 = self.initial_dimensionless_flow2_correct['flow'][n_tau + n_v *period]
                value = value + g1 * g2 * delta_tau
            self.gamma1_gamma2_correct['time'][n_v] = tau
            self.gamma1_gamma2_correct['gg1'][n_v] = value
            progress(n_v, count_1)
        progress(count_1, count_1)

    def execute_initial_correlation_part_first(self):
        print ("\nexecute_initial_correlation_part_first ")
        period = self.experiment["period"]
        self.initial_correlation_part_first = pd.DataFrame()
        self.initial_correlation_part_first['time'] = [0.0] * round((self.numberExamples/2-1)/period)
        self.initial_correlation_part_first['correlation_part_first'] = [0.0] * round((self.numberExamples/2-1)/period)

        size = len(self.initial_dimensionless_flow2['time'])
        tau_max = self.initial_dimensionless_flow2['time'].max()
        tau_min = self.initial_dimensionless_flow2['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.initial_correlation_part_first['time'])
        count_2 = round((size-1)/2)

        for n_v in range(count_1):
            value = 0.0
            tau = self.initial_dimensionless_flow2['time'][n_v * period]
            for n_tau in range(count_2):
                g1 = self.initial_dimensionless_flow2['flow'][n_tau]  - self.initial_dimensionless_flow2_first_part_mean
                g2 = self.initial_dimensionless_flow2['flow'][n_tau + n_v *period]  - self.initial_dimensionless_flow2_first_part_mean
                value = value + g1 * g2 * delta_tau
            self.initial_correlation_part_first['time'][n_v] = tau
            self.initial_correlation_part_first['correlation_part_first'][n_v] = (value
                                              # - self.initial_dimensionless_flow2_first_part_mean * self.initial_dimensionless_flow2_first_part_mean
                                              ) \
                / self.initial_dimensionless_flow2_first_part_std / self.initial_dimensionless_flow2_first_part_std
            progress(n_v, count_1)
        progress(count_1, count_1)

    def execute_initial_correlation_part_first_correct(self):
        print ("\nexecute_initial_correlation_part_first_correct ")
        period = self.experiment["period"]
        self.initial_correlation_part_first_correct = pd.DataFrame()
        self.initial_correlation_part_first_correct['time'] = [0.0] * round((self.numberExamples/2-1)/period)
        self.initial_correlation_part_first_correct['correlation_part_first_correct'] = [0.0] * round((self.numberExamples/2-1)/period)

        size = len(self.initial_dimensionless_flow2_correct['time'])
        tau_max = self.initial_dimensionless_flow2_correct['time'].max()
        tau_min = self.initial_dimensionless_flow2_correct['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.initial_correlation_part_first_correct['time'])
        count_2 = round((size-1)/2)

        for n_v in range(count_1):
            value = 0.0
            tau = self.initial_dimensionless_flow2_correct['time'][n_v * period]
            for n_tau in range(count_2):
                g1_correct = self.initial_dimensionless_flow2_correct['flow'][n_tau] - self.initial_dimensionless_flow2_first_part_correct_mean
                g2_correct = self.initial_dimensionless_flow2_correct['flow'][n_tau + n_v *period] - self.initial_dimensionless_flow2_first_part_correct_mean
                value = value + g1_correct * g2_correct * delta_tau
            self.initial_correlation_part_first_correct['time'][n_v] = tau
            self.initial_correlation_part_first_correct['correlation_part_first_correct'][n_v] = (value
                                                                                  # -( self.initial_dimensionless_flow2_first_part_mean * (1-tau) +
                                                                                  #   self.dimensionless_flow2_mean *  tau )
                                                                                  #  * ( self.initial_dimensionless_flow2_first_part_mean * (1-tau) +
                                                                                  #      self.dimensionless_flow2_mean  * tau )
                                                                                  ) \
                                                                                 / self.initial_dimensionless_flow2_first_part_correct_std / self.initial_dimensionless_flow2_first_part_correct_std
            progress(n_v, count_1)
        progress(count_1, count_1)


    def execute_initial_correlation_part_second(self):
        print ("\nexecute_initial_correlation_part_second ")
        period = self.experiment["period"]
        self.initial_correlation_part_second = pd.DataFrame()
        self.initial_correlation_part_second['time'] = [0.0] * round((self.numberExamples/2-1)/period)
        self.initial_correlation_part_second['correlation_part_second'] = [0.0] * round((self.numberExamples/2-1)/period)

        size = len(self.initial_dimensionless_flow2['time'])
        tau_max = self.initial_dimensionless_flow2['time'].max()
        tau_min = self.initial_dimensionless_flow2['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.initial_correlation_part_second['time'])
        count_2 = round((size-1)/2)

        for n_v in range(count_1):
            value = 0.0
            tau = self.initial_dimensionless_flow2['time'][n_v * period]
            for n_tau in range(count_2):
                g1 = self.initial_dimensionless_flow2['flow'][n_tau + count_2] - self.initial_dimensionless_flow2_second_part_mean
                g2 = self.initial_dimensionless_flow2['flow'][n_tau + count_2 - n_v *period] - self.initial_dimensionless_flow2_second_part_mean
                value = value + g1 * g2 * delta_tau
            self.initial_correlation_part_second['time'][n_v] = tau
            self.initial_correlation_part_second['correlation_part_second'][n_v] = (value
                                                                                  # -( self.initial_dimensionless_flow2_first_part_mean * (1-tau) +
                                                                                  #   self.dimensionless_flow2_mean *  tau )
                                                                                  #  * ( self.initial_dimensionless_flow2_first_part_mean * (1-tau) +
                                                                                  #      self.dimensionless_flow2_mean  * tau )
                                                                                  ) \
                                                                                 / self.initial_dimensionless_flow2_second_part_std / self.initial_dimensionless_flow2_second_part_std
            progress(n_v, count_1)
        progress(count_1, count_1)

    def execute_initial_correlation_part_second_correct(self):
        print ("\nexecute_initial_correlation_part_second_correct ")
        period = self.experiment["period"]
        self.initial_correlation_part_second_correct = pd.DataFrame()
        self.initial_correlation_part_second_correct['time'] = [0.0] * round((self.numberExamples/2-1)/period)
        self.initial_correlation_part_second_correct['correlation_part_second_correct'] = [0.0] * round((self.numberExamples/2-1)/period)

        size = len(self.initial_dimensionless_flow2_correct['time'])
        tau_max = self.initial_dimensionless_flow2_correct['time'].max()
        tau_min = self.initial_dimensionless_flow2_correct['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.initial_correlation_part_second['time'])
        count_2 = round((size-1)/2)

        for n_v in range(count_1):
            value = 0.0
            tau = self.initial_dimensionless_flow2_correct['time'][n_v * period]
            for n_tau in range(count_2):
                g1_correct = self.initial_dimensionless_flow2_correct['flow'][n_tau + count_2] - self.initial_dimensionless_flow2_second_part_correct_mean
                g2_correct = self.initial_dimensionless_flow2_correct['flow'][n_tau + count_2 - n_v *period] - self.initial_dimensionless_flow2_second_part_correct_mean
                value = value + g1_correct * g2_correct * delta_tau
            self.initial_correlation_part_second_correct['time'][n_v] = tau
            self.initial_correlation_part_second_correct['correlation_part_second_correct'][n_v] = (value
                                                                                    # -( self.initial_dimensionless_flow2_first_part_mean * (1-tau) +
                                                                                    #   self.dimensionless_flow2_mean *  tau )
                                                                                    #  * ( self.initial_dimensionless_flow2_first_part_mean * (1-tau) +
                                                                                    #      self.dimensionless_flow2_mean  * tau )
                                                                                    ) \
                                                                                   / self.initial_dimensionless_flow2_second_part_correct_std / self.initial_dimensionless_flow2_second_part_correct_std
            progress(n_v, count_1)
        progress(count_1, count_1)



    def initial_dimension_data_show(self):
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_result"]
        path = result_data + self.file_name + '/' + initial_data_result

        initial_dimension_flows = [self.initial_dimension_flow['time'].values, self.initial_dimension_flow['flow'].values]
        show.common_line(self.experiment, path, initial_dimension_flows, "flow_line_", "initial_flow_line")
        initial_dimension_flows_for_hist = [self.initial_dimension_flow['time'].values, self.initial_dimension_flow['flow'].values]
        show.common_hist(self.experiment, path, initial_dimension_flows_for_hist, "flow_hist_", "initial_flow_hist")
        # initial_dimension_flows_for_hist = [self.initial_dimension_flow['time'].values, self.initial_dimension_flow['time'].values]
        # show.common_hist(self.experiment, path, initial_dimension_flows_for_hist, "flow_hist_", "initial_flow_hist")

    def initial_dimensionless_data_show(self):
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_dimensionless_result"]
        path = result_data + self.file_name + '/' + initial_data_result

        initial_dimensionless_flows = [self.initial_dimensionless_flow['time'].values, self.initial_dimensionless_flow['flow'].values]
        show.common_line(self.experiment, path, initial_dimensionless_flows, "flow_line_", "initial_dimensionless_flow_line")
        initial_dimensionless_flows_for_hist = [self.initial_dimensionless_flow['time'].values, self.initial_dimensionless_flow['flow'].values]
        show.common_hist(self.experiment, path, initial_dimensionless_flows_for_hist, "flow_hist_", "initial_dimensionless_flow_hist")
        # initial_dimensionless_flows_for_hist = [self.initial_dimensionless_flow['time'].values, self.initial_dimensionless_flow['time'].values]
        # show.common_hist(self.experiment, path, initial_dimensionless_flows_for_hist, "flow_hist_", "initial_flow_hist")

    def initial_dimensionless_data_show2(self):
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_dimensionless_result2"]
        path = result_data + self.file_name + '/' + initial_data_result

        initial_dimensionless_flows2 = [self.initial_dimensionless_flow2['time'].values, self.initial_dimensionless_flow2['flow'].values]
        show.common_line(self.experiment, path, initial_dimensionless_flows2, "flow_line_", "initial_dimensionless_flow_line2")
        initial_dimensionless_flows_for_hist2 = [self.initial_dimensionless_flow2['time'].values, self.initial_dimensionless_flow2['flow'].values]
        show.common_hist(self.experiment, path, initial_dimensionless_flows_for_hist2, "flow_hist_", "initial_dimensionless_flow_hist2")

    def initial_dimensionless_data_correct_show2(self):
        print ("\ninitial_dimensionless_data_correct_show2 ")
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_dimensionless_result2"]
        path = result_data + self.file_name + '/' + initial_data_result

        initial_dimensionless_flows2_correct = [self.initial_dimensionless_flow2_correct['time'].values, self.initial_dimensionless_flow2_correct['flow'].values]
        show.common_line(self.experiment, path, initial_dimensionless_flows2_correct, "flow_line_correct_", "initial_dimensionless_flow_line2")
        initial_dimensionless_flows_for_hist2_correct = [self.initial_dimensionless_flow2_correct['time'].values, self.initial_dimensionless_flow2_correct['flow'].values]
        show.common_hist(self.experiment, path, initial_dimensionless_flows_for_hist2_correct, "flow_hist_correct_", "initial_dimensionless_flow_hist2")

    def g_g2_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        gamma1_gamma2s = [self.gamma1_gamma2['time'].values, self.gamma1_gamma2['gg1'].values]
        show.common_line(self.experiment, path, gamma1_gamma2s, "gamma1_gamma2_", "g_g2_line")

    def g_g2_correct_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        gamma1_gamma2s_correct = [self.gamma1_gamma2_correct['time'].values, self.gamma1_gamma2_correct['gg1'].values]
        show.common_line(self.experiment, path, gamma1_gamma2s_correct, "gamma1_gamma2_correct_", "g_g2_line")

    def initial_correlation_part_first_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        initial_correlation_part_firsts = [self.initial_correlation_part_first['time'].values, self.initial_correlation_part_first['correlation_part_first'].values]
        show.common_line(self.experiment, path, initial_correlation_part_firsts, "initial_correlation_part_first_", "initial_correlation_part_first_line")

    def initial_correlation_part_first_correct_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        initial_correlation_part_firsts_correct = [self.initial_correlation_part_first_correct['time'].values, self.initial_correlation_part_first_correct['correlation_part_first_correct'].values]
        show.common_line(self.experiment, path, initial_correlation_part_firsts_correct, "initial_correlation_part_first_correct_", "initial_correlation_part_first_line")

    def initial_correlation_part_second_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        initial_correlation_part_seconds = [self.initial_correlation_part_second['time'].values, self.initial_correlation_part_second['correlation_part_second'].values]
        show.common_line(self.experiment, path, initial_correlation_part_seconds, "initial_correlation_part_second_", "initial_correlation_part_first_line")

    def initial_correlation_part_second_correct_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        initial_correlation_part_seconds_correct = [self.initial_correlation_part_second_correct['time'].values, self.initial_correlation_part_second_correct['correlation_part_second_correct'].values]
        show.common_line(self.experiment, path, initial_correlation_part_seconds_correct, "initial_correlation_part_second_correct_", "initial_correlation_part_first_line")

    def paremeter_model_save(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path_file = result_data + self.file_name + "\ModelDescription.txt"

        file = open(path_file, "w")
        file.write("Model name:               " + self.file_name)
        file.write("\n\n")
        file.write("Dimension parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimension_flow['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimension_flow['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimension_flow['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimension_flow['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimension_flow['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimension_flow['flow'].std()))
        file.write("\n\n")

        file.write("Dimensionless parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimensionless_flow['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimensionless_flow['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimensionless_flow['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimensionless_flow['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimensionless_flow['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimensionless_flow['flow'].std()))
        file.write("\n\n")

        file.write("Dimensionless first part parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimensionless_flow2_first_part['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimensionless_flow2_first_part['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimensionless_flow2_first_part['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimensionless_flow2_first_part['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimensionless_flow2_first_part['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimensionless_flow2_first_part['flow'].std()))
        file.write("\n\n")

        file.write("Dimensionless second part parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimensionless_flow2_second_part['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimensionless_flow2_second_part['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimensionless_flow2_second_part['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimensionless_flow2_second_part['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimensionless_flow2_second_part['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimensionless_flow2_second_part['flow'].std()))
        file.write("\n\n\n")

        file.write("Corrected Dimensionless Flow   =============================================")
        file.write("\n")
        file.write("Dimensionless corrected Fourie coeffitient:               ")
        file.write("\n")
        file.write("a1         : %10.3f * cos(Pi * tau)" % (self.a1_corect))
        file.write("\n")
        file.write("b1         : %10.3f * sin(Pi * tau)" % (self.b1_corect))
        file.write("\n")

        file.write("Corrected dimensionless parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimensionless_flow2_correct['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimensionless_flow2_correct['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimensionless_flow2_correct['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimensionless_flow2_correct['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimensionless_flow2_correct['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimensionless_flow2_correct['flow'].std()))
        file.write("\n\n")

        file.write("Corrected  dimensionless first part parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimensionless_flow2_first_part_correct['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimensionless_flow2_first_part_correct['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimensionless_flow2_first_part_correct['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimensionless_flow2_first_part_correct['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimensionless_flow2_first_part_correct['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimensionless_flow2_first_part_correct['flow'].std()))
        file.write("\n\n")

        file.write("Corrected  dimensionless first part parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.3f" % (self.initial_dimensionless_flow2_second_part_correct['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.3f" % (self.initial_dimensionless_flow2_second_part_correct['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.3f" % (self.initial_dimensionless_flow2_second_part_correct['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.3f" % (self.initial_dimensionless_flow2_second_part_correct['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.3f" % (self.initial_dimensionless_flow2_second_part_correct['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.3f" % (self.initial_dimensionless_flow2_second_part_correct['flow'].std()))
        file.write("\n\n")


        file.close()