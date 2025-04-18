"""
Main execution script for transforming and approximating input flow data.

Steps:
1. Load dimension data from a JSON file.
2. Transform data to dimensionless form.
3. Approximate the dimensionless flow.
4. Save the results to a CSV file.
"""
from datetime import datetime
import sys

from pom.stochastic03.InputFlow import InputFlow

start_time = datetime.now()
FILE_NAME = "C:\\A\\Pro\\flow\\pom\\stochastic03\\project\\dataset_2020_ZeYaWuWa\\data.json"
input_flow = InputFlow(FILE_NAME)

input_flow.initial_load_dimension_data()
input_flow.transform_initial_dimension_to_dimensionless()
input_flow.approximate_dimensionless()
input_flow.execute_correlation()
input_flow.execute_probability()
input_flow.write_to_scv()

sys.exit()
