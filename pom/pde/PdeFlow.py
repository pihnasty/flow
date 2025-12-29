from datetime import datetime

from constants.flow_constants import FLOW
from io_utils.csv.csv_writer import write_csv, write_multiple_matrices_to_csv
from io_utils.console.progress import progress
from pom.pde.Constants import TECHNOLOGICAL_ROUTE, \
    MAX_OPERATION_TIME, NUMBER_DISTRIBUTION_DENSITY_INTERVALS, X, Y, DISTRIBUTION_DENSITY_LINE, INITIAL_DATA, \
    RESULT_DATA, X_LABEL_NAME, NUMBER_OPERATION_TIME, SEED, ORDER_SIZE, TECHNOLOGICAL_PATHS_LINE, VISUAL_LINE_SET, \
    COLOR_LINE_SET, N_TECHNOLOGICAL_PATHS_LINE, N_MIDDLE_TECHNOLOGICAL_PATHS_LINE, \
    N_LAST_TECHNOLOGICAL_PATHS_LINE, BATCH_TIME_HIST, BATCH_TIME_DENSITY_LINE, \
    NUMBER_BATCH_DENSITY_INTERVALS, PROBABILITY_LINE, X_MIN, X_MAX, SIZE_PACKAGE, SHOWED_LINE, EACH_N, BACKLOGS_SIZE, \
    X_TICK_MAIN, X_TICK_AUXILIARY
from pom.pde.TechnologicalRoute import TechnologicalRoute
from pom.pde.flowshop_2m.flow_shop_analyzer import FlowShopAnalyzer
from pom.pde.initData.inizialize_data_e7_e1_01_route_normal import experiments


from pom.stochastic03.utils.Constants import PLOT_PARAMETERS, Y_LABEL_NAME
import pandas as pd
import pom.stochastic03.utils.show as show


