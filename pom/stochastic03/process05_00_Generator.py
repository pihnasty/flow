import sys
import InputFlow04 as flow
from datetime import datetime

start_time = datetime.now()

input_flow = flow.InputFlow04(
    # "2023_05_23_dataset_2013_KoStBe_CopyForGenerator"
    # "2023_05_23_dataset_2012_St_CopyForGenerator"
    # "2023_05_23_dataset_2018_BuyCopyForGenerator"
    # "2023_05_23_dataset_2013_KoStBeCopyForGenerator"
    # "2023_05_23_dataset_2010_JeRiBeStJeMiRaCopyForGenerator"
#    "2023_05_23_dataset_2021_BhAsHuHoEvCopyForGenerator"
      "2023_05_23_dataset_2021_BhAsHuHoEvCopyForGenerator2"
#      "2023_05_23_dataset_2021_BhAsHuHoEvCopyForGenerator3"
)
turn_on_test = True


input_flow.initial_load_dimension_data()
input_flow.initial_dimension_data_show()
input_flow.check_outliers_for_initial_data()

input_flow.transform_initial_dimension_to_dimensionless()
input_flow.initial_dimensionless_data_show()

input_flow.execute_initial_correlation_aproximate()
input_flow.initial_correlation_aproximate_show()

input_flow.get_numeric_fourier_coefficients_by_correlation_function()
input_flow.get_correlation_function_by_fourier_coefficients()
input_flow.correlation_by_fourier_coefficients_show()

input_flow.execute_generator_dimensionless_flow('A_gauss_T_exp')
input_flow.generator_dimensionless_data_show()

input_flow.execute_genetator_correlation()
input_flow.genetator_correlation_show()

input_flow.execute_long_genetator_correlation()
input_flow.long_genetator_correlation_show()

input_flow.gamma_optimum_spectrum_show()
input_flow.paremeter_model_save()

print()
#input_flow.test_theory_cor_function_exp_show()

print('\nAll operations are finished for:', datetime.now() - start_time)


# input_flow.g_g2_show()
#

#
#
#
#
# if(turn_on_test):
#     # input_flow.execute_initial_correlation_ideal()
#     # input_flow.initial_correlation_ideal_show()
#
#     input_flow.execute_initial_correlation_aproximate()
#     input_flow.initial_correlation_aproximate_show()
#
#     number_of_harmonics = 2
#      input_flow.test_execute_fourier_series_aproximate_theory_cor_function_exp(number_of_harmonics)
#     input_flow.test_theory_cor_function_exp_show()
#     input_flow.test_execute_fourier_series_aproximate_theory_cor_function_exp_1_plus_tau(number_of_harmonics)
#     input_flow.test_theory_cor_function_exp_1_plus_tau_show()
#     input_flow.test_execute_fourier_series_aproximate_theory_cor_function_exp_1_minus_tau(number_of_harmonics)
#     input_flow.test_theory_cor_function_exp_1_minus_tau_show()
#     input_flow.test_execute_fourier_series_aproximate_theory_cor_function_exp_cos_betta_tau(number_of_harmonics)
#     input_flow.test_theory_cor_function_exp_cos_betta_tau_show()
#
# input_flow.typization_by_correlation_function()
#
# input_flow.calculate_gamma_optimum_s()
# input_flow.gamma_optimum_s_show()

#
# input_flow.gamma_optimum_d_show()
#
# input_flow.execute_optimal_correlation_aproximate()
# input_flow.optimal_correlation_aproximate_show()
#
# input_flow.execute_optimal_correlation_ideal()
# input_flow.optimal_correlation_ideal_show()
#
# input_flow.paremeter_model_save()
#
#
# input_flow.execute_initial_correlation_part_second()
# input_flow.initial_correlation_part_second_show()
#
# input_flow.initial_dimensionless_data_correct_show2()
# input_flow.g_g2_correct_show()
# input_flow.execute_initial_correlation_part_first_correct()
# input_flow.initial_correlation_part_first_correct_show()
# input_flow.execute_initial_correlation_part_second_correct()
# input_flow.initial_correlation_part_second_correct_show()
#
# print('\nAll operations are finished for:', datetime.now() - start_time)

sys.exit()
