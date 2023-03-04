import math
import pom.stochastic03.Graphics.LineCharts.LineChart as lineChart
import pom.stochastic03.utils.FileUtil as fileUtil
from pom.stochastic03.utils.progress import progress
import numpy as np

RESULT_DATA = 'resultData/'

def prediction_std(period
                   , correlation_time
                   , d_auto_korelation_centered_mass
                   ):
    count = len(d_auto_korelation_centered_mass["time"])
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient_C0 = [d2X, d2Y, d2Y2]
    d_auto_korelation_centered_mass_stdColumn = d_auto_korelation_centered_mass["flow"].std() ** 2

    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0):
            if (j < len(autoKorelationCoeffitient_C0[0])):
                try:
                    autoKorelationCoeffitient_C0[1][j] \
                        = c0_var2(tau, d_auto_korelation_centered_mass["time"], d_auto_korelation_centered_mass["flow"])
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]))
                except IndexError:
                    print("")
            autoKorelationCoeffitient_C0[0][j] = tau
            j = j + 1
        i = i + 1
    integral = 0.0
    count = len(autoKorelationCoeffitient_C0[0]) - 1
    delta_t = (max(autoKorelationCoeffitient_C0[0]) - min(autoKorelationCoeffitient_C0[0])) / count
    for i in range(len(autoKorelationCoeffitient_C0[0])-1):
        integral = integral + autoKorelationCoeffitient_C0[1][i] * delta_t
    progress(len(d_auto_korelation_centered_mass["time"]), len(d_auto_korelation_centered_mass["time"]))
    return (integral - 1) * c_1(correlation_time)

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

    path = RESULT_DATA + fileName + '/common'
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


