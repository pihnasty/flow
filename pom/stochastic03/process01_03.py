import copy
import math
import sys

import pandas as pd
from scipy.stats import chi2_contingency

import Graphics.Histograms.Hist as hist
import Graphics.LineCharts.LineChart as lineChart
import utils.FileUtil as file_util
import StatUtils.Extentions as extentions
import StatUtils.stat_func as stat_func
import StatUtils.show as show

# df = pd.read_csv('netflix_titles.csv', sep=",")
# numberExamples = 11591

# universal .csv
from pom.stochastic03.InitData.inizialize_data import experiments

experiment = experiments["0001"]

RESULT_DATA = 'resultData/'
FILES_CATEGORY = 'files/'
fileName = experiment["file_name"]
df = pd.read_csv(FILES_CATEGORY + fileName, sep=";", decimal=',')
numberExamples = df.shape[0]
count_of_intervals_xi2 = experiment["number_of_intervals_xi2"]

def densityExpectedValue(initialData, densityParameters):
    expectedData = copy.deepcopy(initialData)
    if densityParameters["lawDensity"] == "norm":
        for i, val in enumerate(expectedData[0]):
            value = (expectedData[0][i] - densityParameters["average"]) / densityParameters["std"]
            expectedData[1][i] = (1.0 / densityParameters["std"] / (2.0 * math.pi) ** (0.5)) * math.exp(
                -0.5 * value ** 2)

    delta = (densityParameters["max"] - densityParameters["min"]) / densityParameters["countOfIntervalsXi2"]

    pSum = sum(expectedData[1]) * delta

    for i, val in enumerate(expectedData[1]):
        expectedData[1][i] = expectedData[1][i]/pSum

    return expectedData

def frequencyValue(data, frecuencyParameters):
    frecuencyData = copy.deepcopy(data)
    for i, val in enumerate(frecuencyData[0]):
        frecuencyData[1][i] = data[1][i] * frecuencyParameters["delta"] * frecuencyParameters["numberExamples"]
    return frecuencyData

# ================================================ initial =================================================

fontsize=14

extentions.c1_plot(fileName, fontsize)

path = RESULT_DATA + fileName + '/initial'
file_util.make_dir_if_not(path)
column_name = 'flow_line'
xlabelName = r'$t$'
lineChart.linePlot(path + '/' + column_name, df['time'].values
                   , df['flow'].values, df['flow'].values, xlabelName, r'$\lambda(t)$'
                   , 0.7, _dpi=600, xMin=df['time'].min(), xMax=df['time'].max(), _fontsize=12)

column_name = 'time'
hist.histPlot(path + '/' + column_name, df, column_name, count_of_intervals_xi2, True, 'density', r'$t$', 0.7, 0.7, _dpi=600)
column_name = 'flow'
hist.histPlot(path + '/' + column_name, df, column_name, count_of_intervals_xi2, True, r'f($\lambda$)', r'$\lambda$', 0.7, 0.7,
              _dpi=600)

averageColumn=df['flow'].mean()
stdColumn=df['flow'].std()

d2=copy.copy(df)
d2['flow']=(df['flow'])/averageColumn

averageColumnD2=d2.mean()
stdColumnD2=d2.std()

tMin=df['time'].min()
tMax=df['time'].max()
d2['time'] = (df['time'] - tMin) / (tMax - tMin)
#             * 2
# ============================================= initial_dimensionless ======================================
path = RESULT_DATA + fileName + '/initial_dimensionless'
file_util.make_dir_if_not(path)
column_name ='flow_line'
xlabelName = r'$\tau$'
lineChart.linePlot(path + '/' + column_name, d2['time'].values
         , d2['flow'].values, d2['flow'].values, xlabelName, r'$\gamma(\tau)$'
         , 0.7, _dpi=600
         , xMin = d2['time'].min(), xMax = d2['time'].max()
         , y1Min= d2['flow'].min(), y1Max= d2['flow'].max(), _fontsize=8)
column_name ='time'
hist.histPlot(path + '/' + column_name, d2, column_name, count_of_intervals_xi2, True, 'density', r'$\tau$', 0.7, 0.7,
              _dpi=600)
column_name ='flow'
hist.histPlot(path + '/' + column_name, d2, column_name, count_of_intervals_xi2, True, r'f($\gamma$)'
              , r'$\gamma$', 0.7, 0.7, _dpi=600)

d3 = stat_func.density_values(d2['flow'].values, count_of_intervals_xi2)