class PdeFlow:
    initial_dimension_flow: None
    __numberExamples = 0

    def __init__(self, experiment_name):
        experiment = experiments[experiment_name]
        self.route = experiment[TECHNOLOGICAL_ROUTE]
        self.max_operation_time = experiment[MAX_OPERATION_TIME]
        self.number_distribution_density_intervals = experiment[NUMBER_DISTRIBUTION_DENSITY_INTERVALS]
        self.number_batch_density_intervals = experiment[NUMBER_BATCH_DENSITY_INTERVALS]
        self.number_operation_time = experiment[NUMBER_OPERATION_TIME]
        self.order_size = experiment[ORDER_SIZE]
        self.backlogs_size = experiment[BACKLOGS_SIZE]
        self.seed = experiment[SEED]
        self.distribution_densities = None

        self.initial_dimensionless_flow = None
        self.initial_dimension_flow = None
        self.experiment = experiments[experiment_name]  # experiment: experiment conditions.
        self.create_project_structure()

        self.numberExamples = 0





    def create_route(self):
        technological_route \
            = TechnologicalRoute(self.route, self.max_operation_time, self.number_distribution_density_intervals,
                                 self.number_operation_time, self.order_size, self.seed, self.backlogs_size)
        technological_route.fill_normalization_factor()
        self.route_operations_times = technological_route.generate_route_operations_times()
        self.generated_distribution_densities = technological_route.calculate_generated_distribution_densities()
        self.generated_technological_paths = technological_route.calculate_technological_paths(0)


        flow_shop_analyzer = FlowShopAnalyzer(self.route, self.result_data_structure, self.file_name)
        flow_shop_analyzer.calculate_operation_delays()

        random_size = round(self.number_operation_time/self.order_size) -1
        self.batch_times = self.initialization_batch_times(random_size)
        for i in range(random_size):
            times_set = technological_route.calculate_technological_paths(i * self.order_size)
            last_times_set_element_number = len(times_set) - 1
            last_times_set_element = times_set[last_times_set_element_number]
            batch_time = last_times_set_element[X][len(last_times_set_element[X])-1]
            self.batch_times[X][i] = i
            self.batch_times[Y][i] = batch_time
            progress(i, random_size, "calculate_batch_times")
        progress(random_size, random_size, "calculate_batch_times")

        self.batch_density = self.calculate_distribution_density(self.batch_times[Y],
                                                                 self.number_batch_density_intervals)
        self.probability = self.calculate_probability(self.batch_times[Y],
                                                                 self.number_batch_density_intervals)
        self.probability_per_detail = self.calculate_probability(self.batch_times[Y]/self.order_size,
                                                      self.number_batch_density_intervals)

    def calculate_distribution_density(self, values, intervals):
        max_tau = values.max() * 1.01
        min_tau = values.min()  * 0.99
        delta =(max_tau - min_tau) / intervals
        line = sorted(values)
        generated_distribution_density = self.initialization_distribution_density(intervals)
        tau = min_tau
        for k in range(intervals):
            for i in range(len(line)):
                if tau < line[i] <= tau + delta:
                    generated_distribution_density[Y][k] += 1.0 / (delta * len(line))
            tau = tau + delta
            generated_distribution_density[X][k] = tau
        return generated_distribution_density

    def calculate_probability(self, values, intervals):
        max_tau = values.max() * 1.001
        min_tau = values.min()  * 0.999
        delta =(max_tau - min_tau) / intervals
        line = sorted(values)
        generated_distribution_density = self.initialization_distribution_density(intervals)
        tau = min_tau
        for k in range(intervals):
            for i in range(len(line)):
                if tau < line[i] <= tau + delta:
                    generated_distribution_density[Y][k] += 1.0 / (delta * len(line))
            tau = tau + delta
            generated_distribution_density[X][k] = tau
        probability = self.initialization_distribution_density(intervals)
        summa = 0.0
        for k in range(intervals):
            summa += generated_distribution_density[Y][k] * delta
            probability[X][k] = generated_distribution_density[X][k]
            probability[Y][k] = summa
        return probability

    def initialization_distribution_density(self, intervals):
        distribution_density = pd.DataFrame()
        distribution_density[X] = [0.0] * intervals
        distribution_density[Y] = [0.0] * intervals
        return distribution_density


    @staticmethod
    def initialization_batch_times(random_size):
        batch_times = pd.DataFrame()
        batch_times[X] = [0.0] * random_size
        batch_times[Y] = [0.0] * random_size
        return batch_times

    # ==================================================================================================================
    def distribution_densities_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'

        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        for i in range(1, 1 + len(self.distribution_densities)):
            self.experiment[PLOT_PARAMETERS][DISTRIBUTION_DENSITY_LINE][X_LABEL_NAME] \
                = r'$\vartheta_m$'.replace('m',str(i))
            self.experiment[PLOT_PARAMETERS][DISTRIBUTION_DENSITY_LINE][Y_LABEL_NAME]\
                = r'$f_m(\vartheta_m)$'.replace('m',str(i))
            initial_dimension_flows = [self.distribution_densities[i][X].values, self.distribution_densities[i][Y].values                                   ]
            show.common_line(self.experiment, path, initial_dimension_flows, f"density{i}_", DISTRIBUTION_DENSITY_LINE)

    def generated_distribution_densities_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        for i in range(1, 1 + len(self.generated_distribution_densities)):
            self.experiment[PLOT_PARAMETERS][DISTRIBUTION_DENSITY_LINE][X_LABEL_NAME] \
                = r'$\vartheta_m$'.replace('m',str(i))
            self.experiment[PLOT_PARAMETERS][DISTRIBUTION_DENSITY_LINE][Y_LABEL_NAME] \
                = r'$f_m(\vartheta_m)$'.replace('m',str(i))
            initial_dimension_flows = [self.generated_distribution_densities[i][X].values, self.generated_distribution_densities[i][Y].values                                   ]
            show.common_line(self.experiment, path, initial_dimension_flows, f"generated_density{i}_", DISTRIBUTION_DENSITY_LINE)

    def batch_time_density_line_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result
        batch_densities = [self.batch_density[X].values, self.batch_density[Y].values                                   ]
        show.common_line(self.experiment, path, batch_densities, f"batch_density_", BATCH_TIME_DENSITY_LINE)

    def batch_time_probability_line_show(self):
        plot_name = PROBABILITY_LINE
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result
        batch_densities = [self.probability[X].values, self.probability[Y].values]
        show.common_line(self.experiment, path, batch_densities, f"probability_", plot_name)

        self.experiment[PLOT_PARAMETERS][plot_name][Y_LABEL_NAME] = r'$R_b(\tau_b)$'
        batch_densities = [self.probability[X].values, 1.0 - self.probability[Y].values]
        show.common_line(self.experiment, path, batch_densities, f"risk_", plot_name)

    def batch_time_probability_per_detail_line_show(self):
        plot_name = PROBABILITY_LINE
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        x_min= self.experiment[PLOT_PARAMETERS][plot_name][X_MIN]
        x_max= self.experiment[PLOT_PARAMETERS][plot_name][X_MAX]
        x_tick_main= self.experiment[PLOT_PARAMETERS][plot_name][X_TICK_MAIN]
        x_tick_auxiliary= self.experiment[PLOT_PARAMETERS][plot_name][X_TICK_AUXILIARY]
        x_label_name = self.experiment[PLOT_PARAMETERS][plot_name][X_LABEL_NAME]

        self.experiment[PLOT_PARAMETERS][plot_name][X_MIN] = 0.3 #0.2
        self.experiment[PLOT_PARAMETERS][plot_name][X_MAX] = 1.8 #0.7
        self.experiment[PLOT_PARAMETERS][plot_name][X_TICK_MAIN] = 0.3 #0.1
        self.experiment[PLOT_PARAMETERS][plot_name][X_TICK_AUXILIARY] = 0.15 # 0.05
        self.experiment[PLOT_PARAMETERS][plot_name][Y_LABEL_NAME] = r'$F_d(\tau_d)$'
        self.experiment[PLOT_PARAMETERS][plot_name][X_LABEL_NAME] =  r'$\tau_d$'

        batch_densities = [self.probability_per_detail[X].values, self.probability_per_detail[Y].values]
        show.common_line(self.experiment, path, batch_densities, f"probability_per_detail", plot_name)

        self.experiment[PLOT_PARAMETERS][plot_name][Y_LABEL_NAME] = r'$R_d(\tau_d)$'
        batch_densities = [self.probability_per_detail[X].values, 1.0 - self.probability_per_detail[Y].values]

        show.common_line(self.experiment, path, batch_densities, f"risk_per_detail", plot_name)
        self.experiment[PLOT_PARAMETERS][plot_name][X_MIN] = x_min
        self.experiment[PLOT_PARAMETERS][plot_name][X_MAX] = x_max
        self.experiment[PLOT_PARAMETERS][plot_name][X_TICK_MAIN] = x_tick_main
        self.experiment[PLOT_PARAMETERS][plot_name][X_TICK_AUXILIARY] = x_tick_auxiliary
        self.experiment[PLOT_PARAMETERS][plot_name][X_LABEL_NAME] = x_label_name

    def batch_time_probability_loss_line_show(self):
        plot_name = PROBABILITY_LINE
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result
        self.experiment[PLOT_PARAMETERS][plot_name][X_MIN] = 14
        self.experiment[PLOT_PARAMETERS][plot_name][X_MAX] = 34
        self.experiment[PLOT_PARAMETERS][plot_name][Y_LABEL_NAME] = r'$F_L(N_L)$'
        self.experiment[PLOT_PARAMETERS][plot_name][X_LABEL_NAME] = r'$N_L$'
        batch_densities = [60.0 - 60.0 * 14.87 / self.probability[X].values, self.probability[Y].values]
        show.common_line(self.experiment, path, batch_densities, f"probability_loss_", plot_name)

        self.experiment[PLOT_PARAMETERS][plot_name][Y_LABEL_NAME] = r'$R_L(N_L)$'
        self.experiment[PLOT_PARAMETERS][plot_name][X_LABEL_NAME] = r'$N_L$'
        batch_densities = [60.0 - 60.0 * 14.87 / self.probability[X].values, 1.0 - self.probability[Y].values]
        show.common_line(self.experiment, path, batch_densities, f"risk_loss", plot_name)

    #self.batch_density
    #self.probability

    def generated_technological_paths_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        generated_technological_paths = [self.generated_technological_paths[0][Y].values]
        each_n = min(self.experiment[SHOWED_LINE][EACH_N], self.experiment[ORDER_SIZE])
        for i in range(len(self.generated_technological_paths)):
            if i%each_n==0: # showed each 5th trajectory
                generated_technological_paths.append(self.generated_technological_paths[i][X].values)
        self.experiment[PLOT_PARAMETERS][TECHNOLOGICAL_PATHS_LINE][VISUAL_LINE_SET]\
            = self.create_visual_line_set(len(generated_technological_paths))

        self.experiment[PLOT_PARAMETERS][TECHNOLOGICAL_PATHS_LINE][COLOR_LINE_SET] \
            = self.create_color_line_set(len(generated_technological_paths))
        show.common_line(self.experiment, path, generated_technological_paths, f"generated_paths_",
                         TECHNOLOGICAL_PATHS_LINE)

    def generated_n_technological_paths_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        generated_technological_paths = [self.generated_technological_paths[0][Y].values]
        size_package = min(self.experiment[SHOWED_LINE][SIZE_PACKAGE],self.experiment[ORDER_SIZE])
        for i in range(size_package):
            generated_technological_paths.append(self.generated_technological_paths[i][X].values)
        self.experiment[PLOT_PARAMETERS][N_TECHNOLOGICAL_PATHS_LINE][VISUAL_LINE_SET] \
            = self.create_visual_line_set(len(generated_technological_paths))

        self.experiment[PLOT_PARAMETERS][N_TECHNOLOGICAL_PATHS_LINE][COLOR_LINE_SET] \
            = self.create_color_line_set(len(generated_technological_paths))

        show.common_line(self.experiment, path, generated_technological_paths, f"n_generated_paths_",
                         N_TECHNOLOGICAL_PATHS_LINE)

    def generated_n_middle_technological_paths_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        generated_technological_paths = [self.generated_technological_paths[0][Y].values]
        size = round(len(self.generated_technological_paths)/2)
        size_package = min(self.experiment[SHOWED_LINE][SIZE_PACKAGE],self.experiment[ORDER_SIZE])
        for i in range(size, min(size + size_package,self.experiment[ORDER_SIZE])):
            generated_technological_paths.append(self.generated_technological_paths[i][X].values)
        self.experiment[PLOT_PARAMETERS][N_MIDDLE_TECHNOLOGICAL_PATHS_LINE][VISUAL_LINE_SET] \
            = self.create_visual_line_set(len(generated_technological_paths))

        self.experiment[PLOT_PARAMETERS][N_MIDDLE_TECHNOLOGICAL_PATHS_LINE][COLOR_LINE_SET] \
            = self.create_color_line_set(len(generated_technological_paths))

        show.common_line(self.experiment, path, generated_technological_paths, f"n_middle_generated_paths_",
                         N_MIDDLE_TECHNOLOGICAL_PATHS_LINE)

    def generated_n_last_technological_paths_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result
        plot_name = N_LAST_TECHNOLOGICAL_PATHS_LINE
        generated_technological_paths = [self.generated_technological_paths[0][Y].values]
        size = len(self.generated_technological_paths)
        size_package = min(self.experiment[SHOWED_LINE][SIZE_PACKAGE],self.experiment[ORDER_SIZE])
        for i in range(size - size_package, size):
            generated_technological_paths.append(self.generated_technological_paths[i][X].values)
        self.experiment[PLOT_PARAMETERS][plot_name][VISUAL_LINE_SET] \
            = self.create_visual_line_set(len(generated_technological_paths))

        self.experiment[PLOT_PARAMETERS][plot_name][COLOR_LINE_SET] \
            = self.create_color_line_set(len(generated_technological_paths))

        show.common_line(self.experiment, path, generated_technological_paths, f"n_last_generated_paths_",
                         plot_name)

    def batch_time_density_show(self):
        result_data = self.result_data_structure[RESULT_DATA] + '/'
        # :param sub_directory_name: the name of the directory where the visualization data is located.
        initial_data_result = self.result_data_structure[INITIAL_DATA]
        path = result_data + self.file_name + '/' + initial_data_result

        batch_times = [self.batch_times[X].values, self.batch_times[Y].values]
        show.common_hist(self.experiment, path, batch_times, f"batch_times_", BATCH_TIME_HIST)


    @staticmethod
    def create_visual_line_set(number_line):
        visual_line_set = {}
        for i in range(number_line):
            visual_line_set[str(i)] = i
        return visual_line_set

    @staticmethod
    def create_color_line_set(number_line):
        color_line_set = {}
        for i in range(number_line):
            color_line_set[str(i)] = 'k'
        return color_line_set






    def create_project_structure(self):
        project_structure = self.experiment["project_structure"]
        self.file_name = project_structure["file_name"]
        self.files_category = project_structure["files_category"] + '/'
        self.result_data_structure = project_structure["result_data_structure"]

    def initial_load_dimension_data(self):
        load_period = self.experiment["load_period"]
        temp = pd.read_csv(self.files_category + self.file_name, sep=";", decimal=',')
        self.initial_dimension_flow = pd.DataFrame()
        self.initial_dimension_flow['time'] = [0.0] * int(temp.shape[0] / load_period)
        self.initial_dimension_flow['flow'] = [0.0] * int(temp.shape[0] / load_period)
        self.numberExamples = self.initial_dimension_flow.shape[0]

        for i in range(self.numberExamples):
            self.initial_dimension_flow['time'][i] = temp['time'][i * load_period]
            self.initial_dimension_flow['flow'][i] = temp['flow'][i * load_period]

    def check_outliers_for_initial_data(self):
        if self.numberExamples == 0:
            print("Initial data doesn't upload.")
            return

        initial_dimension_flow_mean = self.initial_dimension_flow[FLOW].mean()
        for n in range(len(self.initial_dimension_flow[FLOW])):
            value = self.initial_dimension_flow[FLOW][n]
            if (value < initial_dimension_flow_mean * 0.0):
                self.initial_dimension_flow[FLOW][n] = initial_dimension_flow_mean


    def path_to(self, source_folder):
        """
        Method creates the path to the folder with research.
        :param source_folder: the folder with research.
        :return: the path to the folder with research.
        """
        return self.result_data_structure["result_data"] + '/' + self.file_name + '/' + self.result_data_structure[
            source_folder]

    def parameter_model_save(self):
        result_data = self.result_data_structure["result_data"] + '/'
        path_file = result_data + self.file_name + "\\ModelDescription.txt"

        file = open(path_file, "w")
        self.save_parameters("Dimensionless parameters:               ",
                             self.batch_times[Y]/self.order_size, file)
        file.close()

    def save_parameters(self, description, data, file):
        file.write(description)
        file.write("\n")
        file.write("t_d_min    : %10.7f" % (data.min()))
        file.write("\n")
        file.write("t_d_max    : %10.7f" % (data.max()))
        file.write("\n")
        file.write("t_d_Mean   : %10.7f" % (data.mean()))
        file.write("\n")
        file.write("t_d_Std    : %10.7f" % (data.std()))
        file.write("\n\n")

def common_data_show(experiment,
                     path,
                     line_file_name_prefix,
                     line_plot_name,
                     hist_file_name_prefix,
                     hist_plot_name,
                     values):
    """
    Method to construct two graphs from one given data set
    :param experiment: experiment conditions.
    :param path: the path to the folder with research.
    :param line_file_name_prefix: file name prefix for the line plot.
    :param line_plot_name: the line plot name with parameters from experiment set.
    :param hist_file_name_prefix: file name prefix for the hist plot.
    :param hist_plot_name: the hist plot name with parameters from experiment set.
    :param values: set of plot-values sequence for the building plot.
    """
    show.common_line(experiment, path, values, line_file_name_prefix, line_plot_name)
    show.common_hist(experiment, path, values, hist_file_name_prefix, hist_plot_name)

