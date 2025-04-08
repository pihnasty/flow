import sys
import InputFlow as flow
from datetime import datetime



start_time = datetime.now()
file_name = "C:\\A\\Pro\\flow\\pom\\stochastic03\\project\\dataset_2020_ZeYaWuWa\\data.json"
input_flow = flow.InputFlow(file_name)
turn_on_test = True
NUMBER_OF_INITIAL_INTERVALS_TO_GENERATE = 8

input_flow.initial_load_dimension_data()
input_flow.transform_initial_dimension_to_dimensionless()

sys.exit()
