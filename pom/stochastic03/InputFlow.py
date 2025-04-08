from common_utils.Graph.constants import Constants
from common_utils.Graph.utils.csv.csv_reader import read_csv
from common_utils.Graph.utils.csv.csv_writer import write_csv
from common_utils.Graph.utils.json.json_reader import read_json
import pandas as pd

from common_utils.approximate_model.approximate_type import ApproximateType
from common_utils.dim_less.dimensionless import Dimensionless
from common_utils.flow_constants import APPROXIMATE_TYPE, STD, DIMENSIONLESS, APPROXIMATE, FLOW, TIME, DIMLESS_FLOW, TAU
from common_utils.approximate_model.SpectrumWithMoreRealizationApproximate import \
    SpectrumWithMoreRealizationApproximate


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
        csv_input_data_path = self.model_parameters[Constants.JsonNames.input_data_paths]["1"][Constants.JsonNames.path]
        csv_output_data_path = self.model_parameters[Constants.JsonNames.output_data_paths]["1"][Constants.JsonNames.path]
        self.csv_data = read_csv(csv_input_data_path)

        time = Constants.JsonNames.time
        flow = Constants.JsonNames.flow
        load_period =self.model_parameters[Constants.JsonNames.input_data_paths]["1"][Constants.JsonNames.load_period]
        self.initial_dimension_flow[time] = [0.0] * int(self.csv_data.shape[0] / load_period)
        self.initial_dimension_flow[Constants.JsonNames.flow] = [0.0] * int(self.csv_data.shape[0] / load_period)
        self.numberExamples = self.initial_dimension_flow.shape[0]

        for i in range(self.numberExamples):
            self.initial_dimension_flow[time][i] = self.csv_data[time][i * load_period]
            self.initial_dimension_flow[flow][i] = self.csv_data[flow][i * load_period]

        write_csv(self.initial_dimension_flow, csv_output_data_path)

    def transform_initial_dimension_to_dimensionless(self):
        dimensionless_config = self.model_parameters[DIMENSIONLESS]
        if ApproximateType[
            self.model_parameters[APPROXIMATE][APPROXIMATE_TYPE]] == ApproximateType.SPECTRUM_WITH_MORE_REALIZATION:
            dim, mean, std = SpectrumWithMoreRealizationApproximate(self.initial_dimension_flow,
                                                                    self.model_parameters[APPROXIMATE]).get_param()
            dimensionless_config[STD] = std

        initial_dimensionless_flow = Dimensionless(self.initial_dimension_flow, dimensionless_config).get_dim_less()
        self.initial_dimension_flow[DIMLESS_FLOW] = initial_dimensionless_flow[FLOW]
        self.initial_dimension_flow[TAU] = initial_dimensionless_flow[TIME]

        csv_output_data_path = self.model_parameters[Constants.JsonNames.output_data_paths]["1"][Constants.JsonNames.path]
        write_csv(self.initial_dimension_flow, csv_output_data_path)