def k(tau
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
        iTauI = (i + tauI) % numberExamples
        integral = integral + dataY[i] * dataY[iTauI] * delta_t
    return integral / (_tMax - _tMin)


def c0_1_v(tau
           , dataX
           , dataY
           ):
    """
    This function calculates the dimensionless correlation coefficient k(tau) for the interval (tau_max-tau)
    Parameters
    ----------
        tau :  float
            dimensionless parameter of the correlation function.
        dataX : array_like
            array of dimensionless time parameters of a random process.
        dataY : array_like
            array of dimensionless values of the stochastic process.
    Returns
    -------
    k: float
        the dimensionless correlation coefficient k(tau).
    """
    _tMin = min(dataX)
    _tMax = max(dataX)
    numberExamples = len(dataX)
    delta_t = (_tMax - _tMin) / numberExamples
    tauI = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(dataY):
        if (i < numberExamples - tauI):
            iTauI = (i + tauI)
            integral = integral + dataY[i] * dataY[iTauI] * delta_t
    return integral / (_tMax - tau - _tMin)

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
        if (i < numberExamples / 2  - 1 and tauI < numberExamples / 2  - 1):
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


def c0_var2(tau
            , data_x
            , data_y
            ):
    """
    This function calculates the dimensionless correlation coefficient k(tau) for the interval (tau_max-tau_min)
    Parameters
    ----------
        tau :  float
            dimensionless parameter of the correlation function.
        data_x : array_like
            array of dimensionless time parameters of a random process.
        data_y : array_like
            array of dimensionless values of the stochastic process.
    Returns
    -------
    k: float
        the dimensionless correlation coefficient k(tau).
    """
    _tMin = min(data_x)
    _tMax = max(data_x)
    number_examples = len(data_x)
    delta_t = (_tMax - _tMin) / number_examples
    tau_i = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(data_y):
        i_tau_i = (i - tau_i)
        if (i_tau_i < 0):
            i_tau_i = i + tau_i
        if (i_tau_i < number_examples):
            integral = integral + data_y[i] * data_y[i_tau_i] * delta_t
    return integral / (_tMax - _tMin)


def c0_tau_tau_minus_v_tau_plus_v(tau
                                  , data_x
                                  , data_y
                                  ):
    """
    This function calculates the dimensionless correlation coefficient k(tau) for the interval (tau_max-tau_min)
    integral = integral + data_y[i] * (data_y[i_tau_i_minus] + data_y[i_tau_i_plus]) * delta_t
    Parameters
    ----------
        tau :  float
            dimensionless parameter of the correlation function.
        data_x : array_like
            array of dimensionless time parameters of a random process.
        data_y : array_like
            array of dimensionless values of the stochastic process.
    Returns
    -------
    k: float
        the dimensionless correlation coefficient k(tau).
    """
    _tMin = min(data_x)
    _tMax = max(data_x)
    number_examples = len(data_x)
    delta_t = (_tMax - _tMin) / number_examples
    tau_i = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(data_y):
        i_tau_i_minus = (i - tau_i)
        i_tau_i_plus = (i + tau_i)

        if (i_tau_i_minus < 0):
            i_tau_i_minus = i + tau_i

        if (i_tau_i_plus > number_examples -1):
            i_tau_i_plus = i - tau_i

        if (i_tau_i_plus > 0 and i_tau_i_minus < number_examples):
            integral = integral + data_y[i] * (data_y[i_tau_i_minus] + data_y[i_tau_i_plus]) / 2 * delta_t
    return integral / (_tMax - _tMin)


def c0_tau_tau_minus_v_tau_plus_v_tau_plus_1(tau
                                  , data_x
                                  , data_y
                                  ):
    """
    This function calculates the dimensionless correlation coefficient k(tau) for the interval (tau_max-tau_min)
    integral = integral + data_y[i] * (data_y[i_tau_i_minus] + data_y[i_tau_i_plus]) * delta_t
    Parameters
    ----------
        tau :  float
            dimensionless parameter of the correlation function.
        data_x : array_like
            array of dimensionless time parameters of a random process.
        data_y : array_like
            array of dimensionless values of the stochastic process.
    Returns
    -------
    k: float
        the dimensionless correlation coefficient k(tau).
    """
    _tMin = min(data_x)
    _tMax = max(data_x)
    number_examples = len(data_x)
    delta_t = (_tMax - _tMin) / number_examples
    tau_i = round(tau / delta_t)
    integral = 0
    for i, val in enumerate(data_y):
        i_tau_i_minus = (i - tau_i)
        i_tau_i_plus = (i + tau_i)

        if (i_tau_i_minus < 0):
            i_tau_i_minus = i + tau_i

        if (i_tau_i_plus > number_examples - 1):
            i_tau_i_plus = i - tau_i

        if (i_tau_i_plus >= 0 and i_tau_i_minus < number_examples):
            integral = integral + data_y[i] * (data_y[i_tau_i_minus] + data_y[i_tau_i_plus]) / 2 * delta_t
        else:
            integral = integral + data_y[i] * (
                    data_y[i_tau_i_minus % number_examples] + data_y[i_tau_i_plus % number_examples]
            ) / 2 * delta_t
    return integral / (_tMax - _tMin)






def c0_tau_tau_minus_v_tau_plus_v_s(
        period
        , dimensionless_flow
):
    count = len(dimensionless_flow["time"])
    d2X_c0_tau_tau_minus_v_tau_plus_v = [0] * round(count / period)
    d2Y_c0_tau_tau_minus_v_tau_plus_v = [0] * round(count / period)
    c0_tau_tau_minus_v_tau_plus_vs = [d2X_c0_tau_tau_minus_v_tau_plus_v, d2Y_c0_tau_tau_minus_v_tau_plus_v]

    i = 0
    j = 0
    for tau in dimensionless_flow["time"]:
        if (i % period == 0 and j < len(c0_tau_tau_minus_v_tau_plus_vs[0])):
            try:
                c0_tau_tau_minus_v_tau_plus_vs[1][j] = c0_tau_tau_minus_v_tau_plus_v( # c0_work_equals_0_5( #c0_1_v( #k( #c0_var2( #
                    tau
                    , dimensionless_flow["time"]
                    , dimensionless_flow["flow"]
                )
                c0_tau_tau_minus_v_tau_plus_vs[0][j] = tau
                j = j + 1
                progress(i + 1, count)
            except IndexError:
                print("")
        i = i + 1
    return c0_tau_tau_minus_v_tau_plus_vs


def c0_tau_tau_minus_v_tau_plus_v_tau_plus_1_s(
        period
        , dimensionless_flow
):
    count = len(dimensionless_flow["time"])
    d2X_c0_tau_tau_minus_v_tau_plus_v = [0] * round(count / period)
    d2Y_c0_tau_tau_minus_v_tau_plus_v = [0] * round(count / period)
    c0_tau_tau_minus_v_tau_plus_vs = [d2X_c0_tau_tau_minus_v_tau_plus_v, d2Y_c0_tau_tau_minus_v_tau_plus_v]

    i = 0
    j = 0
    for tau in dimensionless_flow["time"]:
        if (i % period == 0 and j < len(c0_tau_tau_minus_v_tau_plus_vs[0])):
            try:
                c0_tau_tau_minus_v_tau_plus_vs[1][j] = c0_tau_tau_minus_v_tau_plus_v_tau_plus_1( # c0_work_equals_0_5( #c0_1_v( #k( #c0_var2( #
                    tau
                    , dimensionless_flow["time"]
                    , dimensionless_flow["flow"]
                )
                c0_tau_tau_minus_v_tau_plus_vs[0][j] = tau
                j = j + 1
                progress(i + 1, count)
            except IndexError:
                print("")
        i = i + 1
    return c0_tau_tau_minus_v_tau_plus_vs
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
                                                  / d_auto_korelation_centered_mass_stdColumn
                autoKorelationCoeffitient[0][j] = tau
                j=j+1
                progress(i+1, len(d_auto_korelation_centered_mass["time"]))
            except IndexError:
                print("IndexError")
        i=i+1

    progress(len(d_auto_korelation_centered_mass["time"]),
             len(d_auto_korelation_centered_mass["time"]), '\n')

    path = RESULT_DATA + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName ='flow_autoKorelation_k0_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient[1], autoKorelationCoeffitient[1], xlabelName, r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=1.0 # d_auto_korelation_centered_mass['time'].max()
                       , y1Min=min(autoKorelationCoeffitient[1]), y1Max=max(autoKorelationCoeffitient[1]), _fontsize=8)




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
    d_auto_korelation_centered_mass_stdColumn = d_auto_korelation_centered_mass["flow"].std() ** 2
    _tMax = max(d_auto_korelation_centered_mass["time"])
    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0 and j < len(autoKorelationCoeffitient_C0[0])):
            try:
                autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / 0.07)
                autoKorelationCoeffitient_C0[1][j] = c0_1_v(tau, d_auto_korelation_centered_mass["time"],
                                                            d_auto_korelation_centered_mass[
                                                                "flow"]) / d_auto_korelation_centered_mass_stdColumn
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
                progress(i + 1, len(d_auto_korelation_centered_mass["time"]))
            except IndexError:
                print("")
        i = i + 1

    progress(len(d_auto_korelation_centered_mass["time"]),
             len(d_auto_korelation_centered_mass["time"]), '\n')

    path = RESULT_DATA + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_1_v_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0[1], autoKorelationCoeffitient_C0[1], xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=1.0
                       , y1Min=-0.5
                       # , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)

