import math
import random

from pom.stochastic03.InitData.inizialize_data04 import experiments
import pandas as pd
import pom.stochastic03.utils.show as show
import pom.stochastic03.utils.CorrelationFunctions as cf
import copy
from pom.stochastic03.utils.progress import progress


class InputFlow04:
    __numberExamples = 0
    def __init__(self, experiment_name):
        self.experiment = experiments[experiment_name] # experiment: experiment conditions.
        self.create_project_structure()
        self.correlation_addition_time = self.experiment["correlation_addition_time"]
        self.numberExamples =0

        # self.gamma1_multiply_gamma2()
        #
        # self.transform_initial_dimension_to_dimensionless2_correct()
        # self.gamma1_multiply_gamma2_correct()


    def create_project_structure(self):
        project_structure = self.experiment["project_structure"]
        self.file_name = project_structure["file_name"]
        self.files_category = project_structure["files_category"] + '/'
        self.result_data_structure = project_structure["result_data_structure"]

    def initial_load_dimension_data(self):
        load_period = self.experiment["load_period"]
        temp = pd.read_csv(self.files_category + self.file_name, sep=";", decimal=',')
        self.initial_dimension_flow = pd.DataFrame()
        self.initial_dimension_flow['time'] = [0.0] * int(temp.shape[0]/load_period)
        self.initial_dimension_flow['flow'] = [0.0] * int(temp.shape[0]/load_period)
        self.numberExamples = self.initial_dimension_flow.shape[0]

        for i in range(self.numberExamples):
            self.initial_dimension_flow['time'][i] = temp['time'][i * load_period]
            self.initial_dimension_flow['flow'][i] = temp['flow'][i * load_period]

    def check_outliers_for_initial_data(self):
        if self.numberExamples ==0:
            print("Initial data doesn't upload.")
            return

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
        self.initial_dimensionless_flow['time'] =  self.initial_dimensionless_flow['time'] * 2.0 -1.0

    # def execute_initial_correlation_aproximate(self):
    #     period = self.experiment["period"]
    #     self.initial_correlation = pd.DataFrame()
    #     self.initial_correlation['time'] = [0.0] * round(self.numberExamples/period/2.0)
    #     self.initial_correlation['correlation'] = [0.0] * round(self.numberExamples/period/2.0)
    #
    #     size = len(self.initial_dimensionless_flow['time'])
    #     tau_max = self.initial_dimensionless_flow['time'].max()
    #     tau_min = self.initial_dimensionless_flow['time'].min()
    #     delta_tau = (tau_max - tau_min) / size
    #
    #     initial_dimensionless_flow_mean = self.initial_dimensionless_flow["flow"].mean()
    #     initial_dimensionless_flow_std = self.initial_dimensionless_flow["flow"].std()
    #
    #     count_1 = len(self.initial_correlation['time'])
    #
    #     for n_v in range(count_1):
    #         value = 0.0
    #         tau = n_v * period * delta_tau # self.initial_dimensionless_flow['time'][n_v * period]
    #         count_2 = round(self.numberExamples )
    #         for n_tau in range(round(count_2/2)):
    #             g1 = self.initial_dimensionless_flow['flow'][n_tau] - initial_dimensionless_flow_mean
    #             g2 = self.initial_dimensionless_flow['flow'][n_tau + n_v *period] - initial_dimensionless_flow_mean
    #             value = value + g1 * g2 * delta_tau
    #         self.initial_correlation['time'][n_v] = tau
    #         self.initial_correlation['correlation'][n_v] = value / 2.0 * self.numberExamples / count_2 / initial_dimensionless_flow_std / initial_dimensionless_flow_std
    #
    #         progress(n_v, count_1, 'execute_initial_correlation_aproximate')
    #     progress(count_1, count_1, 'execute_initial_correlation_aproximate')

    def execute_initial_correlation_aproximate(self):
        self.initial_correlation = self.execute_initial_correlation_aproximate2(self.initial_dimensionless_flow)

    def execute_genetator_correlation(self):
        self.genetator_correlation = self.execute_initial_correlation_aproximate2(self.generator_dimensionless_flow)





    # def execute_initial_correlation_aproximate(self):
    #     period = self.experiment["period"]
    #     self.initial_correlation = pd.DataFrame()
    #     self.initial_correlation['time'] = [0.0] * round(self.numberExamples/period/2.0)
    #     self.initial_correlation['correlation'] = [0.0] * round(self.numberExamples/period/2.0)
    #
    #     size = len(self.initial_dimensionless_flow['time'])
    #     tau_max = self.initial_dimensionless_flow['time'].max()
    #     tau_min = self.initial_dimensionless_flow['time'].min()
    #     delta_tau = (tau_max - tau_min) / size
    #
    #     initial_dimensionless_flow_mean = self.initial_dimensionless_flow["flow"].mean()
    #     initial_dimensionless_flow_std = self.initial_dimensionless_flow["flow"].std()
    #
    #     count_1 = len(self.initial_correlation['time'])
    #
    #     for n_v in range(count_1):
    #         value = 0.0
    #         tau = n_v * period * delta_tau # self.initial_dimensionless_flow['time'][n_v * period]
    #         count_2 = round(self.numberExamples - n_v * period)
    #         for n_tau in range(count_2):
    #             g1 = self.initial_dimensionless_flow['flow'][n_tau] - initial_dimensionless_flow_mean
    #             g2 = self.initial_dimensionless_flow['flow'][n_tau + n_v *period] - initial_dimensionless_flow_mean
    #             value = value + g1 * g2 * delta_tau
    #         self.initial_correlation['time'][n_v] = tau
    #         self.initial_correlation['correlation'][n_v] = value / 2.0 * self.numberExamples / count_2 / initial_dimensionless_flow_std / initial_dimensionless_flow_std
    #
    #         progress(n_v, count_1, 'execute_initial_correlation_aproximate')
    #     progress(count_1, count_1, 'execute_initial_correlation_aproximate')

    def execute_initial_correlation_aproximate2(self, initial_dimensionless_flow):
        period = self.experiment["period"]
        initial_correlation = pd.DataFrame()
        initial_correlation['time'] = [0.0] * round(self.numberExamples/period/2.0)
        initial_correlation['correlation'] = [0.0] * round(self.numberExamples/period/2.0)

        size = len(initial_dimensionless_flow['time'])
        tau_max = initial_dimensionless_flow['time'].max()
        tau_min = initial_dimensionless_flow['time'].min()
        delta_tau = (tau_max - tau_min) / size

        initial_dimensionless_flow_mean = initial_dimensionless_flow["flow"].mean()
        initial_dimensionless_flow_std = initial_dimensionless_flow["flow"].std()

        count_1 = len(initial_correlation['time'])

        for n_v in range(count_1):
            value = 0.0
            tau = n_v * period * delta_tau # self.initial_dimensionless_flow['time'][n_v * period]
            count_2 = round(self.numberExamples - n_v * period)
            for n_tau in range(count_2):
                g1 = initial_dimensionless_flow['flow'][n_tau] - initial_dimensionless_flow_mean
                g2 = initial_dimensionless_flow['flow'][n_tau + n_v *period] - initial_dimensionless_flow_mean
                value = value + g1 * g2 * delta_tau
            initial_correlation['time'][n_v] = tau
            initial_correlation['correlation'][n_v] = value / 2.0 * self.numberExamples / count_2 / initial_dimensionless_flow_std / initial_dimensionless_flow_std

            progress(n_v, count_1, 'execute_initial_correlation_aproximate2')
        progress(count_1, count_1, 'execute_initial_correlation_aproximate2\n')
        return initial_correlation



    def get_numeric_fourier_coefficients_by_correlation_function(self):
        number_of_harmonics = self.experiment["number_of_harmonics"]
        self.coefficients = cf.CorrelationFunctions.numeric_case_fourier_series(self.initial_correlation, number_of_harmonics)
        for i in range(len(self.coefficients)):
            if self.coefficients[i] < 0.0:
               self.coefficients[i] = 0.0

        print()

    def get_correlation_function_by_fourier_coefficients(self):
        self.correlation_by_fourier_coefficients = cf.CorrelationFunctions.get_function_value_by_coefficients(self.initial_correlation['time'].size, self.coefficients, tau_first = 0.0, tau_end = 1.0)
        return self.correlation_by_fourier_coefficients

    def execute_generator_dimensionless_flow(self):
    # https://docs.python.org/3/library/random.html
        self.generator_dimensionless_flow = pd.DataFrame()
        self.generator_dimensionless_flow['time'] = [0.0] * self.numberExamples
        self.generator_dimensionless_flow['flow'] = [0.0] * self.numberExamples

        mean = self.initial_dimensionless_flow['flow'].mean()
        std = self.initial_dimensionless_flow['flow'].std()
        coef_size = len(self.coefficients)

        flow_random_A = [random] * coef_size
        flow_random_B = [random] * coef_size

        for num in range(coef_size):
            num_random = random
            coef = 1.0
            if num==0:
                coef = 0.5
            _sigma = (std * math.sqrt(coef * self.coefficients[num]))
            flow_random_A[num] = random
            flow_random_A[num].seed(num + coef_size)   #  (num_random.randint)
            flow_random_A[num].gauss(mu=0.0, sigma=_sigma)
            flow_random_B[num] = random
            flow_random_B[num].seed(num + coef_size)   #  (num_random.randint)
            flow_random_B[num].gauss(mu=0.0, sigma=_sigma)

        for tau_num in range(self.numberExamples):
            tau = self.initial_dimensionless_flow['time'][tau_num]
            self.generator_dimensionless_flow['time'][tau_num] = tau
            value = mean
            for num in range(coef_size):
                coef = 1.0
                if num==0:
                    coef = 0.5
                _sigma = std * math.sqrt(coef * self.coefficients[num])
                value = value + flow_random_A[num].gauss(mu=0.0, sigma=_sigma) * math.cos(math.pi * num * tau) + flow_random_B[num].gauss(mu=0.0, sigma=_sigma) * math.sin(math.pi * num * tau)
            self.generator_dimensionless_flow['flow'][tau_num] = value
            progress(tau_num, self.numberExamples, 'execute_generator_flow')
        progress(self.numberExamples, self.numberExamples, 'execute_generator_flow\n')










    def gamma1_multiply_gamma2(self):
        print ("gamma1_multiply_gamma2 ")
        period = self.experiment["period"]
        self.number_correlation_examples = self.numberExamples
        self.gamma1_gamma2 = pd.DataFrame()
        self.gamma1_gamma2['time'] = [0.0] * round(self.number_correlation_examples/period /2.0)
        self.gamma1_gamma2['gg1'] = [0.0] * round(self.number_correlation_examples/period  /2.0)

        size = len(self.initial_dimensionless_flow['time'])
        tau_max = self.initial_dimensionless_flow['time'].max()
        tau_min = self.initial_dimensionless_flow['time'].min()
        delta_tau = (tau_max - tau_min) / size

        count_1 = len(self.gamma1_gamma2['time'])

        for n_v in range(count_1):
            value = 0.0
            tau = n_v * period * delta_tau # self.initial_dimensionless_flow['time'][n_v * period]
            count_2 = round(self.numberExamples - n_v * period)
            for n_tau in range(count_2):
                g1 = self.initial_dimensionless_flow['flow'][n_tau]
                g2 = self.initial_dimensionless_flow['flow'][n_tau + n_v *period]
                value = value + g1 * g2 * delta_tau
            self.gamma1_gamma2['time'][n_v] = tau
            self.gamma1_gamma2['gg1'][n_v] = value / 2.0 * self.number_correlation_examples / count_2
            progress(n_v, count_1)
        progress(count_1, count_1)

    def execute_initial_correlation_ideal(self):
        print ("\nexecute_initial_correlation_ideal ")
        period = self.experiment["period"]
        self.initial_correlation = pd.DataFrame()
        self.initial_correlation['time'] = [0.0] * round(self.numberExamples/period/2.0)
        self.initial_correlation['correlation'] = [0.0] * round(self.numberExamples/period/2.0)

        size = len(self.initial_dimensionless_flow['time'])
        tau_max = self.initial_dimensionless_flow['time'].max()
        tau_min = self.initial_dimensionless_flow['time'].min()
        delta_tau = (tau_max - tau_min) / size

        initial_dimensionless_flow_mean = self.initial_dimensionless_flow["flow"].mean()
        initial_dimensionless_flow_std = self.initial_dimensionless_flow["flow"].std()

        count_1 = len(self.initial_correlation['time'])

        for n_v in range(count_1):
            value = 0.0
            tau = n_v * period * delta_tau # self.initial_dimensionless_flow['time'][n_v * period]
            count_2 = round(self.numberExamples - n_v * period)
            for n_tau in range(count_2):
                g1 = self.initial_dimensionless_flow['flow'][n_tau]
                g2 = self.initial_dimensionless_flow['flow'][n_tau + n_v *period]
                value = value + g1 * g2 * delta_tau
            self.initial_correlation['time'][n_v] = tau
            self.initial_correlation['correlation'][n_v] = ( (value ) / 2.0 * self.numberExamples / count_2 -1.0) / initial_dimensionless_flow_std / initial_dimensionless_flow_std

            progress(n_v, count_1)
        progress(count_1, count_1)

    def execute_optimal_correlation_aproximate(self):
        print ("\nexecute_optimal_correlation_aproximate ")
        period = self.experiment["period"]
        self.optimal_correlation_aproximate = pd.DataFrame()
        self.optimal_correlation_aproximate['time'] = [0.0] * round(self.numberExamples/period/2.0)
        self.optimal_correlation_aproximate['correlation'] = [0.0] * round(self.numberExamples/period/2.0)

        size = len(self.gamma_optimum_s['time'])
        tau_max = self.gamma_optimum_s['time'].max()
        tau_min = self.gamma_optimum_s['time'].min()
        delta_tau = (tau_max - tau_min) / size

        gamma_optimum_s_mean = self.gamma_optimum_s["flow"].mean()
        gamma_optimum_s_std = self.gamma_optimum_s["flow"].std()

        count_1 = len(self.initial_correlation['time'])

        for n_v in range(count_1):
            value = 0.0
            tau = n_v * period * delta_tau # self.initial_dimensionless_flow['time'][n_v * period]
            count_2 = round(self.numberExamples - n_v * period)
            for n_tau in range(count_2):
                g1 = self.gamma_optimum_s['flow'][n_tau]
                g2 = self.gamma_optimum_s['flow'][n_tau + n_v *period]
                value = value + g1 * g2 * delta_tau
            self.optimal_correlation_aproximate['time'][n_v] = tau
            self.optimal_correlation_aproximate['correlation'][n_v] = ( (value ) / 2.0 * self.numberExamples / count_2 ) / gamma_optimum_s_std**2

            progress(n_v, count_1)
        progress(count_1, count_1)

    def execute_optimal_correlation_ideal(self):
        print ("\nexecute_optimal_correlation_ideal ")

        size = len(self.gamma1_gamma2['time'])
        self.optimal_correlation_ideal = pd.DataFrame()
        self.optimal_correlation_ideal['time'] = [0.0] * size
        self.optimal_correlation_ideal['correlation'] = [0.0] * size

        self.fourier_coefficient_for_gamma_d[0] = math.sqrt(2.0*self.fourier_series_for_gg1[0])
        gd1_gd2 = cf.CorrelationFunctions.get_correlation_function_value_by_coefficients(size, self.fourier_coefficient_for_gamma_d, self.gamma1_gamma2['time'].min(), self.gamma1_gamma2['time'].max())
        g1_g2 = cf.CorrelationFunctions.get_function_value_by_coefficients(size, self.fourier_series_for_gg1, self.gamma1_gamma2['time'].min(), self.gamma1_gamma2['time'].max())
        self.gamma_d = cf.CorrelationFunctions.get_function_value_by_coefficients(size, self.fourier_series_for_gg1, self.gamma1_gamma2['time'].min(), self.gamma1_gamma2['time'].max())
        gamma_optimum_s_std2 = self.gamma_optimum_s['flow'].std()**2
        standard_deviation_optimum2 = self.standard_deviation_optimum**2
        for n in range(size):   #self.gamma1_gamma2['gg1']
            self.optimal_correlation_ideal['time'][n] = self.gamma1_gamma2['time'][n]
