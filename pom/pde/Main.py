import sys
import PdeFlow as flow
from datetime import datetime


start_time = datetime.now()

input_flow = flow.PdeFlow("e7_e1_01")



input_flow.create_route()
#input_flow.distribution_densities_show()
input_flow.generated_distribution_densities_show()
input_flow.generated_technological_paths_show()
input_flow.generated_n_technological_paths_show()
input_flow.generated_n_middle_technological_paths_show()
input_flow.generated_n_last_technological_paths_show()
input_flow.batch_time_density_show()
input_flow.batch_time_density_line_show()
input_flow.batch_time_probability_line_show()
input_flow.batch_time_probability_loss_line_show()
input_flow.parameter_model_save()




# input_flow.check_outliers_for_initial_data()
#
# input_flow.transform_initial_dimension_to_dimensionless()
# input_flow.initial_dimensionless_data_show()
#
# input_flow.approximate_dimensionless()
# input_flow.approximate_initial_dimensionless_data_show()
# #===========================================================
# input_flow.generate_dimensionless()
# input_flow.generated_dimensionless_data_show()
#
# input_flow.execute_init_correlation()
# input_flow.initial_correlation_show()

# input_flow.get_numeric_fourier_coefficients_by_correlation_function()
# input_flow.get_correlation_function_by_fourier_coefficients()
# input_flow.correlation_by_fourier_coefficients_show()

# input_flow.execute_generator_dimensionless_flow('A_gauss_T_exp')
# input_flow.generator_dimensionless_data_show()
#
# input_flow.execute_genetator_correlation()
# input_flow.genetator_correlation_show()
#
# input_flow.execute_long_genetator_correlation()
# input_flow.long_genetator_correlation_show()
#
# input_flow.gamma_optimum_spectrum_show()
# input_flow.paremeter_model_save()

print()
#input_flow.test_theory_cor_function_exp_show()

print('\nAll operations are finished for:', datetime.now() - start_time)


sys.exit()