#===================================== c0_show_work_equals_0_05 ========================================================
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
        if (i % period == 0):
            if (j < len(autoKorelationCoeffitient_C0[0]) / 2):
                try:
                    autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / 0.07)
                    autoKorelationCoeffitient_C0[1][j] = c0_work_equals_0_5(
                        tau
                        , d_auto_korelation_centered_mass["time"]
                        , d_auto_korelation_centered_mass["flow"]
                    ) / (d_auto_korelation_centered_mass_stdColumn)  # * _tMax
                    autoKorelationCoeffitient_C0[0][j] = tau
                    j = j + 1
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]) / 2)
                except IndexError:
                    print("")
            else:
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
        i = i + 1

    progress(len(d_auto_korelation_centered_mass["time"]) / 2,
             len(d_auto_korelation_centered_mass["time"]) / 2, '\n')

    path = RESULT_DATA + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_work_equals_0_05_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0[1], autoKorelationCoeffitient_C0[1], xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=1.0
                       # , y1Min= -1.0
                       , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)


#===================================== c0_show_work_equals_05_1_ =======================================================
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
                                                             d_auto_korelation_centered_mass_stdColumn )
                    autoKorelationCoeffitient_C0[0][j] = tau
                    j = j + 1
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]) / 2)
                except IndexError:
                    print("")
            else:
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
        i = i + 1

    progress(len(d_auto_korelation_centered_mass["time"]) / 2,
             len(d_auto_korelation_centered_mass["time"]) / 2, '\n')

    path = RESULT_DATA + fileName + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_test_equals_05_1_'
    xlabelName = r'$\vartheta$'
    lineChart.linePlot(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0[1], autoKorelationCoeffitient_C0[1], xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=1.0
                       # , y1Min= -0.5
                       , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)


