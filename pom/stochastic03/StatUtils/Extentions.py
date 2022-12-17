import math
import pom.stochastic03.Graphics.LineCharts.LineChart as lineChart
import pom.stochastic03.utils.FileUtil as fileUtil
from pom.stochastic03.utils.progress import progress
import numpy as np

def c_1(tau):
    return 1.0 / (tau * (1.0 - math.exp(-1.0 / tau)))

def c1_plot(fileName, fontsize):
    N = 1000
    tau_correlation_max = 5.0
    dtau_correlation = tau_correlation_max / N
    c1 = [0] * N
    tau = [0] * N
    c1_tau = [tau , c1 ]
    for i in range(N):
        if i > 0:
            c1_tau [0] [i] = i * dtau_correlation
            c1_tau [1] [i] = c_1(c1_tau [0] [i])

    path = 'figures/' + fileName + '/common'
    fileUtil.make_dir_if_not(path)
    columName ='flow_c1_tau'

    lineChart.linePlot(path + '/' + columName
                       , c1_tau[0]
                       , c1_tau[1]
                       , c1_tau[1]
                       , r'$\tau_{cor}$'
                       , r'$C_1(\tau_{cor})$'
                       , 0.7
                       , _dpi=600
                       , xMin=0.0
                       , xMax=tau_correlation_max
                       , y1Min=1.0
                       , y1Max=5.0
                       , _fontsize=fontsize)

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

# ======================================================================================================================
def c0_1_v(tau
       , dataX
       , dataY
       ):
    _tMin = min(dataX)
    _tMax = max(dataX)
    numberExamples = len(dataX)
    delta_t = (_tMax - _tMin) / numberExamples
    tauI = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(dataY):
        if (i < numberExamples - tauI):
            iTauI = (i + tauI) % numberExamples
            integral = integral + dataY[i] * dataY[iTauI] * delta_t
        else:
            integral = integral
    return integral

# ======================================================================================================================
def c0_work_equals_0_5(tau
           , dataX
           , dataY
           ):
    _tMin = min(dataX)
    _tMax = max(dataX)
    numberExamples = len(dataX)
    delta_t = (_tMax - _tMin) / numberExamples
    tauI = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(dataY):
        if (i < numberExamples / 2  - 1):
            iTauI = (i + tauI)
            integral = integral + dataY[i] * dataY[iTauI] * delta_t
        else:
            integral = integral
    return integral

# ======================================================================================================================
def c0_test_equals_0_5(tau
                       , dataX
                       , dataY
                       ):
    _tMin = min(dataX)
    _tMax = max(dataX)
    numberExamples = len(dataX)
    delta_t = (_tMax - _tMin) / numberExamples
    tauI = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(dataY):
        if (i > numberExamples / 2  + 1):
            iTauI = (i - tauI)
            integral = integral + dataY[i] * dataY[iTauI] * delta_t
        else:
            integral = integral
    return integral

# ========================================= c0_show_k0 =================================================================
def c0_show_k0(fileName
                , d_auto_korelation_centered_mass
                , period
                ):
    count = len(d_auto_korelation_centered_mass["time"])
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient = [d2X, d2Y, d2Y2]
    i=0
    j=0

    d_auto_korelation_centered_mass_stdColumn=d_auto_korelation_centered_mass["flow"].std()**2
    _tMax = d_auto_korelation_centered_mass['time'].max()
    for tau in d_auto_korelation_centered_mass["time"]:
        if(i % period == 0 and j< autoKorelationCoeffitient[0].__len__()):
            try:
                autoKorelationCoeffitient[2][j] = np.exp(-0.1 * tau)
                autoKorelationCoeffitient[1][j] = k(tau
                                                    , d_auto_korelation_centered_mass["time"]
                                                    , d_auto_korelation_centered_mass["flow"]) \
                                                  / d_auto_korelation_centered_mass_stdColumn / _tMax
                autoKorelationCoeffitient[0][j] = tau
                j=j+1
                progress(i+1, len(d_auto_korelation_centered_mass["time"]))
            except IndexError:
                print("IndexError")
        i=i+1

    progress(len(d_auto_korelation_centered_mass["time"]), len(d_auto_korelation_centered_mass["time"]))

    path = 'figures/' + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName ='flow_autoKorelation'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient[1], autoKorelationCoeffitient[1], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , xMax = d_auto_korelation_centered_mass['time'].max()
                       , y1Min= min(autoKorelationCoeffitient[1]), y1Max= max(autoKorelationCoeffitient[1]), _fontsize=8)




