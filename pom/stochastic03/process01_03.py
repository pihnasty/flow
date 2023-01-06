import copy
import math
import sys

import pandas as pd
from scipy.stats import chi2_contingency

import Graphics.CombinedCharts.LineHistChart as lineHistChart
import Graphics.Histograms.Hist as hist
import Graphics.LineCharts.LineChart as lineChart
import utils.FileUtil as file_util
import StatUtils.Extentions as extentions

# df = pd.read_csv('netflix_titles.csv', sep=",")
# numberExamples = 11591

# universal .csv
from pom.stochastic03.InitData.inizialize_data import experiments

experiment = experiments["0001"]




filesCategory = 'files/'
fileName = experiment["file_name"]
df = pd.read_csv(filesCategory + fileName, sep=";", decimal=',')
numberExamples = df.shape[0]
# KaKr
# df = pd.read_csv('dataset_2021_KaKr.csv', sep=";" , decimal=',')
# numberExamples = 57951


# PiIv
# df = pd.read_csv('datasetPiIv_gamma52.csv', sep=";" , decimal=',')
# numberExamples = 999

# countOfIntervalsXi2 = 5.0*math.sqrt(numberExamples)
# countOfIntervalsXi2 = 5.0*math.log10(numberExamples)
countOfIntervalsXi2 = 50

def densityValue(initialColumnData, minValue, maxValue, numberOfBars):
    delta = (maxValue - minValue)/numberOfBars
    columnData = sorted(initialColumnData)
    elementSize = len(columnData)
    indexIndex = 0
    intervalValue = minValue + delta
    xValue = [0] * numberOfBars
    yValue = [0] * numberOfBars
    xValue [0] = intervalValue
    for value in enumerate(columnData):
        if value[1] < intervalValue:
            yValue[indexIndex] += 1 / elementSize / delta
        else:
            indexIndex += 1
            if indexIndex < len(xValue):
                intervalValue = intervalValue + delta
                xValue[indexIndex] = intervalValue
    returnValue = [xValue, yValue]
    return returnValue


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

path = 'figures/'+ fileName + '/initial'
file_util.make_dir_if_not(path)
columName = 'flow_line'
xlabelName = r'$t$'
lineChart.linePlot(path + '/' + columName, df['time'].values
                   , df['flow'].values, df['flow'].values, xlabelName, r'$\lambda(t)$'
                   , 0.7, _dpi=600, xMin=df['time'].min(), xMax=df['time'].max(), _fontsize=12)

columName = 'time'
hist.histPlot(path + '/' + columName, df, columName, countOfIntervalsXi2, True, 'density', r'$t$', 0.7, 0.7, _dpi=600)
columName = 'flow'
hist.histPlot(path + '/' + columName, df, columName, countOfIntervalsXi2, True, r'f($\lambda$)', r'$\lambda$', 0.7, 0.7,
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
path = 'figures/' + fileName + '/initial_dimensionless'
file_util.make_dir_if_not(path)
columName ='flow_line'
xlabelName = r'$\tau$'
lineChart.linePlot(path + '/' + columName, d2['time'].values
         , d2['flow'].values, d2['flow'].values, xlabelName, r'$\gamma(\tau)$'
         , 0.7, _dpi=600
         , xMin = d2['time'].min(), xMax = d2['time'].max()
         , y1Min= d2['flow'].min(), y1Max= d2['flow'].max(), _fontsize=8)
columName ='time'
hist.histPlot(path + '/' + columName, d2, columName, countOfIntervalsXi2, True, 'density', r'$\tau$', 0.7, 0.7,
              _dpi=600)
columName ='flow'
hist.histPlot(path + '/' + columName, d2, columName, countOfIntervalsXi2, True, r'f($\gamma$)', r'$\gamma$', 0.7, 0.7,
              _dpi=600)

d3 = densityValue(d2['flow'].values, d2['flow'].min(), d2['flow'].max(), countOfIntervalsXi2)

densityParameters= {"lawDensity" : "norm"
    , "min" : d2['flow'].min()
    , "max" : d2['flow'].max()
    , "countOfIntervalsXi2" : countOfIntervalsXi2
    , "average" : 0.0, "std" : 1.0}
d3normal = densityExpectedValue(d3, densityParameters)
# ================================================ check ============================================
path = 'figures/' + fileName + '/check'
file_util.make_dir_if_not(path)
x = d3[0]
y1 = d3[1]
y2 = d3normal[1]
columName ='flow_density'
xlabelName = r'$\gamma$'
lineChart.linePlot(path + '/' + columName, x, y1, y1, xlabelName, r'f($\gamma$)'
# lineChart.linePlot(path + '/' + columName, x, y1, y2, xlabelName, r'f($\gamma$)'
         , 0.7, _dpi=600
         , xMin=min(x), xMax=max(x)
         , y1Min=min(y1), y1Max=max(y1), _fontsize=10)

columName ='flow_frequency_hist'
lineHistChart.lineHistPlot(path + '/' + columName, x
             , y2
             , d2['flow']
             , countOfIntervalsXi2
             , xlabelName, r'f($\gamma$)'
             , 0.7, _dpi=600
             , xMin=min(x), xMax=max(x)
             , y1Min=min(y1), y1Max=max(y1), _fontsize=8)

frequencyParameters = {"delta": (d2['flow'].max() - d2['flow'].min()) / countOfIntervalsXi2,
                       "numberExamples": numberExamples}
d31 = frequencyValue(d3, frequencyParameters)
d31normal = frequencyValue(d3normal, frequencyParameters)
columName ='flow_frequency'
xlabelName = r'$\gamma$'
lineChart.linePlot(path + '/' + columName, d31[0], d31[1], d31[1], xlabelName, r'Frequency of the value '+xlabelName
                   # lineChart.linePlot(path + '/' + columName, d31[0], d31[1], d31normal[1], xlabelName,
                   # r'Frequency of the value '+xlabelName
         , 0.7, _dpi=600
         , xMin=min(d31[0]), xMax=max( d31[0])
         , y1Min=min(d31[1]), y1Max=max(d31[1]), _fontsize=8)

d4=[d31[1], d31normal[1]]
kf = chi2_contingency(d4)
print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)
# ================================================ autoKorelationCoeffitient ===========================================
d_auto_korelation_centered_mass=copy.copy(d2)
# !!!!!! is transformed the dimensionless flow into a centered dimensionless flow with an average constant in time
d_auto_korelation_centered_mass['flow']=(d2['flow']) - d2['flow'].mean()
period = 200   #  The variable [period] is introduced to reduce calculations.
# The variable specifies that only the point for which the ratio is valid [i % period == 0] is calculated for the plot.

#===============================================================================
if (experiment["show_prepare_k"] == True):
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
period = 200   #  The variable [period] is introduced to reduce calculations.
# The variable specifies that only the point for which the ratio is valid [i % period == 0] is calculated for the plot.

#===============================================================================
# if (experiment["show_prepare_k"] == True):
extentions.c0_show_k0(fileName, d_auto_korelation_centered_mass2, period)
extentions.c0_show_1_v(fileName, d_auto_korelation_centered_mass2, period)
extentions.c0_show_work_equals_0_5(fileName, d_auto_korelation_centered_mass2, period)
extentions.c0_show_test_equals_0_5(fileName, d_auto_korelation_centered_mass2, period)
extentions.c0_show_var2(experiment, d_auto_korelation_centered_mass2)
extentions.c0_show_tau_tau_minus_v_tau_plus_v(experiment, d_auto_korelation_centered_mass2)



sys.exit()
