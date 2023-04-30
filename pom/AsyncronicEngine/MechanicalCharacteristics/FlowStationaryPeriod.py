import math
import pandas as pd
import pom.stochastic03.utils.FileUtil as file_util
import pom.stochastic03.Graphics.LineCharts.LineChart as line_chart

class FlowStationaryPeriod:
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    """
    def __init__(self, experiment):
        self.experiment = experiment
        self.result_data = 'resultData/'
        self.sub_directory_name = '/FlowStationaryPeriod'
        self.file_name_prefix = 'STP_'
        self.size=1000
        self.plot_parameters = "plot_parameters"
        self.plot_name = "flow_stationary_period"

    def show(self):
        """
        The method visualizes the calculated results.
        """
        path = self.result_data + self.experiment["file_name"] + self.sub_directory_name
        file_util.make_dir_if_not(path)

        lines = pd.DataFrame()
        temp_size = int(self.size)
        lines['tau'] = [0.0] * round(temp_size)
        lines['gamma1'] = [0.0] * round(temp_size)
        lines['gamma2'] = [0.0] * round(temp_size)
        lines['gamma3'] = [0.0] * round(temp_size)
        lines['gamma4'] = [0.0] * round(temp_size)

        x_max = 1
        g_st = 0.35
        k = 0.25
        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['gamma1'][i] = k

        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['gamma2'][i] = k * (1 + tau)

        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['gamma3'][i] = k * (1 + math.sin(math.pi *2 * tau))

        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['gamma4'][i] = k * (1 + math.cos(math.pi *2 * tau))

        plot_values = [lines['tau'].values, lines['gamma1'].values, lines['gamma2'].values,
                       lines['gamma3'].values, lines['gamma4'].values]


        x_values = plot_values[0]
        y_values = line_chart.visual_lines(plot_values, self.experiment, self.plot_name)
        params=self.experiment[self.plot_parameters][self.plot_name]
        line_chart.line_plot3(path + '/' + self.file_name_prefix
                              , x_values
                              , y_values
                              , xlabel_name=params["x_label_name"]
                              , title=params["y_label_name"]
                              , _alpha_main=params["alpha_main"]
                              , _alpha_grid=params["alpha_grid"]
                              , _color=params["color"]
                              , _dpi=self.experiment[self.plot_parameters]["dpi"]
                              , x_min=min(x_values)
                              , x_max=x_max
                              , x_tick_main=params["x_tick_main"]
                              , x_tick_auxiliary=params["x_tick_auxiliary"]
                              , x_axis_order=params["x_axis_order"]
                              , y1_min=0
                              , y1_max=0.5
                              , y_tick_main=params["y_tick_main"]
                              , y_tick_auxiliary=params["y_tick_auxiliary"]
                              , _fontsize=params["fontsize"]
                              , _x_size_plot=params["x_size_plot"]
                              , _y_size_plot=params["y_size_plot"]
                              , _plot_line_width=params["plot_line_width"]
                              , _grid_line_width=params["grid_line_width"]
                              )