# ===================================== c0_show_var2=====================================================================
def c0_show_var2(experiment
                 , d_auto_korelation_centered_mass
                 ):
    count = len(d_auto_korelation_centered_mass["time"])
    period = experiment["period"]
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient_C0 = [d2X, d2Y, d2Y2]
    d_auto_korelation_centered_mass_stdColumn = d_auto_korelation_centered_mass["flow"].std() ** 2
    _tMax = max(d_auto_korelation_centered_mass["time"])
    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0):
            if (j < len(autoKorelationCoeffitient_C0[0])):
                try:
                    autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / experiment["tau_correlation"])
                    autoKorelationCoeffitient_C0[1][j] = c0_var2(tau, d_auto_korelation_centered_mass["time"],
                                                                 d_auto_korelation_centered_mass[
                                                                     "flow"]) / (
                                                             d_auto_korelation_centered_mass_stdColumn)
                    autoKorelationCoeffitient_C0[0][j] = tau
                    j = j + 1
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]))
                except IndexError:
                    print("")
            else:
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
        i = i + 1

    progress(len(d_auto_korelation_centered_mass["time"]), len(d_auto_korelation_centered_mass["time"]), '\n')

    path = RESULT_DATA + experiment["file_name"] + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_var2'
    xlabelName = r'$\vartheta$'
    autoKorelationCoeffitient_C0s = [
        autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["1"]]
        , autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["2"]]
        , autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["3"]]
        , autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["4"]]
        , autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["5"]]
    ]
    lineChart.linePlot2(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                       # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                       , autoKorelationCoeffitient_C0s
                       , xlabelName,
                       r'k($\vartheta$) ',
                       0.7, _dpi=600
                       , xMax=1.0
                       , y1Min=-0.5
                       # , y1Min=min(autoKorelationCoeffitient_C0[1])
                       , y1Max=max(autoKorelationCoeffitient_C0[1]),
                       _fontsize=8)


# ===================================== c0_show_tau_tau_minus_v_tau_plus_v =============================================
def c0_show_tau_tau_minus_v_tau_plus_v(experiment
                 , d_auto_korelation_centered_mass
                 ):
    count = len(d_auto_korelation_centered_mass["time"])
    period = experiment["period"]
    d2X = [0] * round(count / period)
    d2Y = [0] * round(count / period)
    d2Y2 = [0] * round(count / period)
    autoKorelationCoeffitient_C0 = [d2X, d2Y, d2Y2]
    d_auto_korelation_centered_mass_stdColumn = d_auto_korelation_centered_mass["flow"].std() ** 2
    _tMax = max(d_auto_korelation_centered_mass["time"])
    i = 0
    j = 0
    for tau in d_auto_korelation_centered_mass["time"]:
        if (i % period == 0):
            if (j < len(autoKorelationCoeffitient_C0[0])):
                try:
                    autoKorelationCoeffitient_C0[2][j] = np.exp(-tau / experiment["tau_correlation"])
                    autoKorelationCoeffitient_C0[1][j] = c0_tau_tau_minus_v_tau_plus_v(
                        tau
                        , d_auto_korelation_centered_mass["time"]
                        , d_auto_korelation_centered_mass["flow"]) / (
                                                             d_auto_korelation_centered_mass_stdColumn)
                    autoKorelationCoeffitient_C0[0][j] = tau
                    j = j + 1
                    progress(i + 1, len(d_auto_korelation_centered_mass["time"]))
                except IndexError:
                    print("")
            else:
                autoKorelationCoeffitient_C0[0][j] = tau
                j = j + 1
        i = i + 1

    progress(len(d_auto_korelation_centered_mass["time"]), len(d_auto_korelation_centered_mass["time"]), '\n')

    path = RESULT_DATA + experiment["file_name"] + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_tau_tau_minus_v_tau_plus_v'
    xlabelName = r'$\vartheta$'
    autoKorelationCoeffitient_C0s = [
        autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["1"]]
        , autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["2"]]
        , autoKorelationCoeffitient_C0[experiment["c0_show_var2"]["3"]]
    ]
    lineChart.linePlot2(path + '/' + columName, autoKorelationCoeffitient_C0[0]
                        # , autoKorelationCoeffitient[1], autoKorelationCoeffitient[2], xlabelName, r'k($\vartheta$) ', 0.7, _dpi=600
                        , autoKorelationCoeffitient_C0s
                        , xlabelName,
                        r'k($\vartheta$) ',
                        0.7, _dpi=600
                        , xMax=1.0
                        , y1Min=-0.5
                        # , y1Min=min(autoKorelationCoeffitient_C0[1])
                        , y1Max=max(autoKorelationCoeffitient_C0[1]),
                        _fontsize=8)


