import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] =20_000
import numpy as np
import statsmodels.api as sm
import pylab as plt

def visual_lines(lines, experiment, plot_name):
    """
    Visualization of lines depending on the design of the experiment.
    :param lines: y-values.
    :param experiment: experiment conditions.
    :param plot_name: plot name.
    :return: visualization options.
    """
    return [
        lines[experiment["plot_parameters"][plot_name]["visual_line_set"]["1"]]
        , lines[experiment["plot_parameters"][plot_name]["visual_line_set"]["2"]]
        , lines[experiment["plot_parameters"][plot_name]["visual_line_set"]["3"]]
        , lines[experiment["plot_parameters"][plot_name]["visual_line_set"]["4"]]
        , lines[experiment["plot_parameters"][plot_name]["visual_line_set"]["5"]]
        # , lines[experiment["plot_parameters"][plot_name]["visual_line_set"]["7"]]

    ]


def mm_to_inch(mm_value):
    """
    The function converts mm to inches.
    :param mm_value: size in mm.
    :return: size in inches.
    """
    return mm_value / 25.4

def q_q_plot(file_name
               , x_values
               , ys_values
               , xlabel_name
               , title
               , _y_colors={'0': 'k', '1': 'k', '2': 'k', '3': 'k', '4': 'k', '5': 'k'}
               , _alpha_main=1.0  # яркость plot
               , _alpha_grid=0.5  # яркость grid
               , _color='black'  # the column color of the diagram
               , _dpi=1000
               , x_min=0.0
               , x_max=0.0
               , x_tick_main=0.0
               , x_tick_auxiliary=0.0
               , x_axis_order="forward"  # "back"
               , y1_min=0.0
               , y1_max=0.0
               , y_tick_main=0.0
               , y_tick_auxiliary=0.0
               , _fontsize=10
               , _x_size_plot=100
               , _y_size_plot=75
               , _plot_line_width=2
               , _grid_line_width=1.5
               , _adjust_left=0.12
               , _adjust_right=0.98
               , _adjust_top=0.92
               , _adjust_bottom=0.17
               ):
    """
    Line plot visualization.
    :param file_name: full name of the file to save the plot.
    :param x_values: set of x sequence.
    :param ys_values: set of ys sequence.
    :param xlabel_name: x-axis label.
    :param title: y-axis label.
    :param _alpha_main: brightness of chart bars.
    :param _alpha_grid: brightness of grid bars.
    :param _color: the column color of the diagram.
    :param _dpi: dpi for figure.
    :param x_min: x min.
    :param x_max: x max.
    :param x_tick_main: number of main ticks along the axis x.
    :param x_tick_auxiliary: number of auxiliary ticks along the axis x.
    :param x_axis_order: forward - 1,2,3,4,5; back - 5,4,3,2,1.
    :param y1_min: y1 min.
    :param y1_max: y1 max.
    :param y_tick_main: number of main ticks along the axis y.
    :param y_tick_auxiliary: number of auxiliary ticks along the axis y.
    :param _fontsize: fontsize for axis.
    :param _x_size_plot: x size of plot.
    :param _y_size_plot: y size of plot.
    :param _plot_line_width: plot line width.
    :param _grid_line_width: grid line width.
    """
    plt.close('all')
    dates = datetime.datetime.now()
    syffix = dates.strftime("%Y_%m_%d_%H_%M_%S")
    plt.figure(figsize=(7.90/2.54, 6.00/2.54))
    # ==================================================================================================================
    # https://pyprog.pro/mpl/mpl_axis_ticks.html
    # https://www.inp.nsk.su/~grozin/python/python6.html
    # https://proproprogs.ru/modules/matplotlib-funkciya-plot-dlya-postroeniya-i-oformleniya-dvumernyh-grafikov
    # https://newtechaudit.ru/vizualizacziya-v-python-matplotlib/    #убираем рамку справа
    fig, axis = plt.subplots()
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    i = 1

    # sm.qqplot(ys_values[1], line='45')

    pp = sm.ProbPlot(ys_values[1], fit=True)
    qq = pp.qqplot(marker='.', markerfacecolor=_y_colors[1], markeredgecolor=_y_colors[1], alpha=0.3)
    sm.qqline(qq.axes[0], line='45', fmt='k--')


    plt.xlim(x_min, x_max)
    plt.ylim(y1_min, y1_max)

    # ==================================================================================================================
    plt.grid(True, color='black', alpha=_alpha_main)
    plt.xlabel(xlabel_name, fontsize=_fontsize, loc='right')
    plt.ylabel(title, fontsize=_fontsize, loc='top')
    # plt.title(title
    #           # , fontweight ="bold"
    #           , fontsize=_fontsize, loc='left')

    plt.xticks(fontsize=_fontsize)
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout(pad=1.5)  # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax

    # Reduce the plot border
    plt.subplots_adjust(left=_adjust_left, right=_adjust_right, top=_adjust_top, bottom=_adjust_bottom)
    plt.savefig(file_name + syffix + ".jpeg", dpi=_dpi)
    plt.show()
