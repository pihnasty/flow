import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] =20_000

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


def linePlot(fileName
             , x
             , y1
             , y2
             , xlabelName
             , title
             , _alpha  # яркость столбцов диаграммы
             , _color1='black'  # the column color of the diagram
             , _color2='black'  # the column color of the diagram
             , _dpi=1000
             , xMin=0.0
             , xMax=0.0
             , y1Min=0.0
             , y1Max=0.0
             , _fontsize=10
             ):
    plt.close('all')

    dateS = datetime.datetime.now()
    syffix = dateS.strftime("%Y_%m_%d_%H_%M_%S")
    plt.grid(True, color=_color1, alpha=_alpha / 2)  #
    plt.rcParams["figure.figsize"] = [4.0,
                                      3.0]  # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    plt.xlabel(xlabelName, fontsize=_fontsize, loc='right')
    plt.xlim(min(x), max(x))  # set xMin, xMax
    plt.xlim(min(y1), max(y1))  # set yMin, yMax
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
    plt.tight_layout(pad=1.5)  # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left')

    plt.savefig(fileName + syffix + ".jpeg", dpi=_dpi)
    plt.show()
    plt.close()


def linePlot2(fileName
              , x
              , ys
              , xlabelName
              , title
              , _alpha  # яркость столбцов диаграммы
              , _color='black'  # the column color of the diagram
              , _dpi=1000
              , xMin=0.0
              , xMax=0.0
              , y1Min=0.0
              , y1Max=0.0
              , _fontsize=10
              ):
    plt.close('all')

    date_s = datetime.datetime.now()
    syffix = date_s.strftime("%Y_%m_%d_%H_%M_%S")
    plt.figure(figsize=(7.90/2.54, 6.00/2.54))
    # plt.rcParams["figure.figsize"] = [4.0, 3.0]
    #plt.rcParams["figure.figsize"] = [7.90/2.54, 6.00/2.54]
    # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    # plt.grid(True, color=_color, alpha=_alpha / 2)
    plt.grid(True, color=_color, alpha=_alpha)
    plt.xlabel(xlabelName, fontsize=_fontsize, loc='right')
    plt.xlim(min(x), max(x))  # set xMin, xMax
    plt.ylim(min(ys[0]), max(ys[0]))  # set yMin, yMax
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
    plt.tight_layout(pad=1.5)  # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left')
    # Reduce the plot border
    plt.subplots_adjust(left=0.1, right=0.97, top=0.92, bottom=0.17)
    plt.savefig(fileName + syffix + ".jpeg", dpi=_dpi)
    plt.show()


