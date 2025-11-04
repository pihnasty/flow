import copy
import math

from approximate_model.ApproximateDimension import ApproximateDimension

from Graph.constants import Constants
from Graph.utils.csv.csv_reader import read_csv
from Graph.utils.csv.csv_writer import write_csv
from Graph.utils.json.json_reader import read_json
import pandas as pd

from approximate_model.approximate_type import ApproximateType
from corr_func.correlation_function import CorrelationFunction
from dim_less.dimensionless import Dimensionless
from constants.flow_constants import APPROXIMATE_TYPE, STD, DIMENSIONLESS, APPROXIMATE, FLOW, TIME, DIMLESS_FLOW, TAU, \
    NUMBER_OF_INTERVALS, NUMBER_OF_HARMONICS, APPROXIMATE_DIMLESS_FLOW, APPROXIMATE_ERR_DIMLESS_FLOW, \
    HARMONIC_NUMBER, CORRELATION, VARTHETA, PROBABILITY, \
    NUMBER_DENSITY_INTERVALS, FLOW_PROBABILITY_Y, FLOW_PROBABILITY_X, FLOW_DENSITY_Y, CRITICAL_PROB_VALUE, \
    DIMLESS_FLOW3, AMPLITUDES_FOR_INTERVAL, PHASES_FOR_INTERVAL, \
    COS_HARMONICS_FOR_INTERVAL, SIN_HARMONICS_FOR_INTERVAL
from approximate_model.spectrum_approximation import SpectrumWithMoreRealizationApproximate
from io_utils.console.progress import progress
from maths.stats import calculate_probability, calculate_density