densityParameters= {"lawDensity" : "norm"
    , "min" : d2['flow'].min()
    , "max" : d2['flow'].max()
    , "countOfIntervalsXi2" : count_of_intervals_xi2
    , "average" : 0.0, "std" : 1.0}
d3normal = densityExpectedValue(d3, densityParameters)
# ================================================ check ==============================================================
x = d3[0]
y1 = d3[1]
y2 = d3normal[1]
flow_densities = [d3[0], d3[1], d3normal[1]]
show.flow_density(experiment, '/check', flow_densities, 'flow_density', r'$\gamma$', r'f($\gamma$)', 0.7)
show.frequency_plot_hist(
    experiment, '/check', x, d3normal[1], d2['flow'], 'flow_frequency_hist', r'$\gamma$', r'f($\gamma$)', 0.7
)

# # this module compares two distribution functions: experimental and with normal distribution,
# applying Pearson's criterion

# path = RESULT_DATA + fileName + '/check'
# frequencyParameters = {"delta": (d2['flow'].max() - d2['flow'].min()) / count_of_intervals_xi2,
#                        "numberExamples": numberExamples}
# d31 = frequencyValue(d3, frequencyParameters)
# d31normal = frequencyValue(d3normal, frequencyParameters)
# columName ='flow_frequency'
# xlabelName = r'$\gamma$'
# lineChart.linePlot(path + '/' + columName, d31[0], d31[1], d31[1], xlabelName, r'Frequency of the value '+xlabelName
#                    # lineChart.linePlot(path + '/' + columName, d31[0], d31[1], d31normal[1], xlabelName,
#                    # r'Frequency of the value '+xlabelName
#          , 0.7, _dpi=600
#          , xMin=min(d31[0]), xMax=max( d31[0])
#          , y1Min=min(d31[1]), y1Max=max(d31[1]), _fontsize=8)
#
# d4=[d31[1], d31normal[1]]
# kf = chi2_contingency(d4)
# print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)



# ================================================ autoKorelationCoeffitient ===========================================
d_auto_korelation_centered_mass=copy.copy(d2)
# !!!!!! is transformed the dimensionless flow into a centered dimensionless flow with an average constant in time
d_auto_korelation_centered_mass['flow']=(d2['flow']) - d2['flow'].mean()
period = 200   #  The variable [period] is introduced to reduce calculations.
# The variable specifies that only the point for which the ratio is valid [i % period == 0] is calculated for the plot.

#===============================================================================
if experiment["show_prepare_k"] == True:
    extentions.c0_show_k0(fileName, d_auto_korelation_centered_mass, period)
    extentions.c0_show_1_v(fileName, d_auto_korelation_centered_mass, period)
    extentions.c0_show_work_equals_0_5(fileName, d_auto_korelation_centered_mass, period)
    extentions.c0_show_test_equals_0_5(fileName, d_auto_korelation_centered_mass, period)
    extentions.c0_show_var2(experiment, d_auto_korelation_centered_mass)
    extentions.c0_show_tau_tau_minus_v_tau_plus_v(experiment, d_auto_korelation_centered_mass)



# dimensionless_flow=copy.copy(d2)
# extentions.prediction_std(experiment["period"], experiment["tau_correlation"], dimensionless_flow)


dimensionless_flow = copy.copy(d2)
fourier_coefficients_gamma = [0] * round(experiment["number_of_harmonics"])

for n in range(len(fourier_coefficients_gamma)):
    print(['n=', n])
    fourier_coefficients_gamma[n] = extentions.fourier_coefficients(experiment["period"], dimensionless_flow, n)

approximated_gamma = extentions.approximated_gamma(experiment["period"], fourier_coefficients_gamma, dimensionless_flow)
extentions.approximated_gamma_show(
    experiment
    , dimensionless_flow
    , approximated_gamma
    , 'approximatedGamma'
    , r'$\gamma$($\tau$)'
)

dimensionless_flow = copy.copy(d2)
fourier_coefficients_gamma_d = [0] * round(experiment["number_of_harmonics"])
std = d_auto_korelation_centered_mass["flow"].std()

c0_tau_tau_minus_v_tau_plus_vs = extentions.c0_tau_tau_minus_v_tau_plus_v_tau_plus_1_s(
    experiment["period"]
    , dimensionless_flow
)
extentions.c0_show_tau_tau_minus_v_tau_plus_v2(
    experiment
    , c0_tau_tau_minus_v_tau_plus_vs[0]
    , c0_tau_tau_minus_v_tau_plus_vs[1]
)