#===================================== c0_show_1_v =============================================================================
def c0_show_1_v(fileName
       , d_auto_korelation_centered_mass
       , period
       ):
    count = len(d_auto_korelation_centered_mass["time"])
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient_C0 = [d2X, d2Y, d2Y2]
    d_auto_korelation_centered_mass_stdColumn=d_auto_korelation_centered_mass["flow"].std()**2
    _tMax = max(d_auto_korelation_centered_mass["time"])
    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0 and j < len(autoKorelationCoeffitient_C0[0])):
            try:
                autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / 0.07)
                autoKorelationCoeffitient_C0[1][j] = c0_1_v(tau, d_auto_korelation_centered_mass["time"],
                                                                   d_auto_korelation_centered_mass[
                                                                       "flow"]) / d_auto_korelation_centered_mass_stdColumn /  ( _tMax - tau )
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
                progress(i + 1, len(d_auto_korelation_centered_mass["time"]))
            except IndexError:
                print("")
        i = i + 1

    path = 'figures/' + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_1_v_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0[1], autoKorelationCoeffitient_C0[2], xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=2.0
                       # , y1Min= -1.5
                       , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)

#===================================== c0_show_work_equals_0_5 =========================================================
def c0_show_work_equals_0_5(fileName
            , d_auto_korelation_centered_mass
            , period
            ):

    count = len(d_auto_korelation_centered_mass["time"])
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient_C0 = [d2X, d2Y, d2Y2]
    d_auto_korelation_centered_mass_stdColumn = d_auto_korelation_centered_mass["flow"].std() ** 2
    _tMax = max(d_auto_korelation_centered_mass["time"])
    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0 ):
            if ( j < len(autoKorelationCoeffitient_C0[0]) / 2 ):
                try:
                    autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / 0.07)
                    autoKorelationCoeffitient_C0[1][j] = c0_work_equals_0_5(tau, d_auto_korelation_centered_mass["time"],
                                                                            d_auto_korelation_centered_mass[
                                                                                "flow"]) / (
                                                                     d_auto_korelation_centered_mass_stdColumn ) # * _tMax
                    autoKorelationCoeffitient_C0[0][j] = tau
                    j = j + 1
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]) / 2)
                except IndexError:
                    print("")
            else:
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
        i = i + 1

    path = 'figures/' + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_work_equals_0_5_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0[1], autoKorelationCoeffitient_C0[2], xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=2.0
                       , y1Min= -1.0
                       # , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)


#===================================== c0_show_work_equals_0_5 =========================================================
def c0_show_test_equals_0_5(fileName
                            , d_auto_korelation_centered_mass
                            , period
                            ):

    count = len(d_auto_korelation_centered_mass["time"])
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient_C0 = [d2X, d2Y, d2Y2]
    d_auto_korelation_centered_mass_stdColumn = d_auto_korelation_centered_mass["flow"].std() ** 2
    _tMax = max(d_auto_korelation_centered_mass["time"])
    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0 ):
            if ( j < len(autoKorelationCoeffitient_C0[0]) / 2 ):
                try:
                    autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / 0.07)
                    autoKorelationCoeffitient_C0[1][j] = c0_test_equals_0_5(tau, d_auto_korelation_centered_mass["time"],
                                                                            d_auto_korelation_centered_mass[
                                                                                "flow"]) / (
                                                             d_auto_korelation_centered_mass_stdColumn ) # * _tMax
                    autoKorelationCoeffitient_C0[0][j] = tau
                    j = j + 1
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]) / 2)
                except IndexError:
                    print("")
            else:
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
        i = i + 1

    path = 'figures/' + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_test_equals_0_5_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0[1], autoKorelationCoeffitient_C0[2], xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=2.0
                       # , y1Min= -0.5
                       , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)