# =======================================================================================================================
def c0_show_tau_tau_minus_v_tau_plus_v2(experiment
                                        , x
                                        , y
                                        ):
    path = RESULT_DATA + experiment["file_name"] + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_tau_tau_minus_v_tau_plus_v2_'
    xlabelName = r'$\vartheta$'
    autoKorelationCoeffitient_C0s = [y]
    lineChart.linePlot2(
        path + '/' + columName
        , x
        , autoKorelationCoeffitient_C0s
        , xlabelName
        , r'$С_0(\vartheta)$ '
        , 0.7
        , _dpi=600
        , xMax=1.0
        , y1Min=-0.5
        , y1Max=max(y),
        _fontsize=8
    )


def c0_show_tau_tau_minus_v_tau_plus_v_tau_plus_1(experiment
                                                  , x
                                                  , y
                                                  ):
    path = RESULT_DATA + experiment["file_name"] + '/autoCorelation'
    fileUtil.make_dir_if_not(path)
    columName = 'flow_autoKorelation_C0_tau_tau_minus_v_tau_plus_v2'
    xlabelName = r'$\tau$'
    autoKorelationCoeffitient_C0s = [y]
    lineChart.linePlot2(path + '/' + columName, x
                        , autoKorelationCoeffitient_C0s
                        , xlabelName,
                        r'C($\tau$) '
                        , 0.7
                        , _dpi=600
                        , xMax=1.0
                        , y1Min=-0.5  # , y1Min=min(autoKorelationCoeffitient_C0[1])
                        , y1Max=max(y),
                        _fontsize=8)

def approximated_gamma_show(experiment
                            , dimensionless_flow
                            , approximated_gamma
                            , columName
                            , title
                 ):
    path = RESULT_DATA + experiment["file_name"] + '/approximatedGamma'
    fileUtil.make_dir_if_not(path)
    xlabelName = r'$\tau$'

    lineChart.linePlot(path + '/' + columName
                       , dimensionless_flow["time"]
                       , dimensionless_flow["flow"]
                       , approximated_gamma
                       , xlabelName, title
                       # lineChart.linePlot(path + '/' + columName, x, y1, y2, xlabelName, r'f($\gamma$)'
                       , 0.7, _dpi=600
                       , _color2 = "black"
                       , xMin=min(dimensionless_flow["time"]), xMax=max(dimensionless_flow["time"])
                       , y1Min=limit_min_value(min(dimensionless_flow["flow"]),0)
                       , y1Max=max(dimensionless_flow["flow"]), _fontsize=10)

def approximated_gamma_s_show(experiment
                            , dimensionless_flow
                            , approximated_gamma
                            , columName
                            , title
                            ):
    path = RESULT_DATA + experiment["file_name"] + '/approximatedGamma'
    fileUtil.make_dir_if_not(path)
    xlabelName = r'$\tau$'
    approximated_gamma_s = [
        approximated_gamma["flow"]
    ]

    lineChart.linePlot2(path + '/' + columName
                        , approximated_gamma["time"]
                        , approximated_gamma_s
                        , xlabelName, title
                        , 0.7
                        , _dpi=600
                        , xMin=min(approximated_gamma["time"]), xMax=max(approximated_gamma["time"])
                        , y1Min=min(approximated_gamma["flow"]), y1Max=max(approximated_gamma["flow"])
                        , _fontsize=8)

