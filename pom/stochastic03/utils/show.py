"""
Visual dataset.
"""
import math

import pom.stochastic03.Graphics.LineCharts.LineChart as lineChart
import pom.stochastic03.Graphics.Histograms.Hist as hist
import pom.stochastic03.utils.FileUtil as file_util

RESULT_DATA = 'resultData/'
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
    ]

def common_line(
        experiment
        , path
        , plot_values
        , file_name_prefix
        , plot_name
):
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    :param path: the name of the directory where the visualization data is located.
    :param plot_values: set of plot-values sequence.
    :param file_name_prefix: file name prefix.
    :param plot_name: the plot name with parameters.
    """

    file_util.make_dir_if_not(path)

    x_values = plot_values[0]
    y_values = visual_lines(plot_values, experiment, plot_name)

    plot = experiment["plot_parameters"][plot_name]
    lineChart.line_plot4(path + '/' + file_name_prefix
                         , x_values
                         , y_values
                         , xlabel_name=plot["x_label_name"]
                         , title=plot["y_label_name"]
                         , _y_colors = plot["color_line_set"]
                         , _alpha_main=plot["alpha_main"]
                         , _alpha_grid=plot["alpha_grid"]
                         , _color=plot["color"]
                         , _dpi=experiment["plot_parameters"]["dpi"]
                         , x_min=plot["x_min"]
                         , x_max=plot["x_max"]
                         , x_tick_main =plot["x_tick_main"]
                         , x_tick_auxiliary =plot["x_tick_auxiliary"]
                         , x_axis_order =plot["x_axis_order"]
                         , y1_min= plot["y_min"]
                         , y1_max= plot["y_max"]
                         , y_tick_main =plot["y_tick_main"]
                         , y_tick_auxiliary =plot["y_tick_auxiliary"]
                         , _fontsize=plot["fontsize"]
                         , _x_size_plot=plot["x_size_plot"]
                         , _y_size_plot=plot["y_size_plot"]
                         , _plot_line_width =plot["plot_line_width"]
                         , _grid_line_width =plot["grid_line_width"]
                         , _adjust_left=plot["border_adjustment"]["left"]
                         , _adjust_right=plot["border_adjustment"]["right"]
                         , _adjust_top=plot["border_adjustment"]["top"]
                         , _adjust_bottom=plot["border_adjustment"]["bottom"]
                         )

def common_hist(
        experiment
        , path
        , plot_values
        , file_name_prefix
        , plot_name
):
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    :param path: the name of the directory where the visualization data is located.
    :param plot_values: set of plot-values sequence.
    :param file_name_prefix: file name prefix.
    :param plot_name: the plot name with parameters.
    """

    file_util.make_dir_if_not(path)

    x_values = plot_values[0]
    y_values = visual_lines(plot_values, experiment, plot_name)

    plot = experiment["plot_parameters"][plot_name]
    count_of_intervals_xi2 = plot["count_of_intervals_xi2"]

    # column_name = 'time'
    # hist.histPlot(path + '/' + column_name, df, column_name, count_of_intervals_xi2, True, 'density', r'$t$', 0.7, 0.7,
    #               _dpi=600)

    hist.histPlot2(path + '/' + file_name_prefix
                   , y_values
                   , count_of_intervals_xi2
                   , True
                   , _alpha=plot["alpha"]
                   , _rwidth=plot["rwidth"]
                   , ylabel_name=plot["y_label_name"]
                   , xlabel_name=plot["x_label_name"]
                   , fontsize=plot["fontsize"]
                   , _x_size_plot=plot["x_size_plot"]
                   , _y_size_plot=plot["y_size_plot"]
                   , _dpi=experiment["plot_parameters"]["dpi"]
                   , _adjust_left=plot["border_adjustment"]["left"]
                   , _adjust_right=plot["border_adjustment"]["right"]
                   , _adjust_top=plot["border_adjustment"]["top"]
                   , _adjust_bottom=plot["border_adjustment"]["bottom"]
                   )
