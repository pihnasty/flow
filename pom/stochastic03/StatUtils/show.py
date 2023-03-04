"""
Visual dataset.
"""
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

def flow_density(
        experiment
        , sub_directory_name
        , flow_densities
        , file_name_prefix
        , xlabel_name
        , ylabel_name
        , alpha
):
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    :param sub_directory_name: the name of the directory where the visualization data is located.
    :param flow_densities: set of random variable sequence.
    :param file_name_prefix: file name prefix.
    :param xlabel_name: x-axis label.
    :param ylabel_name: y-axis label.
    :param alpha: chart bar brightness.
    """
    path = RESULT_DATA + experiment["file_name"] + sub_directory_name
    file_util.make_dir_if_not(path)
    xvalues = flow_densities[0]
    yvalues = visual_lines(flow_densities, experiment, "show_flow_density")
    lineChart.linePlot2(path + '/' + file_name_prefix
                        , xvalues
                        , yvalues
                        , xlabel_name
                        , ylabel_name
                        , alpha
                        , _color='black'
                        , _dpi=experiment["plot_parameters"]["dpi"]
                        , xMin=min(xvalues)
                        , xMax=max(xvalues)
                        , y1Min=min(yvalues[0])
                        , y1Max=max(yvalues[0])
                        , _fontsize=experiment["plot_parameters"]["show_flow_density"]["fontsize"]
                        )

def frequency_plot_hist(
        experiment
        , sub_directory_name
        , x_values
        , plot_values
        , hist_values
        , file_name_prefix
        , xlabel_name
        , ylabel_name
        , alpha
):
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    :param sub_directory_name: the name of the directory where the visualization data is located.
    :param x_values: set of x-variable sequence.
    :param plot_values: set of plot-values sequence.
    :param hist_values: set of hist-values sequence.
    :param file_name_prefix: file name prefix.
    :param xlabel_name: x-axis label.
    :param ylabel_name: y-axis label.
    :param alpha: chart bar brightness.
    """
    path = RESULT_DATA + experiment["file_name"] + sub_directory_name
    file_util.make_dir_if_not(path)

    values = visual_lines([x_values, plot_values, hist_values], experiment, "frequency_plot_hist")
    density_values = stat_func.density_values(hist_values, experiment["number_of_intervals_xi2"])

    lineHistChart.linePlotHist(
        path + '/' + file_name_prefix
        , x_values  # x_values
        , values[0]  # plot
        , values[1]  # hist
        , experiment["number_of_intervals_xi2"]
        , xlabel_name
        , ylabel_name
        , alpha
        , _dpi=experiment["plot_parameters"]["dpi"]
        , xMin=min(x_values)
        , xMax=max(x_values)
        , y1Min=min(density_values[1])
        , y1Max=max(density_values[1])
        , _fontsize=experiment["plot_parameters"]["frequency_plot_hist"]["fontsize"]
    )