def line_plot3(file_name
               , x_values
               , ys_values
               , xlabel_name
               , title
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
    :param _adjust_bottom: Float value representing the bottom's position
    of the subplots as a fraction of the figure height.
    :param _adjust_top: Float value representing the top's position
    of the subplots as a fraction of the figure height.
    :param _adjust_right:Float value representing the right side's
    position of the subplots as a fraction of the figure width.
    :param _adjust_left:Float value representing the left side's position
    of the subplots as a fraction of the figure width.
    """
    plt.close('all')
    dates = datetime.datetime.now()
    syffix = dates.strftime("%Y_%m_%d_%H_%M_%S")

    # ==================================================================================================================
    # https://pyprog.pro/mpl/mpl_axis_ticks.html
    # https://www.inp.nsk.su/~grozin/python/python6.html
    # https://proproprogs.ru/modules/matplotlib-funkciya-plot-dlya-postroeniya-i-oformleniya-dvumernyh-grafikov
    # https://newtechaudit.ru/vizualizacziya-v-python-matplotlib/    #убираем рамку справа
    fig, axis = plt.subplots()
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    for y_values in ys_values:
        axis.plot(x_values, y_values, 'k', alpha=_alpha_main, lw=_plot_line_width)
    if x_tick_auxiliary > 0:  # Set the interval of the auxiliary ticks:
        axis.xaxis.set_minor_locator(ticker.MultipleLocator(x_tick_auxiliary))
    if y_tick_auxiliary > 0:
        axis.yaxis.set_minor_locator(ticker.MultipleLocator(y_tick_auxiliary))
    #  Set the interval of the main ticks:
    if x_tick_main > 0:
        axis.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_main))
    if y_tick_main > 0:
        axis.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_main))
    # ==================================================================================================================
    plt.grid(True, color=_color, alpha=_alpha_grid, lw=_grid_line_width)
    plt.xlabel(xlabel_name, fontsize=_fontsize, loc='right')
    plt.xlim(min(x_values), max(x_values))  # set xMin, xMax
    plt.ylim(min(ys_values[0]), max(ys_values[0]))  # set yMin, yMax

    plt.xticks(fontsize=_fontsize)
    plt.ylim(0)
    if x_max > 0.0:
        plt.xlim(x_min, x_max)
    if y1_max > 0.0:
        plt.ylim(y1_min, y1_max)
    # plt.yticks(np.linspace(0, 0.0006, 11))
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout(pad=3.0)  # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left')
    if x_axis_order == "back":
        plt.gca().invert_xaxis()
    fig.set_figwidth(mm_to_inch(_x_size_plot))
    fig.set_figheight(mm_to_inch(_y_size_plot))
    # Reduce the plot border
    plt.subplots_adjust(left=_adjust_left, right=_adjust_right, top=_adjust_top, bottom=_adjust_bottom)
    plt.savefig(file_name + syffix + ".jpeg", dpi=_dpi)
    plt.show()


def line_plot4(file_name
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

    # ==================================================================================================================
    # https://pyprog.pro/mpl/mpl_axis_ticks.html
    # https://www.inp.nsk.su/~grozin/python/python6.html
    # https://proproprogs.ru/modules/matplotlib-funkciya-plot-dlya-postroeniya-i-oformleniya-dvumernyh-grafikov
    # https://newtechaudit.ru/vizualizacziya-v-python-matplotlib/    #убираем рамку справа
    fig, axis = plt.subplots()
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    i = 1
    for y_values in ys_values:
        color = _y_colors[i]
        i = i + 1
        axis.plot(x_values, y_values, color, alpha=_alpha_main, lw=_plot_line_width)
    if x_tick_auxiliary > 0:  # Set the interval of the auxiliary ticks:
        axis.xaxis.set_minor_locator(ticker.MultipleLocator(x_tick_auxiliary))
    if y_tick_auxiliary > 0:
        axis.yaxis.set_minor_locator(ticker.MultipleLocator(y_tick_auxiliary))
    #  Set the interval of the main ticks:
    if x_tick_main > 0:
        axis.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_main))
    if y_tick_main > 0:
        axis.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_main))
    # ==================================================================================================================
    plt.grid(True, color=_color, alpha=_alpha_grid, lw=_grid_line_width)
    plt.xlabel(xlabel_name, fontsize=_fontsize, loc='right')
    plt.xlim(min(x_values), max(x_values))  # set xMin, xMax
    plt.ylim(min(ys_values[0]), max(ys_values[0]))  # set yMin, yMax

    plt.xticks(fontsize=_fontsize)
    plt.ylim(0)
    if x_max > 0.0:
        plt.xlim(x_min, x_max)
    if y1_max > 0.0:
        plt.ylim(y1_min, y1_max)
    # plt.yticks(np.linspace(0, 0.0006, 11))
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout(pad=3.0)  # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left')
    if x_axis_order == "back":
        plt.gca().invert_xaxis()
    fig.set_figwidth(mm_to_inch(_x_size_plot))
    fig.set_figheight(mm_to_inch(_y_size_plot))
    # Reduce the plot border
    plt.subplots_adjust(left=_adjust_left, right=_adjust_right, top=_adjust_top, bottom=_adjust_bottom)
    plt.savefig(file_name + syffix + ".jpeg", dpi=_dpi)
    plt.show()

def bar_plot4(fileName
              , x
              , ys
              , xlabel_name
              , title
              , _alpha_main  # яркость столбцов диаграммы
              , _color='black'  # the column color of the diagram
              , _dpi=1000
              , x_min=0.0
              , x_max=0.0
              , y1_min=0.0
              , y1_max=0.0
              , _fontsize=10
              , _adjust_left=0.12
              , _adjust_right=0.98
              , _adjust_top=0.92
              , _adjust_bottom=0.17
              ):
    plt.close('all')
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html
    date_s = datetime.datetime.now()
    syffix = date_s.strftime("%Y_%m_%d_%H_%M_%S")
    plt.figure(figsize=(7.90/2.54, 6.00/2.54))
    # plt.rcParams["figure.figsize"] = [4.0, 3.0]
    #plt.rcParams["figure.figsize"] = [7.90/2.54, 6.00/2.54]
    # size of the figure 3.0*2.54 ~ 7.5 cm     # plt.figure(figsize=(12, 7))
    # plt.grid(True, color=_color, alpha=_alpha / 2)
    plt.grid(True, color='black', alpha=_alpha_main)
    plt.xlabel(xlabel_name, fontsize=_fontsize, loc='right')
    plt.xlim(min(x), max(x))  # set xMin, xMax
    plt.ylim(min(ys[0]), max(ys[0]))  # set yMin, yMax
    # https://devpractice.ru/matplotlib-lesson-4-1-viz-linear-chart/
    for y in ys:
        plt.bar(x, y, alpha=_alpha_main, lw=2, color=_color, width = 0.75)
    plt.xticks(fontsize=_fontsize)
    plt.ylim(0)
    if x_max > 0.0:
        plt.xlim(x_min, x_max)
    if y1_max > 0.0:
        plt.ylim(y1_min, y1_max)
    plt.yticks(fontsize=_fontsize)
    plt.tight_layout(pad=1.5)  # tight_layout() can take keyword arguments of pad, w_pad and h_pad
    plt.rcParams['axes.xmargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.rcParams['axes.ymargin'] = 0  # offset of the axes from the origin, given by xMin, xMax, yMin, yMax
    plt.title(title
              # , fontweight ="bold"
              , fontsize=_fontsize, loc='left')
    # Reduce the plot border
    plt.subplots_adjust(left=_adjust_left, right=_adjust_right, top=_adjust_top, bottom=_adjust_bottom)
    plt.savefig(fileName + syffix + ".jpeg", dpi=_dpi)
    plt.show()

