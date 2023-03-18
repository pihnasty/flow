import datetime
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

def linePlot(fileName
             , x
             , y1
             , y2
             , xlabelName
             , title
             , _alpha # яркость столбцов диаграммы
             , _color1 = 'black'  # the column color of the diagram
             , _color2 = 'black'  # the column color of the diagram
             , _dpi=1000
             , xMin=0.0
             , xMax=0.0
             , y1Min=0.0
             , y1Max=0.0
             , _fontsize=10
             ):
    plt.close('all')

    dateS = datetime.datetime.now()
    syffix=dateS.strftime("%Y_%m_%d_%H_%M_%S")
    plt.grid(True, color =_color1, alpha = _alpha/2)      #
    plt.rcParams["figure.figsize"] = [4.0, 3.0]   # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    plt.xlabel(xlabelName, fontsize=_fontsize, loc='right')
    plt.xlim(min(x), max(x))    # set xMin, xMax
    plt.xlim(min(y1), max(y1))    # set yMin, yMax
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    plt.plot(x, y1, 'k', alpha=0.7, lw=2, color=_color1)
    plt.plot(x, y2, 'k', alpha=0.7, lw=2, color=_color2)
    plt.xticks(fontsize=_fontsize)
    plt.ylim(0)

    if (xMax > 0.0):
        plt.xlim(xMin, xMax)
    if (y1Max > 0.0):
        plt.ylim(y1Min, y1Max)
    # plt.yticks(np.linspace(0, 0.0006, 11))
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout( pad =1.5)           # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left' )



    plt.savefig(fileName + syffix + ".jpeg", dpi=_dpi)
    plt.show()
    plt.close()

def linePlot2(fileName
             , x
             , ys
             , xlabelName
             , title
             , _alpha # яркость столбцов диаграммы
             , _color = 'black'  # the column color of the diagram
             , _dpi=1000
             , xMin=0.0
             , xMax=0.0
             , y1Min=0.0
             , y1Max=0.0
             , _fontsize=10
             ):
    plt.close('all')

    dateS = datetime.datetime.now()
    syffix=dateS.strftime("%Y_%m_%d_%H_%M_%S")
    plt.grid(True, color =_color, alpha = _alpha/2)      #
    plt.rcParams["figure.figsize"] = [4.0, 3.0]   # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    plt.xlabel(xlabelName, fontsize=_fontsize, loc='right')
    plt.xlim(min(x), max(x))    # set xMin, xMax
    plt.ylim(min(ys[0]), max(ys[0]))    # set yMin, yMax
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    for y in ys:
        plt.plot(x, y, 'k', alpha=0.7, lw=2)
    plt.xticks(fontsize=_fontsize)
    plt.ylim(0)
    if xMax > 0.0:
        plt.xlim(xMin, xMax)
    if y1Max > 0.0:
        plt.ylim(y1Min, y1Max)
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout( pad =1.5)           # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left' )



    plt.savefig(fileName + syffix + ".jpeg", dpi=_dpi)
    plt.show()

def line_plot3(file_name
                  , x_values
                  , ys_values
                  , xlabel_name
                  , title
                  , _alpha # яркость столбцов диаграммы
                  , _color = 'black'  # the column color of the diagram
                  , _dpi=1000
                  , x_min=0.0
                  , x_max=0.0
                  , x_tick_main = 0.0
                  , x_tick_auxiliary = 0.0
                  , y1_min=0.0
                  , y1_max=0.0
                  , y_tick_main = 0.0
                  , y_tick_auxiliary = 0.0
                  , _fontsize=10
 ):
    """
    Line plot visualization.
    :param file_name: full name of the file to save the plot.
    :param x_values: set of x sequence.
    :param ys_values: set of ys sequence.
    :param xlabel_name: x-axis label.
    :param title: y-axis label.
    :param _alpha: brightness of chart bars.
    :param _color: the column color of the diagram.
    :param _dpi: dpi for figure.
    :param x_min: x min.
    :param x_max: x max.
    :param x_tick_main: number of main ticks along the axis x.
    :param x_tick_auxiliary: number of auxiliary ticks along the axis x.
    :param y1_min: y1 min.
    :param y1_max: y1 max.
    :param y_tick_main: number of main ticks along the axis y.
    :param y_tick_auxiliary: number of auxiliary ticks along the axis y.
    :param _fontsize: fontsize for axis.
    """
    plt.close('all')

    dates = datetime.datetime.now()
    syffix=dates.strftime("%Y_%m_%d_%H_%M_%S")

    # ==================================================================================================================
    # https://pyprog.pro/mpl/mpl_axis_ticks.html
    fig, axis = plt.subplots()
    if x_tick_auxiliary > 0:     #  Set the interval of the auxiliary ticks:
        axis.xaxis.set_minor_locator(ticker.MultipleLocator(x_tick_auxiliary))
    if y_tick_auxiliary > 0:
        axis.yaxis.set_minor_locator(ticker.MultipleLocator(y_tick_auxiliary))
    #  Set the interval of the main ticks:
    if x_tick_main > 0:
        axis.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_main))
    if y_tick_main > 0:
        axis.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_main))
# ======================================================================================================================
    plt.grid(True, color =_color, alpha = _alpha/2)
    plt.rcParams["figure.figsize"] = [4.0, 3.0] # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    plt.xlabel(xlabel_name, fontsize=_fontsize, loc='right')
    plt.xlim(min(x_values), max(x_values))    # set xMin, xMax
    plt.ylim(min(ys_values[0]), max(ys_values[0]))    # set yMin, yMax
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    for y_values in ys_values:
        plt.plot(x_values, y_values, 'k', alpha=0.7, lw=2)
    plt.xticks(fontsize=_fontsize)
    plt.ylim(0)
    if x_max > 0.0:
        plt.xlim(x_min, x_max)
    if y1_max > 0.0:
        plt.ylim(y1_min, y1_max)
    # plt.yticks(np.linspace(0, 0.0006, 11))
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout( pad =1.5)           # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left' )
    plt.savefig(file_name + syffix + ".jpeg", dpi=_dpi)
    plt.show()
