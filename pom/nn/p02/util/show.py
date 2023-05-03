"""
Visual dataset.
"""
import math

import pom.stochastic03.Graphics.LineCharts.LineChart as lineChart
import pom.stochastic03.Graphics.CombinedCharts.LineHistChart as lineHistChart
import pom.stochastic03.utils.FileUtil as file_util
import pom.stochastic03.StatUtils.stat_func as stat_func

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

def output_flow(
        experiment
        , sub_directory_name
        , plot_values
        , file_name_prefix
):
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    :param sub_directory_name: the name of the directory where the visualization data is located.
    :param plot_values: set of plot-values sequence.
    :param file_name_prefix: file name prefix.
    :param xlabel_name: x-axis label.
    :param ylabel_name: y-axis label.
    """
    path = RESULT_DATA + experiment["file_name"] + sub_directory_name
    file_util.make_dir_if_not(path)

    x_values = plot_values[0]
    y_values = visual_lines(plot_values, experiment, "output_flow")

    plot = experiment["plot_parameters"]["output_flow"]
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
                         , x_min=95
                         , x_max=100
                         , x_tick_main =plot["x_tick_main"]
                         , x_tick_auxiliary =plot["x_tick_auxiliary"]
                         , x_axis_order =plot["x_axis_order"]
                         , y1_min=min(y_values[0])
                         , y1_max= 5 # max(y_values[0])
                         , y_tick_main =plot["y_tick_main"]
                         , y_tick_auxiliary =plot["y_tick_auxiliary"]
                         , _fontsize=plot["fontsize"]
                         , _x_size_plot=plot["x_size_plot"]
                         , _y_size_plot=plot["y_size_plot"]
                         , _plot_line_width =plot["plot_line_width"]
                         , _grid_line_width =plot["grid_line_width"]
                         )

def loss(
        experiment
        , sub_directory_name
        , plot_values
        , file_name_prefix
):
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    :param sub_directory_name: the name of the directory where the visualization data is located.
    :param plot_values: set of plot-values sequence.
    :param file_name_prefix: file name prefix.
    :param xlabel_name: x-axis label.
    :param ylabel_name: y-axis label.
    """
    path = RESULT_DATA + experiment["file_name"] + sub_directory_name
    file_util.make_dir_if_not(path)
    plot_name = "loss"

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
                         , x_min=0
                         , x_max= experiment["learning"]["count_epochs"]
                            # math.log10(experiment["learning"]["count_epochs"])
                         , x_tick_main =plot["x_tick_main"]
                         , x_tick_auxiliary =plot["x_tick_auxiliary"]
                         , x_axis_order =plot["x_axis_order"]
                         , y1_min= 0 # min(y_values[0])
                         , y1_max= 0.5 # max(y_values[0])
                         , y_tick_main =plot["y_tick_main"]
                         , y_tick_auxiliary =plot["y_tick_auxiliary"]
                         , _fontsize=plot["fontsize"]
                         , _x_size_plot=plot["x_size_plot"]
                         , _y_size_plot=plot["y_size_plot"]
                         , _plot_line_width =plot["plot_line_width"]
                         , _grid_line_width =plot["grid_line_width"]
                         )