class InputFlow:
    initial_dimension_flow: None
    __numberExamples = 0

    def __init__(self, file_name):
        self.json_data = read_json(file_name)
        self.model_parameters = self.json_data[Constants.JsonNames.model_parameters]
        self.initial_dimension_flow : pd.DataFrame = pd.DataFrame()
        self.csv_data = None
        self.numberExamples = 0

    def initial_load_dimension_data(self):
        csv_input_data_path= self.model_parameters[Constants.JsonNames.input_data_paths]["1"][Constants.JsonNames.path]
        self.csv_data = read_csv(csv_input_data_path)
        self.limit_csv_with_time_less_than_given()
        time = Constants.JsonNames.time
        flow = Constants.JsonNames.flow
        load_period = self.model_parameters[Constants.JsonNames.input_data_paths]["1"][Constants.JsonNames.load_period]
        self.initial_dimension_flow[time] = [0.0] * int(self.csv_data.shape[0] / load_period)
        self.initial_dimension_flow[Constants.JsonNames.flow] = [0.0] * int(self.csv_data.shape[0] / load_period)
        self.numberExamples = self.initial_dimension_flow.shape[0]

        for i in range(self.numberExamples):
            self.initial_dimension_flow[time][i] = self.csv_data[time][i * load_period]
            self.initial_dimension_flow[flow][i] = self.csv_data[flow][i * load_period]

    def transform_initial_dimension_to_dimensionless(self):
        dimensionless_config = self.model_parameters[DIMENSIONLESS]
        if ApproximateType[
            self.model_parameters[APPROXIMATE][APPROXIMATE_TYPE]] == ApproximateType.SPECTRUM_WITH_MORE_REALIZATION:
            dim, mean, std = SpectrumWithMoreRealizationApproximate(self.initial_dimension_flow,
                                                                    self.model_parameters[APPROXIMATE]).get_param()
            dimensionless_config[STD] = std

        initial_dimensionless_flow = Dimensionless(self.initial_dimension_flow, dimensionless_config).get_dim_less()
        self._add_column(initial_dimensionless_flow[FLOW], DIMLESS_FLOW)
        self._add_column(initial_dimensionless_flow[TIME], TAU)

    def approximate_dimensionless(self):
        approximate_dimension = ApproximateDimension(
            pd.DataFrame(copy.deepcopy({
                TIME: self.initial_dimension_flow[TAU],
                FLOW: self.initial_dimension_flow[DIMLESS_FLOW]
            })),
            self.model_parameters[APPROXIMATE]
        )
        approximate_initial_dimensionless_flow = approximate_dimension.get_approximate_dim()
        # need to discuss
        self.approximate_tau_sequence = approximate_dimension.get_tau_sequence()

        self._add_column(range(self.model_parameters[APPROXIMATE][NUMBER_OF_HARMONICS]), HARMONIC_NUMBER)
        cos_harmonic_values, sin_harmonic_values = approximate_dimension.get_cos_and_sin_harmonic_values()
        amplitudes_for_intervals, phases_for_intervals = approximate_dimension.get_amplitudes_and_phases_for_interval()

        for i in range(self.model_parameters[APPROXIMATE][NUMBER_OF_INTERVALS]):
            self._add_column(cos_harmonic_values[i], COS_HARMONICS_FOR_INTERVAL + str(i + 1))
            self._add_column(sin_harmonic_values[i], SIN_HARMONICS_FOR_INTERVAL + str(i + 1))
            self._add_column(amplitudes_for_intervals[i], AMPLITUDES_FOR_INTERVAL + str(i + 1))
            self._add_column(phases_for_intervals[i], PHASES_FOR_INTERVAL + str(i + 1))

        self._add_column(approximate_dimension.get_error_approximate_dim()[FLOW], APPROXIMATE_ERR_DIMLESS_FLOW)
        self._add_column(approximate_initial_dimensionless_flow[FLOW], APPROXIMATE_DIMLESS_FLOW)
        progress(1, 1, "approximate_dimensionless \n")

    def execute_correlation(self):
        dim = pd.DataFrame(copy.deepcopy({
            TIME: self.initial_dimension_flow[TAU],
            FLOW: self.initial_dimension_flow[DIMLESS_FLOW]
        }))
        correlation_function = CorrelationFunction(dim, self.model_parameters[CORRELATION]).get_correlation()
        # self.approximate_initial_correlation \
        #     = CorrelationFunction(self.approximate_initial_dimensionless_flow, self.experiment[PERIOD]).get_correlation()
        # self.generated_correlation \
        #     = CorrelationFunction(self.generated_dimensionless_flow, self.experiment[PERIOD]).get_correlation()
        # self.long_generated_correlation \
        #     = CorrelationFunction(self.long_generated_dimensionless_flow, self.experiment[PERIOD]).get_correlation()
        self._add_column(correlation_function[CORRELATION], CORRELATION, 1.0)
        self._add_column(correlation_function[TIME], VARTHETA, 1.0)

    def execute_probability(self):
        _, density =  calculate_density(
            self.initial_dimension_flow[DIMLESS_FLOW],
            self.model_parameters[PROBABILITY][NUMBER_DENSITY_INTERVALS],
            FLOW_DENSITY_Y, FLOW_PROBABILITY_X
        )
        probability =  calculate_probability(
            self.initial_dimension_flow[DIMLESS_FLOW],
            self.model_parameters[PROBABILITY][NUMBER_DENSITY_INTERVALS],
            FLOW_PROBABILITY_Y, FLOW_PROBABILITY_X
        )

        critical_prob_value = self.model_parameters[PROBABILITY][CRITICAL_PROB_VALUE]

        dimension_flow_for_conveyor3 = self.execute_dimension_flow_for_conveyor3(1.0)

        self._add_column(probability[FLOW_PROBABILITY_Y], FLOW_PROBABILITY_Y, 1.0)
        self._add_column(probability[FLOW_PROBABILITY_X], FLOW_PROBABILITY_X, 2.0)

        self._add_column(density[FLOW_DENSITY_Y], FLOW_DENSITY_Y, 1.0)
        self._add_column(
            [critical_prob_value]*len(probability[FLOW_PROBABILITY_Y]), CRITICAL_PROB_VALUE, critical_prob_value
        )

    def execute_dimension_flow_for_conveyor3(self, critical_prob_value):
        dimension_flow_for_conveyor3 = pd.DataFrame(copy.deepcopy({
            TAU: self.initial_dimension_flow[TAU],
            DIMLESS_FLOW3: self.initial_dimension_flow[DIMLESS_FLOW]
        }))
        for i in range(len(dimension_flow_for_conveyor3[DIMLESS_FLOW3])):
            if dimension_flow_for_conveyor3[DIMLESS_FLOW3][i] > critical_prob_value:
                dimension_flow_for_conveyor3[DIMLESS_FLOW3][i] = critical_prob_value
        return dimension_flow_for_conveyor3

    def write_to_scv(self):
        csv_output_data_path = self.model_parameters[Constants.JsonNames.output_data_paths]["1"][
            Constants.JsonNames.path]
        write_csv(self.initial_dimension_flow, csv_output_data_path)

    def _add_column(self,column, column_name, default_value = 0.0):
        required_size = len(self.initial_dimension_flow)
        current_size = len(column)
        if current_size < required_size:
            padding = [default_value] * (required_size - current_size)
            column = list(column) + padding
        elif current_size < required_size:
            column = column[:required_size]
        self.initial_dimension_flow[column_name] = column

    def limit_csv_with_time_less_than_given(self):
        dimensionless_config = self.model_parameters[DIMENSIONLESS]
        if dimensionless_config[Constants.JsonNames.pi2_criterion]:
            self.csv_data = self.csv_data[
                self.csv_data[Constants.JsonNames.time] < dimensionless_config[Constants.JsonNames.max_time_value]
                ]

    def paremeter_model_save(self):
        path_file = self.model_parameters[Constants.JsonNames.output_data_paths]["2"][Constants.JsonNames.path]
        file = open(path_file, "w")
        self.save_parameters("Dimension parameters:               ",
                             self.initial_dimension_flow, FLOW, TIME, file)
        self.save_parameters("Dimensionless parameters:               ",
                             self.initial_dimension_flow, DIMLESS_FLOW, TAU, file)
        self.save_parameters("Approximated dimensionless parameters:               ",
                             self.initial_dimension_flow, APPROXIMATE_DIMLESS_FLOW, TAU, file)
        file.write("\n\n")
        file.close()

    def save_parameters(self, description, data, y_row_name, x_row_name,  file):
        file.write(description)
        file.write("\n")
        file.write("tMin       : %10.7f" % (data[x_row_name].min()))
        file.write("\n")
        file.write("tMax       : %10.7f" % (data[x_row_name].max()))
        file.write("\n")
        file.write("flowMin    : %10.7f" % (data[y_row_name].min()))
        file.write("\n")
        file.write("flowMax    : %10.7f" % (data[y_row_name].max()))
        file.write("\n")
        file.write("flowMean   : %10.7f" % (data[y_row_name].mean()))
        file.write("\n")
        file.write("flowStd    : %10.7f" % (data[y_row_name].std()))
        file.write("\n")
        file.write("pi1=flowMean/flowStd : %10.7f" % (data[y_row_name].std()/data[y_row_name].mean()))
        file.write("Max time value       : %10.7f" % (self.model_parameters[DIMENSIONLESS][Constants.JsonNames.max_time_value]))
        file.write("\n\n")
