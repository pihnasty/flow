import copy
import math
import sys
import InputFlow as flow

import Graphics.Histograms.Hist as hist
import Graphics.LineCharts.LineChart as lineChart
import utils.FileUtil as file_util
import StatUtils.Extentions as extentions
import StatUtils.stat_func as stat_func
import StatUtils.show as show

from datetime import datetime




start_time = datetime.now()

input_flow = flow.InputFlow(
    "2023_05_23_dataset_2021_BhAsHuHoEv"
)

input_flow.initial_dimension_data_show()
input_flow.initial_dimensionless_data_show()
input_flow.initial_dimensionless_data_show2()
input_flow.g_g2_show()
input_flow.execute_initial_correlation_part_first()
input_flow.initial_correlation_part_first_show()
input_flow.execute_initial_correlation_part_second()
input_flow.initial_correlation_part_second_show()

input_flow.initial_dimensionless_data_correct_show2()
input_flow.g_g2_correct_show()
input_flow.execute_initial_correlation_part_first_correct()
input_flow.initial_correlation_part_first_correct_show()
input_flow.execute_initial_correlation_part_second_correct()
input_flow.initial_correlation_part_second_correct_show()

print('\nAll operations are finished for:', datetime.now() - start_time)

sys.exit()