#            self.optimal_correlation_ideal['correlation'][n] = (self.gamma1_gamma2['gg1'][n] - gd1_gd2['correlation'][n]) / self.standard_deviation_optimum**2
#           self.optimal_correlation_ideal['correlation'][n] = (g1_g2['flow'][n] - gd1_gd2['correlation'][n]) / standard_deviation_optimum2
            self.optimal_correlation_ideal['correlation'][n] = (self.gamma1_gamma2['gg1'][n] - gd1_gd2['correlation'][n]) / standard_deviation_optimum2
            progress(n, size)
        progress(size, size)

    def test_execute_fourier_series_aproximate_theory_cor_function_exp(self, number_of_harmonics):
        print ("\nexecute_fourier_series_aproximate_theory_cor_function_exp ")

        size = len(self.initial_correlation['time'])
        self.theory_cor_function_exp = pd.DataFrame()
        self.theory_cor_function_exp['time'] = [0.0] * size
        self.theory_cor_function_exp['correlation'] = [0.0] * size

        correlation_tau = self.experiment["correlation_tau"]
        for n in range(size):
            tau =  self.initial_correlation['time'][n]
            self.theory_cor_function_exp['time'][n] = tau
            self.theory_cor_function_exp['correlation'][n] = cf.CorrelationFunctions.exp(tau, correlation_tau)

        # number_of_harmonics = self.experiment["number_of_harmonics"]
        test_number = 4
        #===============================================================================================================
        self.theory_cor_function_exp_fourier_series = [0.0] * number_of_harmonics
        self.fourier_series_theory_cor_function_exp_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            fourier_series_theory_cor_function_exp = pd.DataFrame()
            fourier_series_theory_cor_function_exp['time'] = [0.0] * size
            fourier_series_theory_cor_function_exp['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                fourier_series_theory_cor_function_exp['time'][n] = tau
                fourier_series_theory_cor_function_exp['correlation'][n] \
                    = cf.CorrelationFunctions.fourier_series_exp(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.fourier_series_theory_cor_function_exp_s[k] = fourier_series_theory_cor_function_exp
        #===============================================================================================================
        self.continuous_spectrum_theory_cor_function_exp_fourier_series = [0.0] * number_of_harmonics
        self.continuous_spectrum_fourier_series_theory_cor_function_exp_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            continuous_spectrum_fourier_series_theory_cor_function_exp = pd.DataFrame()
            continuous_spectrum_fourier_series_theory_cor_function_exp['time'] = [0.0] * size
            continuous_spectrum_fourier_series_theory_cor_function_exp['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                continuous_spectrum_fourier_series_theory_cor_function_exp['time'][n] = tau
                continuous_spectrum_fourier_series_theory_cor_function_exp['correlation'][n] \
                    = cf.CorrelationFunctions.continuous_spectrum_fourier_series_exp(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[k] = continuous_spectrum_fourier_series_theory_cor_function_exp

        #===============================================================================================================
        self.numeric_case_fourier_series_theory_cor_function_exp_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            numeric_case_fourier_series_theory_cor_function_exp = pd.DataFrame()
            numeric_case_fourier_series_theory_cor_function_exp['time'] = [0.0] * size
            numeric_case_fourier_series_theory_cor_function_exp['correlation'] = [0.0] * size

            self.numeric_case_correlation_function_fourier_series \
                = cf.CorrelationFunctions.numeric_case_fourier_series(self.theory_cor_function_exp, (k+1)*number_of_harmonics)
            for n in range(size):
                tau =  self.theory_cor_function_exp['time'][n]
                numeric_case_fourier_series_theory_cor_function_exp['time'][n] = tau
                value = 0.0
                for num in range( len(self.numeric_case_correlation_function_fourier_series)):
                    coef = 1.0
                    if (num==0):
                        coef = 0.5
                    value = value + coef * self.numeric_case_correlation_function_fourier_series[num] * math.cos(math.pi * num * tau)
                numeric_case_fourier_series_theory_cor_function_exp['correlation'][n] = value
            self.numeric_case_fourier_series_theory_cor_function_exp_s[k] = numeric_case_fourier_series_theory_cor_function_exp

    def test_execute_fourier_series_aproximate_theory_cor_function_exp_1_plus_tau(self, number_of_harmonics):
        print ("\ntest_execute_fourier_series_aproximate_theory_cor_function_exp_1_plus_tau ")

        size = len(self.initial_correlation['time'])
        self.theory_cor_function_exp_1_plus_tau = pd.DataFrame()
        self.theory_cor_function_exp_1_plus_tau['time'] = [0.0] * size
        self.theory_cor_function_exp_1_plus_tau['correlation'] = [0.0] * size

        correlation_tau = self.experiment["correlation_tau"]
        for n in range(size):
            tau =  self.initial_correlation['time'][n]
            self.theory_cor_function_exp_1_plus_tau['time'][n] = tau
            self.theory_cor_function_exp_1_plus_tau['correlation'][n] = cf.CorrelationFunctions.exp_1_plus_tau(tau, correlation_tau)

        # number_of_harmonics = self.experiment["number_of_harmonics"]
        test_number = 4
        #===============================================================================================================
        self.theory_cor_function_exp_1_plus_tau_fourier_series = [0.0] * number_of_harmonics
        self.fourier_series_theory_cor_function_exp_1_plus_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            fourier_series_theory_cor_function_exp_1_plus_tau = pd.DataFrame()
            fourier_series_theory_cor_function_exp_1_plus_tau['time'] = [0.0] * size
            fourier_series_theory_cor_function_exp_1_plus_tau['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                fourier_series_theory_cor_function_exp_1_plus_tau['time'][n] = tau
                fourier_series_theory_cor_function_exp_1_plus_tau['correlation'][n] \
                    = cf.CorrelationFunctions.fourier_series_exp_1_plus_tau(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.fourier_series_theory_cor_function_exp_1_plus_tau_s[k] = fourier_series_theory_cor_function_exp_1_plus_tau
        #===============================================================================================================
        self.continuous_spectrum_theory_cor_function_exp_1_plus_tau_fourier_series = [0.0] * number_of_harmonics
        self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau = pd.DataFrame()
            continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau['time'] = [0.0] * size
            continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau['time'][n] = tau
                continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau['correlation'][n] \
                    = cf.CorrelationFunctions.continuous_spectrum_fourier_series_exp_1_plus_tau(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s[k] = continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau

        #===============================================================================================================
        self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau = pd.DataFrame()
            numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau['time'] = [0.0] * size
            numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau['correlation'] = [0.0] * size

            self.numeric_case_correlation_function_fourier_series_1_plus_tau \
                = cf.CorrelationFunctions.numeric_case_fourier_series(self.theory_cor_function_exp_1_plus_tau, (k+1)*number_of_harmonics)
            for n in range(size):
                tau =  self.theory_cor_function_exp_1_plus_tau['time'][n]
                numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau['time'][n] = tau
                value = 0.0
                for num in range( len(self.numeric_case_correlation_function_fourier_series_1_plus_tau)):
                    coef = 1.0
                    if (num==0):
                        coef = 0.5
                    value = value + coef * self.numeric_case_correlation_function_fourier_series_1_plus_tau[num] * math.cos(math.pi * num * tau)
                numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau['correlation'][n] = value
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[k] = numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau

    def test_execute_fourier_series_aproximate_theory_cor_function_exp_1_minus_tau(self, number_of_harmonics):
        print ("\ntest_execute_fourier_series_aproximate_theory_cor_function_exp_1_minus_tau ")

        size = len(self.initial_correlation['time'])
        self.theory_cor_function_exp_1_minus_tau = pd.DataFrame()
        self.theory_cor_function_exp_1_minus_tau['time'] = [0.0] * size
        self.theory_cor_function_exp_1_minus_tau['correlation'] = [0.0] * size

        correlation_tau = self.experiment["correlation_tau"]
        for n in range(size):
            tau =  self.initial_correlation['time'][n]
            self.theory_cor_function_exp_1_minus_tau['time'][n] = tau
            self.theory_cor_function_exp_1_minus_tau['correlation'][n] = cf.CorrelationFunctions.exp_1_minus_tau(tau, correlation_tau)

        test_number = 4
        #===============================================================================================================
        self.theory_cor_function_exp_1_minus_tau_fourier_series = [0.0] * number_of_harmonics
        self.fourier_series_theory_cor_function_exp_1_minus_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            fourier_series_theory_cor_function_exp_1_minus_tau = pd.DataFrame()
            fourier_series_theory_cor_function_exp_1_minus_tau['time'] = [0.0] * size
            fourier_series_theory_cor_function_exp_1_minus_tau['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                fourier_series_theory_cor_function_exp_1_minus_tau['time'][n] = tau
                fourier_series_theory_cor_function_exp_1_minus_tau['correlation'][n] \
                    = cf.CorrelationFunctions.fourier_series_exp_1_minus_tau(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.fourier_series_theory_cor_function_exp_1_minus_tau_s[k] = fourier_series_theory_cor_function_exp_1_minus_tau
        #===============================================================================================================
        self.continuous_spectrum_theory_cor_function_exp_1_minus_tau_fourier_series = [0.0] * number_of_harmonics
        self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau = pd.DataFrame()
            continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau['time'] = [0.0] * size
            continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau['time'][n] = tau
                continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau['correlation'][n] \
                    = cf.CorrelationFunctions.continuous_spectrum_fourier_series_exp_1_minus_tau(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s[k] = continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau
        #===============================================================================================================
        self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau = pd.DataFrame()
            numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau['time'] = [0.0] * size
            numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau['correlation'] = [0.0] * size

            self.numeric_case_correlation_function_fourier_series_1_minus_tau \
                = cf.CorrelationFunctions.numeric_case_fourier_series(self.theory_cor_function_exp_1_minus_tau, (k+1)*number_of_harmonics)
            for n in range(size):
                tau =  self.theory_cor_function_exp_1_minus_tau['time'][n]
                numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau['time'][n] = tau
                value = 0.0
                for num in range( len(self.numeric_case_correlation_function_fourier_series_1_minus_tau)):
                    coef = 1.0
                    if (num==0):
                        coef = 0.5
                    value = value + coef * self.numeric_case_correlation_function_fourier_series_1_minus_tau[num] * math.cos(math.pi * num * tau)
                numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau['correlation'][n] = value
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[k] = numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau

    def test_execute_fourier_series_aproximate_theory_cor_function_exp_cos_betta_tau(self, number_of_harmonics):
        print ("\ntest_execute_fourier_series_aproximate_theory_cor_function_exp_cos_betta_tau ")

        size = len(self.initial_correlation['time'])
        self.theory_cor_function_exp_cos_betta_tau = pd.DataFrame()
        self.theory_cor_function_exp_cos_betta_tau['time'] = [0.0] * size
        self.theory_cor_function_exp_cos_betta_tau['correlation'] = [0.0] * size

        correlation_tau = self.experiment["correlation_tau"]
        for n in range(size):
            tau =  self.initial_correlation['time'][n]
            self.theory_cor_function_exp_cos_betta_tau['time'][n] = tau
            self.theory_cor_function_exp_cos_betta_tau['correlation'][n] = cf.CorrelationFunctions.exp_cos_betta_tau(tau, correlation_tau)

        test_number = 4
        #===============================================================================================================

        #===============================================================================================================
        self.continuous_spectrum_theory_cor_function_exp_cos_betta_tau_fourier_series = [0.0] * number_of_harmonics
        self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau = pd.DataFrame()
            continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau['time'] = [0.0] * size
            continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau['correlation'] = [0.0] * size

            for n in range(size):
                tau =  self.initial_correlation['time'][n]
                continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau['time'][n] = tau
                continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau['correlation'][n] \
                    = cf.CorrelationFunctions.continuous_spectrum_fourier_series_exp_cos_betta_tau(tau, correlation_tau, (k+1)*number_of_harmonics)
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[k] = continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau
        #===============================================================================================================
        self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s = [pd.DataFrame()] * test_number
        for k in range(test_number):
            numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau = pd.DataFrame()
            numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau['time'] = [0.0] * size
            numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau['correlation'] = [0.0] * size

            self.numeric_case_correlation_function_fourier_series_cos_betta_tau \
                = cf.CorrelationFunctions.numeric_case_fourier_series(self.theory_cor_function_exp_cos_betta_tau, (k+1)*number_of_harmonics)
            for n in range(size):
                tau =  self.theory_cor_function_exp_cos_betta_tau['time'][n]
                numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau['time'][n] = tau
                value = 0.0
                for num in range( len(self.numeric_case_correlation_function_fourier_series_cos_betta_tau)):
                    coef = 1.0
                    if (num==0):
                        coef = 0.5
                    value = value + coef * self.numeric_case_correlation_function_fourier_series_cos_betta_tau[num] * math.cos(math.pi * num * tau)
                numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau['correlation'][n] = value
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[k] = numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau





    def typization_by_correlation_function(self):

        print ("\ntypization_by_correlation_function ")
        gg1 = pd.DataFrame()
        gg1['time'] = [0.0] * len(self.gamma1_gamma2['time'])
        gg1['correlation'] = [0.0] * len(self.gamma1_gamma2['time'])

        gg1['time'] =   self.gamma1_gamma2['time']
        gg1['correlation'] =   self.gamma1_gamma2['gg1']

        number_of_harmonics = self.experiment["number_of_harmonics"]

        squared_fourier_coefficient_for_gamma_d = [0.0] * number_of_harmonics

        number_of_checking = 10
        correlation_tau_max = 1.0
        standard_deviation_max = self.initial_dimensionless_flow['flow'].std()

        delta_correlation_tau = correlation_tau_max / (number_of_checking-1)
        delta_standard_deviation = standard_deviation_max / (number_of_checking-1)
        self.criterium = 100000000.0
        self.correlation_tau_optimum = 0.0
        self.standard_deviation_optimum = 0.0
        self.type_id_optimum =0

        self.fourier_series_for_gg1 = cf.CorrelationFunctions.numeric_case_fourier_series(gg1, number_of_harmonics)

        for type_id in range(4):
            #type_id = 1
            for n_cor in range(number_of_checking):
                correlation_tau = delta_correlation_tau * (n_cor +1)
                if (type_id == 0 or type_id == 1 or type_id == 2):
                    fourier_coefficients = cf.CorrelationFunctions.get_fourier_coefficients_by_function_id(type_id, number_of_harmonics, correlation_tau)
                if (type_id == 3):
                    fourier_coefficients = cf.CorrelationFunctions.get_numeric_fourier_coefficients_by_function_id(type_id, number_of_harmonics, correlation_tau)

                for n_std in range(number_of_checking):
                    standard_deviation = delta_standard_deviation * n_std
                    temp = 0.0
                    for n in range(number_of_harmonics):
                        if(n==0):
                            squared_fourier_coefficient_for_gamma_d[n] \
                                = (- standard_deviation **2 * fourier_coefficients[n] )
                            squared_fourier_coefficient_for_gamma_d[n] = 0.0
                        else:
                            squared_fourier_coefficient_for_gamma_d[n] \
                                = 2.0 * (self.fourier_series_for_gg1[n] - standard_deviation **2 * fourier_coefficients[n] )
                        if(squared_fourier_coefficient_for_gamma_d[n]<0):
                            # print("\n")
                            # print('\nstandard_deviation:', standard_deviation)
                            # print('\ncorrelation_tau:', correlation_tau)
                            # print(squared_fourier_coefficient_for_gamma_d[n])
                            squared_fourier_coefficient_for_gamma_d[n]=0.0
                        temp = temp + squared_fourier_coefficient_for_gamma_d[n]**2
                    if(temp<=self.criterium ):
                        self.criterium=temp
                        self.correlation_tau_optimum = correlation_tau
                        self.standard_deviation_optimum = standard_deviation
                        self.type_id_optimum = type_id
                progress(n_cor, number_of_checking)
            progress(number_of_checking, number_of_checking)

        self.fourier_coefficient_for_gamma_d = [0.0] * number_of_harmonics

        if (self.type_id_optimum == 0 or self.type_id_optimum == 1 or self.type_id_optimum == 2):
            fourier_coefficients = cf.CorrelationFunctions.get_fourier_coefficients_by_function_id(self.type_id_optimum, number_of_harmonics, self.correlation_tau_optimum)
        if (self.type_id_optimum == 3):
            fourier_coefficients = cf.CorrelationFunctions.get_numeric_fourier_coefficients_by_function_id(self.type_id_optimum, number_of_harmonics, self.correlation_tau_optimum)

        for n in range(number_of_harmonics):
            if(n==0):
                self.fourier_coefficient_for_gamma_d[n] = 2.0
            else:
                squared_fourier_coefficient = 2.0 * (self.fourier_series_for_gg1[n] - self.standard_deviation_optimum **2 * fourier_coefficients[n] )
                if(squared_fourier_coefficient < 0.0):
                    self.fourier_coefficient_for_gamma_d[n]=0.0
                else:
                    self.fourier_coefficient_for_gamma_d[n] = math.sqrt(squared_fourier_coefficient)

        print()

#=======================================================================================================================
    def calculate_gamma_optimum_s(self):
        print ("\ncalculate_gamma_optimum_s ")

        size = len(self.initial_dimensionless_flow['flow'])
        min_time = self.initial_dimensionless_flow['time'].min()
        max_time = self.initial_dimensionless_flow['time'].max()
        self.gamma_optimum_d = cf.CorrelationFunctions.get_function_value_by_coefficients(size, self.fourier_coefficient_for_gamma_d, min_time, max_time)

        self.gamma_optimum_s = pd.DataFrame()
        self.gamma_optimum_s['time'] = [0.0] * size
        self.gamma_optimum_s['flow'] = [0.0] * size

        for n_tau in range(size):
            self.gamma_optimum_s['time'][n_tau] = self.initial_dimensionless_flow['time'][n_tau]
            self.gamma_optimum_s['flow'][n_tau] = self.initial_dimensionless_flow['flow'][n_tau] - self.gamma_optimum_d['flow'][n_tau]







#=======================================================================================================================
    def initial_dimension_data_show(self):
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_result"]
        path = result_data + self.file_name + '/' + initial_data_result

        initial_dimension_flows = [self.initial_dimension_flow['time'].values, self.initial_dimension_flow['flow'].values]
        show.common_line(self.experiment, path, initial_dimension_flows, "flow_line_", "initial_flow_line")
        initial_dimension_flows_for_hist = [self.initial_dimension_flow['time'].values, self.initial_dimension_flow['flow'].values]
        show.common_hist(self.experiment, path, initial_dimension_flows_for_hist, "flow_hist_", "initial_flow_hist")

    def initial_dimensionless_data_show(self):
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_dimensionless_result"]
        path = result_data + self.file_name + '/' + initial_data_result

        initial_dimensionless_flows = [self.initial_dimensionless_flow['time'].values, self.initial_dimensionless_flow['flow'].values]
        show.common_line(self.experiment, path, initial_dimensionless_flows, "flow_line_", "initial_dimensionless_flow_line")
        initial_dimensionless_flows_for_hist = [self.initial_dimensionless_flow['time'].values, self.initial_dimensionless_flow['flow'].values]
        show.common_hist(self.experiment, path, initial_dimensionless_flows_for_hist, "flow_hist_", "initial_dimensionless_flow_hist")

    def initial_correlation_aproximate_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        initial_correlation = [self.initial_correlation['time'].values, self.initial_correlation['correlation'].values]
        show.common_line(self.experiment, path, initial_correlation, "initial_aproximat_correlation_", "initial_correlation_line")

    def correlation_by_fourier_coefficients_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        correlation_by_fourier_s = [self.correlation_by_fourier_coefficients['time'].values, self.correlation_by_fourier_coefficients['flow'].values, self.initial_correlation['correlation'].values]
        show.common_line(self.experiment, path, correlation_by_fourier_s, "correlation_by_fourier_s_", "initial_correlation_line")

    def generator_dimensionless_data_show(self):
        result_data = self.result_data_structure["result_data"] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure["initial_data_dimensionless_result"]
        path = result_data + self.file_name + '/' + initial_data_result

        generator_dimensionless_flows = [self.generator_dimensionless_flow['time'].values, self.generator_dimensionless_flow['flow'].values, self.initial_dimensionless_flow['flow'].values]
        show.common_line(self.experiment, path, generator_dimensionless_flows, "generator_flow_line_", "initial_dimensionless_flow_line")
        generator_dimensionless_flows_for_hist = [self.generator_dimensionless_flow['time'].values, self.generator_dimensionless_flow['flow'].values]
        show.common_hist(self.experiment, path, generator_dimensionless_flows_for_hist, "generator_flow_hist_", "initial_dimensionless_flow_hist")

    def genetator_correlation_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        genetator_correlation_s = [self.genetator_correlation['time'].values, self.genetator_correlation['correlation'].values, self.initial_correlation['correlation'].values]
        show.common_line(self.experiment, path, genetator_correlation_s, "genetator_correlation_", "initial_correlation_line")
        sum = 0.0
        for i in range(len(self.coefficients)):
            if i==0:
                sum = sum + self.coefficients[i]/2.0
            else:
                sum = sum + self.coefficients[i]
        print('sum',sum)
        print(self.generator_dimensionless_flow['flow'].std())
        print(self.initial_dimensionless_flow['flow'].std())

    def gamma_optimum_spectrum_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["gamma_optimal_s"]
        path = result_data + self.file_name + '/' + initial_data_result

        size = len(self.coefficients)
        fourier_coefficient = [0] * size
        for n in range(size):
            if(n==0):
                fourier_coefficient[n] = self.coefficients[n]/2
            else:
                fourier_coefficient[n] = self.coefficients[n]

        fourier_coefficient_s = [range(size), fourier_coefficient]
        show.common_bar(self.experiment, path, fourier_coefficient_s, "gamma_optimum_spectrum_s_bar_", "gamma_optimum_s_bar")































    def gamma_optimum_s_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["gamma_optimal_s"]
        path = result_data + self.file_name + '/' + initial_data_result

        gamma_optimum_s_s = [self.gamma_optimum_s['time'].values, self.gamma_optimum_s['flow'].values]
        show.common_line(self.experiment, path, gamma_optimum_s_s, "gamma_optimum_s_line_", "gamma_optimum_s_line")
        gamma_optimum_s_s_for_hist = [self.gamma_optimum_s['time'].values, self.gamma_optimum_s['flow'].values]
        show.common_hist(self.experiment, path, gamma_optimum_s_s_for_hist, "gamma_optimum_s_hist_", "gamma_optimum_s_hist")

    def gamma_optimum_d_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["gamma_optimal_s"]
        path = result_data + self.file_name + '/' + initial_data_result

        gamma_optimum_d_s = [self.gamma_optimum_d['time'].values, self.gamma_optimum_d['flow'].values]
        show.common_line(self.experiment, path, gamma_optimum_d_s, "gamma_optimum_d_line_", "gamma_optimum_d_line")

    def g_g2_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        gamma1_gamma2s = [self.gamma1_gamma2['time'].values, self.gamma1_gamma2['gg1'].values]
        show.common_line(self.experiment, path, gamma1_gamma2s, "gamma1_gamma2_", "g_g2_line")

    def initial_correlation_ideal_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        initial_correlation = [self.initial_correlation['time'].values, self.initial_correlation['correlation'].values]
        show.common_line(self.experiment, path, initial_correlation, "initial_correlation_", "initial_correlation_line")

    def optimal_correlation_aproximate_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        optimal_correlation_aproximate_s = [self.optimal_correlation_aproximate['time'].values, self.optimal_correlation_aproximate['correlation'].values]
        show.common_line(self.experiment, path, optimal_correlation_aproximate_s, "optimal_correlation_aproximate_", "initial_correlation_line")

    def optimal_correlation_ideal_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["g_g2_result"]
        path = result_data + self.file_name + '/' + initial_data_result
        optimal_correlation_ideal_s = [self.optimal_correlation_ideal['time'].values, self.optimal_correlation_ideal['correlation'].values]
        show.common_line(self.experiment, path, optimal_correlation_ideal_s, "optimal_correlation_ideal_", "initial_correlation_line")

    def test_theory_cor_function_exp_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["test_theory_cor_function_exp"]
        path = result_data + self.file_name + '/' + initial_data_result
        theory_cor_function_exp = [self.theory_cor_function_exp['time'].values, self.theory_cor_function_exp['correlation'].values]
        show.common_line(self.experiment, path, theory_cor_function_exp, "theory_cor_func_", "test_theory_cor_function_exp_line")

        fourier_series_theory_cor_function_exp_s = [
            self.fourier_series_theory_cor_function_exp_s[0]['time'].values,
            self.theory_cor_function_exp['correlation'].values,
            self.fourier_series_theory_cor_function_exp_s[0]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_s[1]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_s[2]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, fourier_series_theory_cor_function_exp_s, "fourier_series_theory_cor_func_", "test_theory_cor_function_exp_line")

        continuous_spectrum_fourier_series_theory_cor_function_exp_s = [
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[0]['time'].values,
            self.theory_cor_function_exp['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[0]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[1]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[2]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, continuous_spectrum_fourier_series_theory_cor_function_exp_s, "continuous_spectrum_fourier_series_theory_cor_func_", "test_theory_cor_function_exp_line")


        numeric_case_fourier_series_theory_cor_function_exp_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_s[0]['time'].values,
            self.theory_cor_function_exp['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, numeric_case_fourier_series_theory_cor_function_exp_s, "fourier_series_numeric_cor_func_", "test_theory_cor_function_exp_line")

        delta_numeric_case_fourier_series_theory_cor_function_exp_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_s[0]['time'].values,
            self.theory_cor_function_exp['correlation'].values + 1,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[0]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[1]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[2]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_s[3]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, delta_numeric_case_fourier_series_theory_cor_function_exp_s, "fourier_series_delta_numeric_cor_func_", "test_theory_delta_cor_function_exp_line")
#=========================================================
        delta_continuous_theoretical_case_fourier_series_theory_cor_function_exp_s = [
            self.theory_cor_function_exp['time'].values,
            self.theory_cor_function_exp['correlation'].values + 1,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[0]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[0]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[1]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[1]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[2]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[2]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_s[3]['correlation'].values - self.fourier_series_theory_cor_function_exp_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path,  delta_continuous_theoretical_case_fourier_series_theory_cor_function_exp_s, "fourier_series_delta_continuous_cor_func_", "test_theory_delta_cor_function_exp_line")


    def test_theory_cor_function_exp_1_plus_tau_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["test_theory_cor_function_exp_1_plus_tau"]
        path = result_data + self.file_name + '/' + initial_data_result
        theory_cor_function_exp_1_plus_tau = [self.theory_cor_function_exp_1_plus_tau['time'].values, self.theory_cor_function_exp_1_plus_tau['correlation'].values]
        show.common_line(self.experiment, path, theory_cor_function_exp_1_plus_tau, "theory_cor_func_1_plus_tau_", "test_theory_cor_function_exp_line")

        fourier_series_theory_cor_function_exp_1_plus_tau_s = [
            self.fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['time'].values,
            self.theory_cor_function_exp_1_plus_tau['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_plus_tau_s[1]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_plus_tau_s[2]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_plus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, fourier_series_theory_cor_function_exp_1_plus_tau_s, "fourier_series_theory_cor_func_1_plus_tau_", "test_theory_cor_function_exp_line")

        continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s = [
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['time'].values,
            self.theory_cor_function_exp_1_plus_tau['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s[1]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s[2]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, continuous_spectrum_fourier_series_theory_cor_function_exp_1_plus_tau_s, "continuous_spectrum_fourier_series_theory_cor_func_1_plus_tau_", "test_theory_cor_function_exp_line")


        numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['time'].values,
            self.theory_cor_function_exp_1_plus_tau['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s, "fourier_series_numeric_cor_func_1_plus_tau_", "test_theory_cor_function_exp_line")

        delta_numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['time'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_plus_tau_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[1]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_plus_tau_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[2]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_plus_tau_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s[3]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_plus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, delta_numeric_case_fourier_series_theory_cor_function_exp_1_plus_tau_s, "fourier_series_delta_numeric_cor_func_1_plus_tau_", "test_theory_delta_cor_function_exp_line")

    def test_theory_cor_function_exp_1_minus_tau_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["test_theory_cor_function_exp_1_minus_tau"]
        path = result_data + self.file_name + '/' + initial_data_result
        theory_cor_function_exp_1_minus_tau = [self.theory_cor_function_exp_1_minus_tau['time'].values, self.theory_cor_function_exp_1_minus_tau['correlation'].values]
        show.common_line(self.experiment, path, theory_cor_function_exp_1_minus_tau, "theory_cor_func_1_minus_tau_", "test_theory_cor_function_exp_line")

        fourier_series_theory_cor_function_exp_1_minus_tau_s = [
            self.fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['time'].values,
            self.theory_cor_function_exp_1_minus_tau['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_minus_tau_s[1]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_minus_tau_s[2]['correlation'].values,
            self.fourier_series_theory_cor_function_exp_1_minus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, fourier_series_theory_cor_function_exp_1_minus_tau_s, "fourier_series_theory_cor_func_1_minus_tau_", "test_theory_cor_function_exp_line")

        continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s = [
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['time'].values,
            self.theory_cor_function_exp_1_minus_tau['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s[1]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s[2]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, continuous_spectrum_fourier_series_theory_cor_function_exp_1_minus_tau_s, "continuous_spectrum_fourier_series_theory_cor_func_1_minus_tau_", "test_theory_cor_function_exp_line")

        numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['time'].values,
            self.theory_cor_function_exp_1_minus_tau['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s, "fourier_series_numeric_cor_func_1_minus_tau_", "test_theory_cor_function_exp_line")

        delta_numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['time'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[1]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_minus_tau_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[2]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_minus_tau_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s[3]['correlation'].values - self.fourier_series_theory_cor_function_exp_1_minus_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, delta_numeric_case_fourier_series_theory_cor_function_exp_1_minus_tau_s, "fourier_series_delta_numeric_cor_func_1_minus_tau_", "test_theory_delta_cor_function_exp_line")

    def test_theory_cor_function_exp_cos_betta_tau_show(self):
        result_data = self.result_data_structure["result_data"] + '/'
        initial_data_result = self.result_data_structure["test_theory_cor_function_exp_cos_betta_tau"]
        path = result_data + self.file_name + '/' + initial_data_result
        theory_cor_function_exp_cos_betta_tau = [self.theory_cor_function_exp_cos_betta_tau['time'].values, self.theory_cor_function_exp_cos_betta_tau['correlation'].values]
        show.common_line(self.experiment, path, theory_cor_function_exp_cos_betta_tau, "theory_cor_func_cos_betta_tau_", "test_theory_cor_function_exp_line")

        # fourier_series_theory_cor_function_exp_1_minus_tau_s = [
        #     self.fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['time'].values,
        #     self.theory_cor_function_exp_1_minus_tau['correlation'].values,
        #     self.fourier_series_theory_cor_function_exp_1_minus_tau_s[0]['correlation'].values,
        #     self.fourier_series_theory_cor_function_exp_1_minus_tau_s[1]['correlation'].values,
        #     self.fourier_series_theory_cor_function_exp_1_minus_tau_s[2]['correlation'].values,
        #     self.fourier_series_theory_cor_function_exp_1_minus_tau_s[3]['correlation'].values
        # ]
        # show.common_line(self.experiment, path, fourier_series_theory_cor_function_exp_1_minus_tau_s, "fourier_series_theory_cor_func_1_minus_tau_", "test_theory_cor_function_exp_line")

        continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s = [
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['time'].values,
            self.theory_cor_function_exp_cos_betta_tau['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[1]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[2]['correlation'].values,
            self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s, "continuous_spectrum_fourier_series_theory_cor_func_cos_betta_tau_", "test_theory_cor_function_exp_line")

        numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['time'].values,
            self.theory_cor_function_exp_cos_betta_tau['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s, "fourier_series_numeric_cor_func_cos_betta_tau_", "test_theory_cor_function_exp_line")

        delta_numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s = [
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['time'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['correlation'].values - self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[0]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[1]['correlation'].values - self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[1]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[2]['correlation'].values - self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[2]['correlation'].values,
            self.numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s[3]['correlation'].values - self.continuous_spectrum_fourier_series_theory_cor_function_exp_cos_betta_tau_s[3]['correlation'].values
        ]
        show.common_line(self.experiment, path, delta_numeric_case_fourier_series_theory_cor_function_exp_cos_betta_tau_s, "fourier_series_delta_numeric_cor_func_exp_cos_betta_tau_", "test_theory_delta_cor_function_exp_line")
    #=======================================================================================================================
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
        file.write("Number of harmonics:      %10d " % (self.experiment["number_of_harmonics"]))
        file.write("\n\n")
        file.write("Period             :      %10d " % (self.experiment["period"]))
        file.write("\n\n")
        file.write("Load_period        :      %10d " % (self.experiment["load_period"]))
        file.write("\n\n")

        file.write("Dimension parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.7f" % (self.initial_dimension_flow['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.7f" % (self.initial_dimension_flow['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.7f" % (self.initial_dimension_flow['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.7f" % (self.initial_dimension_flow['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.7f" % (self.initial_dimension_flow['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.7f" % (self.initial_dimension_flow['flow'].std()))
        file.write("\n\n")

        file.write("Dimensionless parameters:               ")
        file.write("\n")
        file.write("tMin       : %10.7f" % (self.initial_dimensionless_flow['time'].min()))
        file.write("\n")
        file.write("tMax       : %10.7f" % (self.initial_dimensionless_flow['time'].max()))
        file.write("\n")
        file.write("flowMin    : %10.7f" % (self.initial_dimensionless_flow['flow'].min()))
        file.write("\n")
        file.write("flowMax    : %10.7f" % (self.initial_dimensionless_flow['flow'].max()))
        file.write("\n")
        file.write("flowMean   : %10.7f" % (self.initial_dimensionless_flow['flow'].mean()))
        file.write("\n")
        file.write("flowStd    : %10.7f" % (self.initial_dimensionless_flow['flow'].std()))
        file.write("\n\n")

        file.write("Optimal parameters:               ")
        file.write("Fourier coefficients               :")
        file.write("\n")
        for n in range(len(self.coefficients)):
            file.write("  n: %2d  " % n)
            file.write("%10.5f" % self.coefficients[n])
        file.write("\n")

        file.close()