for n in range(len(fourier_coefficients_gamma_d)):
    print(['n=', n])
    fourier_coefficients_gamma_d[n] = extentions.fourier_coefficients_d(
        experiment["period"]
        , experiment["tau_correlation"]
        , std
        , experiment["relative_sigma_correlation"]
        , c0_tau_tau_minus_v_tau_plus_vs
        , fourier_coefficients_gamma
        , n)

approximated_gamma_d = extentions.approximated_gamma(
    experiment["period"]
    , fourier_coefficients_gamma_d
    , dimensionless_flow
)
extentions.approximated_gamma_show(
    experiment
    , dimensionless_flow
    , approximated_gamma_d
    , 'approximatedGamma_d_'
    , r'$\gamma_d$($\tau$)'
)


# ================================================ autoKorelationCoeffitient ===========================================
d_auto_korelation_centered_mass2=copy.copy(d2)
# !!!!!! is transformed the dimensionless flow into a centered dimensionless flow with an average constant in time
d_auto_korelation_centered_mass2['flow']=(d2['flow']) - approximated_gamma_d
PERIOD = 200   #  The variable [period] is introduced to reduce calculations.
# The variable specifies that only the point for which the ratio is valid [i % period == 0] is calculated for the plot.

extentions.approximated_gamma_s_show(
    experiment
    , dimensionless_flow
    , d_auto_korelation_centered_mass2
    , 'approximatedGamma_s_'
    , r'$\gamma_s$($\tau$)'
)

approximated_gamma_d2=copy.copy(d_auto_korelation_centered_mass2)
approximated_gamma_d2["flow"]=approximated_gamma_d
approximated_gamma_d2["time"]=dimensionless_flow["time"]
extentions.approximated_gamma_s_show(
    experiment
    , dimensionless_flow
    , approximated_gamma_d2
    , 'approximatedGamma_d2_'
    , r'$\gamma_d$($\tau$)'
)
RESULT_DATA_CATEDORY = RESULT_DATA + experiment["file_name"] + '/output/'
file_util.make_dir_if_not(RESULT_DATA_CATEDORY)
approximated_gamma_d2.to_csv(RESULT_DATA_CATEDORY + 'gamma_d.csv', sep=";", decimal=',', index=False)
approximated_gamma_s2 = copy.copy(approximated_gamma_d2)
approximated_gamma_s2['flow'] = dimensionless_flow['flow'] - approximated_gamma_d2['flow']
approximated_gamma_s2.to_csv(RESULT_DATA_CATEDORY + 'gamma_s.csv', sep=";", decimal=',', index=False)
dimensionless_flow.to_csv(RESULT_DATA_CATEDORY + 'gamma.csv', sep=";", decimal=',', index=False)

fourier_coefficients_gamma_d2 = pd.DataFrame()
fourier_coefficients_gamma_d2['number'] = range(experiment["number_of_harmonics"])
fourier_coefficients_gamma_d2['fourier coefficient'] = fourier_coefficients_gamma_d
fourier_coefficients_gamma_d2.to_csv(RESULT_DATA_CATEDORY + 'fourier_coefficients_gamma_d.csv', sep=";", decimal=','
                                     , index=False)

#===============================================================================
if experiment["show_prepare_k"]:
    extentions.c0_show_k0(fileName, d_auto_korelation_centered_mass2, period)
    extentions.c0_show_1_v(fileName, d_auto_korelation_centered_mass2, period)
    extentions.c0_show_work_equals_0_5(fileName, d_auto_korelation_centered_mass2, period)
    extentions.c0_show_test_equals_0_5(fileName, d_auto_korelation_centered_mass2, period)
    extentions.c0_show_var2(experiment, d_auto_korelation_centered_mass2)
    extentions.c0_show_tau_tau_minus_v_tau_plus_v(experiment, d_auto_korelation_centered_mass2)

# ================================================ check after Fourier analysis  =======================================
density_values_lambda_s = stat_func.density_values(
    d_auto_korelation_centered_mass2['flow'].values, experiment["number_of_intervals_xi2"]
)
flow_densities = [density_values_lambda_s[0], density_values_lambda_s[1]]

show.flow_density(
    experiment, '/check_after_Fourier_analysis', flow_densities, 'flow_density', r'$\gamma_s$', r'f($\gamma_s$)', 0.7
)
show.frequency_plot_hist(
    experiment
    , '/check_after_Fourier_analysis'
    , density_values_lambda_s[0]
    , density_values_lambda_s[1]
    , d_auto_korelation_centered_mass2['flow'], 'flow_frequency_hist', r'$\gamma_s$', r'f($\gamma_s$)', 0.7
)

sys.exit()
