# ba01.csv Kawalec W, Król R.: Generating of Electric Energy by a Declined Overburden Conveyor in a Continuous Surface Mine. Energies 14, 1–13 (2021). https://doi.org/10.3390/en14134030

import copy
import math
import sys

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

import Graphics.CombinedCharts.LineHistChart as lineHistChart
import Graphics.Histograms.Hist as hist
import Graphics.LineCharts.LineChart as lineChart
import utils.FileUtil as file_util
from utils.progress import progress

# df = pd.read_csv('netflix_titles.csv', sep=",")
# df = pd.read_csv('ba01.csv', sep=";" , decimal=',')
# numberExamples = 11591

# universal .csv
df = pd.read_csv('dataset.csv', sep=";", decimal=',')
numberExamples = df.shape[0]
# KaKr
# df = pd.read_csv('datasetKaKr.csv', sep=";" , decimal=',')
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
        if(value[1] < intervalValue):
            yValue[indexIndex] +=1/elementSize/delta
        else:
            indexIndex+=1
            if(indexIndex < len(xValue)):
                intervalValue = intervalValue + delta
                xValue[indexIndex] = intervalValue
    returnValue = [xValue, yValue]
    return returnValue

def densityExpectedValue(initialData, densityParameters):
    expectedData = copy.deepcopy(initialData)
    if(densityParameters["lawDensity"]=="norm"):
        for i, val in enumerate(expectedData[0]):
            value = (expectedData[0][i]-densityParameters["average"])/densityParameters["std"]
            expectedData[1][i] = (1.0/densityParameters["std"]/(2.0*math.pi)**(0.5))*math.exp(-0.5*value**2)

    delta = (densityParameters["max"]-densityParameters["min"])/densityParameters["countOfIntervalsXi2"]

    pSum = sum(expectedData[1])*delta

    for i, val in enumerate(expectedData[1]):
        expectedData[1][i] = expectedData[1][i]/pSum

    return expectedData

def frequencyValue(data, frecuencyParameters):
    frecuencyData = copy.deepcopy(data)
    for i, val in enumerate(frecuencyData[0]):
        frecuencyData[1][i] = data[1][i] * frecuencyParameters["delta"] * frecuencyParameters["numberExamples"]
    return frecuencyData

def k(tau # interval between the sections
      , dataX
      , dataY
      ):
    _tMin = min(dataX)
    _tMax = max(dataX)
    numberExamples = len(dataX)
    delta_t = (_tMax - _tMin) / numberExamples
    tauI = round(tau/delta_t)
    integral = 0
    for i, val in enumerate(dataY):
        iTauI = (i+tauI) % numberExamples
        integral = integral + dataY[i]*dataY[iTauI]*delta_t
    return integral


# ================================================ initial =================================================
path = 'figures/initial'
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
d2['time']=(df['time']-tMin)/(tMax-tMin)
# ============================================= initial_dimensionless ======================================
path = 'figures/initial_dimensionless'
file_util.make_dir_if_not(path)
columName ='flow_line'
xlabelName = r'$\tau$'
lineChart.linePlot(path + '/' + columName, d2['time'].values
         , d2['flow'].values, d2['flow'].values, xlabelName, r'$\gamma(\tau)$'
         , 0.7, _dpi=600
         , xMin = d2['time'].min(), xMax = d2['time'].max()
         , y1Min= d2['flow'].min(), y1Max= d2['flow'].max(), _fontsize=8)
columName ='time'
hist.histPlot(path + '/' + columName, d2, columName, countOfIntervalsXi2, True, 'density', r'$\tau$'         , 0.7, 0.7, _dpi=600)
columName ='flow'
hist.histPlot(path + '/' + columName, d2, columName, countOfIntervalsXi2, True, r'f($\gamma$)',r'$\gamma$', 0.7, 0.7, _dpi=600)

d3 = densityValue(d2['flow'].values, d2['flow'].min(), d2['flow'].max(), countOfIntervalsXi2)

densityParameters= {"lawDensity" : "norm"
    , "min" : d2['flow'].min()
    , "max" : d2['flow'].max()
    , "countOfIntervalsXi2" : countOfIntervalsXi2
    , "average" : 0.0, "std" : 1.0}
d3normal = densityExpectedValue(d3, densityParameters)
# ================================================ check ============================================
path = 'figures/check'
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

frequencyParameters= {"delta" : (d2['flow'].max()-d2['flow'].min())/countOfIntervalsXi2, "numberExamples" : numberExamples}
d31 = frequencyValue(d3, frequencyParameters)
d31normal = frequencyValue(d3normal, frequencyParameters)
columName ='flow_frequency'
xlabelName = r'$\gamma$'
lineChart.linePlot(path + '/' + columName, d31[0], d31[1], d31[1], xlabelName, r'Frequency of the value '+xlabelName
# lineChart.linePlot(path + '/' + columName, d31[0], d31[1], d31normal[1], xlabelName, r'Frequency of the value '+xlabelName
         , 0.7, _dpi=600
         , xMin=min(d31[0]), xMax=max( d31[0])
         , y1Min=min(d31[1]), y1Max=max(d31[1]), _fontsize=8)

d4=[d31[1], d31normal[1]]
kf = chi2_contingency(d4)
print('chisq-statistic=%.4f, p-value=%.4f, df=%i expected_frep=%s'%kf)
# ================================================ autoKorelationCoeffitient ============================================
d_auto_korelation_centered_mass=copy.copy(d2)
d_auto_korelation_centered_mass['flow']=(d2['flow']) - d2['flow'].mean() # !!!!!! is transformed the dimensionless flow into a centered dimensionless flow with an average constant in time
period = 200   #  The variable [period] is introduced to reduce calculations.
# The variable specifies that only the point for which the ratio is valid [i % period == 0] is calculated for the plot.
d2X=[0] * round(numberExamples/period)
d2Y=[0] * round(numberExamples/period)
d2Y2=[0] * round(numberExamples/period)
autoKorelationCoeffitient = [d2X, d2Y, d2Y2]
i=0
j=0

d_auto_korelation_centered_mass_stdColumn=d_auto_korelation_centered_mass["flow"].std()**2

for tau in d_auto_korelation_centered_mass["time"]:
    if(i % period == 0 and j< autoKorelationCoeffitient[0].__len__()):
        try:
            autoKorelationCoeffitient[2][j] = np.exp(-0.1*tau)
            autoKorelationCoeffitient[1][j] = k(tau, d_auto_korelation_centered_mass["time"],d_auto_korelation_centered_mass["flow"])/d_auto_korelation_centered_mass_stdColumn
            autoKorelationCoeffitient[0][j] = tau
            j=j+1
            progress(i+1, numberExamples)
        except IndexError:
            print("")
    i=i+1

path = 'figures/autoCorelation'
file_util.make_dir_if_not(path)
columName ='flow_autoKorelation'
xlabelName = r'$\vartheta$'
lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient[0]
         # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
         , autoKorelationCoeffitient[1], autoKorelationCoeffitient[1], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
         , xMax = 0.5, y1Min= min(autoKorelationCoeffitient[1]), y1Max= max(autoKorelationCoeffitient[1]), _fontsize=8)

sys.exit()


