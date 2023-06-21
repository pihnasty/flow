import datetime
from matplotlib import pyplot as plt

def linePlotHist(fileName
                 , x
                 , y1
                 , y2
                 , countOfIntervalsXi2
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
                 , _density = True
                 ):
    plt.close('all')

    dateS = datetime.datetime.now()
    syffix=dateS.strftime("%Y_%m_%d_%H_%M_%S")
    #plt.rcParams["figure.figsize"] = [4.0, 3.0]   # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    plt.figure(figsize=(7.90/2.54, 6.00/2.54))
    #plt.grid(True, color =_color, alpha = _alpha/2)      #
    plt.grid(True, color =_color, alpha = _alpha)      #
    plt.xlabel(xlabelName, fontsize=_fontsize, loc='right')
    plt.xlim(min(x), max(x))    # set xMin, xMax
    plt.xlim(min(y1), max(y1))    # set xMin, xMax
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    # plt.plot(x, y1, 'k', alpha=0.7, lw=2)
    plt.plot(x, y1, 'k', alpha=1, lw=2)
    # plt.hist(y2, 5, density=True, facecolor='g', alpha=0.75)
    plt.hist(y2, bins = countOfIntervalsXi2, bottom=False, density = _density, alpha = _alpha,  histtype='bar', align='mid', color =_color
             , rwidth = 0.8)
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
    # Reduce the plot border
    plt.subplots_adjust(left=0.1, right=0.97, top=0.92, bottom=0.17)
    plt.savefig(fileName + syffix+"_"+str(countOfIntervalsXi2)+".jpeg", dpi=_dpi)
    plt.show()



