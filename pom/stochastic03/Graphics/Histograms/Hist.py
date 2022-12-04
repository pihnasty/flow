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