def fourier_coefficients(period
                         , dimensionless_flow
                         , n  # harmonic number
                         ):
    count = len(dimensionless_flow["time"]) - 1
    delta_tau = (max(dimensionless_flow["time"]) - min(dimensionless_flow["time"])) / count
    integral = 0.0
    for i in range(count):
        tau = dimensionless_flow["time"][i]
        integral = integral + dimensionless_flow["flow"][i] * math.cos(math.pi * n * tau) * delta_tau
        if (i % period == 0):
            progress(i, count)
    progress(count, count)
    return 2 * integral


def fourier_coefficients_d(period
                           , tau_correlation
                           , std
                           , relative_sigma_correlation
                           , c0_tau_tau_minus_v_tau_plus_vs
                           , fourier_coefficients_gamma
                           , n  # harmonic number
                           ):
    count = len(c0_tau_tau_minus_v_tau_plus_vs[0]) - 1
    delta_tau = (max(c0_tau_tau_minus_v_tau_plus_vs[0]) - min(c0_tau_tau_minus_v_tau_plus_vs[0])) / count
    integral = 0.0
    for i in range(count):
        tau = c0_tau_tau_minus_v_tau_plus_vs[0][i]
        integral = integral + (
                (std * relative_sigma_correlation) ** 2 * math.exp(-tau / tau_correlation)
                - c0_tau_tau_minus_v_tau_plus_vs[1][i]
        ) * math.cos(math.pi * n * tau) * delta_tau

        if (i % period == 0):
            progress(i, count)
    progress(count, count)

    discriminant = 4 * fourier_coefficients_gamma[n] ** 2 + 4 * 4 * integral

    print([
        'n=', n, "   discriminant", discriminant
        , "   fourier_coefficients_gamma[n]", fourier_coefficients_gamma[n]
    ])

    if (discriminant < 0):
        discriminant = 0

    value = 0
    if (fourier_coefficients_gamma[n] > 0):
        value = (2 * fourier_coefficients_gamma[n] - math.sqrt(discriminant)) / 2
    else:
        value  = (2 * fourier_coefficients_gamma[n] + math.sqrt(discriminant)) / 2
    return value

def approximated_gamma(period
                       , fourier_coefficients
                       , dimensionless_flow
                       ):
    coefficients_number = len(fourier_coefficients)
    count = len(dimensionless_flow["time"])

    approximated_gamma_function = [0] * count
    for i in range(count):
        tau = dimensionless_flow["time"][i]
        value = 0.0
        for n in range(coefficients_number):
            if (n == 0):
                value = fourier_coefficients[n] / 2
            else:
                value = value + fourier_coefficients[n] * math.cos(math.pi * n * tau)
            approximated_gamma_function[i] = value
            if (i % period == 0):
                progress(i, count)
        progress(count, count)
    return approximated_gamma_function

def approximated_gamma_d(period
                       , fourier_coefficients
                       , dimensionless_flow
                       ):
    coefficients_number = len(fourier_coefficients)
    count = len(dimensionless_flow["time"])

    approximated_gamma_function = [0] * count
    for i in range(count):
        tau = dimensionless_flow["time"][i]
        value = 0.0
        for n in range(coefficients_number):
            if (n == 0):
                value = fourier_coefficients[n] / 2
            else:
                value = value + fourier_coefficients[n] * math.cos(math.pi * n * tau)
            approximated_gamma_function[i] = value
            if (i % period == 0):
                progress(i, count)
        progress(count, count)
    return approximated_gamma_function


def limit_min_value(value_1, value_2):
    """
    Method returns the minimum value of two numbers.
    :param value_1: first value.
    :param value_2: second value.
    :return: the minimum value of two numbers.
    """
    value = value_1
    if (value_2 < value):
        value = value_2
    return value
