import datetime
import matplotlib.pyplot as plt
import numpy as np

def histPlot(fileName
             , df
             , columName
             , countOfIntervalsXi2
             , _density # This parameter is an optional parameter and it contains the boolean values.
             , ylabelName
             , xlabelName
             , _alpha # яркость столбцов диаграммы
             , _rwidth
             ,  _color = 'black'  # the column color of the diagram
             , _dpi = 1000
             ):
    plt.close('all')
    x = datetime.datetime.now()
    syffix=x.strftime("%Y_%m_%d_%H_%M_%S")
    columData = df[columName]
    delta = ( max(columData) - min(columData) ) / countOfIntervalsXi2
    bins = np.arange(min(columData), max(columData) , delta) # This parameter is an optional parameter and it contains the integer or sequence or string.

    plt.grid(True, color =_color, alpha = _alpha/2)      #

    #    plt.hist(x, 5, density=True, facecolor='g', alpha=0.75)
    plt.hist(columData, bins = countOfIntervalsXi2, bottom=False, density = _density, alpha = _alpha, color =_color, histtype='bar', align='mid'
             , rwidth = 0.8)
    # plt.rcParams['text.usetex'] = True
    # plt.ylabel(ylabelName, fontsize=10)
    plt.xlabel(xlabelName, fontsize=10, loc='right')

    plt.xlim(min(columData), max(columData))    # set xMin, xMax
    #   plt.xticks(np.linspace(min(columData), max(columData), 5))           # set xMin, xMax, number of ticket

    plt.xticks(fontsize=10)
    plt.ylim(0)                                 # set yMin, yMax
    # plt.yticks(np.linspace(0, 0.0006, 11))
    plt.yticks(fontsize=10)

    plt.rcParams["figure.figsize"] = [4.0, 3.0]   # size of the figure 3.0*2.54 ~ 7.5 cm
    plt.tight_layout( pad =1.5)           # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax

    # https://scipy-lectures.org/intro/matplotlib/index.html
    # https://www.math.uci.edu/~xiangwen/pdf/LaTeX-Math-Symbols.pdf


    plt.title(ylabelName
              # , fontweight ="bold"
              , fontsize=10, loc='left' )

    #   plt.text(60, .025, r'$\mu=100,\ \sigma=15$')

    plt.savefig(fileName + syffix+"_"+str(countOfIntervalsXi2)+".jpeg", dpi=_dpi)
    #plt.interactive(True)
    plt.show()


def histPlot2(fileName
             , y_values
             , countOfIntervalsXi2
             , _density # This parameter is an optional parameter and it contains the boolean values.
             , _alpha # яркость столбцов диаграммы
             , _rwidth
              , ylabel_name
              , xlabel_name
              , fontsize
              , _x_size_plot
              , _y_size_plot
             ,  _color = 'black'  # the column color of the diagram
             , _dpi = 1000
              , _adjust_left=0.12
              , _adjust_right=0.98
              , _adjust_top=0.92
              , _adjust_bottom=0.17
             ):
    plt.close('all')
    fig, axis = plt.subplots()
    x = datetime.datetime.now()
    syffix=x.strftime("%Y_%m_%d_%H_%M_%S")
    columData = y_values[0]
    delta = ( max(columData) - min(columData) ) / countOfIntervalsXi2
    bins = np.arange(min(columData), max(columData) , delta) # This parameter is an optional parameter and it contains the integer or sequence or string.

    plt.grid(True, color =_color, alpha = _alpha/2)      #

    #    plt.hist(x, 5, density=True, facecolor='g', alpha=0.75)
    plt.hist(columData, bins = countOfIntervalsXi2, bottom=False, density = _density, alpha = _alpha, color =_color, histtype='bar', align='mid'
             , rwidth = 0.8)
    # plt.rcParams['text.usetex'] = True
    # plt.ylabel(ylabelName, fontsize=10)
    plt.xlabel(xlabel_name, fontsize=fontsize, loc='right')

    plt.xlim(min(columData), max(columData))    # set xMin, xMax
    #   plt.xticks(np.linspace(min(columData), max(columData), 5))           # set xMin, xMax, number of ticket

    plt.xticks(fontsize=fontsize)
    plt.ylim(0)                                 # set yMin, yMax
    # plt.yticks(np.linspace(0, 0.0006, 11))
    plt.yticks(fontsize=fontsize)

    plt.tight_layout( pad =1.5)           # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0      # offset of the axes from the origin, given by xMin, xMax, yMin, yMax

    # https://scipy-lectures.org/intro/matplotlib/index.html
    # https://www.math.uci.edu/~xiangwen/pdf/LaTeX-Math-Symbols.pdf


    plt.title(ylabel_name
              # , fontweight ="bold"
              , fontsize=fontsize, loc='left' )

    #   plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    fig.set_figwidth(mm_to_inch(_x_size_plot))
    fig.set_figheight(mm_to_inch(_y_size_plot))
    # Reduce the plot border
    plt.subplots_adjust(left=_adjust_left, right=_adjust_right, top=_adjust_top, bottom=_adjust_bottom)
    plt.savefig(fileName + syffix+"_"+str(countOfIntervalsXi2)+".jpeg", dpi=_dpi)
    #plt.interactive(True)
    plt.show()



def mm_to_inch(mm_value):
    """
    The function converts mm to inches.
    :param mm_value: size in mm.
    :return: size in inches.
    """
    return mm_value / 25.4