import math
import pandas as pd
import pom.stochastic03.utils.FileUtil as file_util
import pom.stochastic03.Graphics.LineCharts.LineChart as line_chart

class SpeedStationaryPeriod:
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    """
    def __init__(self, experiment):
        self.experiment = experiment
        self.result_data = 'resultData/'
        self.sub_directory_name = '/SpeedStationaryPeriod'
        self.file_name_prefix = 'STP_'
        self.size=1000
        self.plot_parameters = "plot_parameters"
        self.plot_name = "speed_stationary_period"

    def g_g0(self, k_m, w_w0, tau):
        """
        The method calculates the speed.
        """
        coef_a = 0
        coef_b = 0
        g1_g0 = 0
        tau_tr = 1
        if 0.0 <= w_w0 < 0.4:
            coef_a = 1.6
            coef_b = 1.0
            g1_g0 = 0
        if 0.4 <= w_w0 < 0.6:
            coef_a = 2.4
            coef_b = 2.0
            g1_g0 = 0.4
        if 0.6 <= w_w0 < 0.74:
            coef_a = 3.31
            coef_b = 2.85
            g1_g0 = 0.6
        if 0.74 <= w_w0 < 0.84:
            coef_a = 4.56
            coef_b = 4.0
            g1_g0 = 0.74
        if 0.84 <= w_w0:
            coef_a = 7.2
            coef_b = 6.67
            g1_g0 = 0.84
        return (g1_g0 - (coef_a - k_m) / coef_b) * math.exp(- tau/ tau_tr) + (coef_a - k_m) / coef_b

    def g_g0_check(self, w_w0):
        """
        The method checks the speed.
        """
        g1_g0 = 0.0
        if 0.0 <= w_w0 < 0.4:
            g1_g0 = 0
        if 0.4 <= w_w0 < 0.6:
            g1_g0 = 0.4
        if 0.6 <= w_w0 < 0.74:
            g1_g0 = 0.6
        if 0.74 <= w_w0 < 0.84:
            g1_g0 = 0.74
        if 0.84 <= w_w0:
            g1_g0 = 0.84
        return g1_g0

    def show(self):
        """
        The method visualizes the calculated results.
        """
        path = self.result_data + self.experiment["file_name"] + self.sub_directory_name
        file_util.make_dir_if_not(path)

        lines = pd.DataFrame()
        temp_size = int(self.size)
        lines['tau'] = [0.0] * round(temp_size)
        lines['g1'] = [0.0] * round(temp_size)
        lines['g2'] = [0.0] * round(temp_size)
        lines['g3'] = [0.0] * round(temp_size)
        lines['g4'] = [0.0] * round(temp_size)

        x_max = 1
        g_st = 0.35
        k = 0.25
        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['g1'][i] = - k * (tau) + g_st

        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['g2'][i] = - k * (tau + tau * tau /2) + g_st

        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['g3'][i] = - k * (tau - 2/(math.pi *2) * math.cos(math.pi *2 * tau)) + g_st - 2*k/(2*math.pi)

        for i in range(temp_size):
            tau = float(i) / self.size * x_max
            lines['tau'][i] = tau
            lines['g4'][i] = - k * (tau - 2/(math.pi *2) * math.sin(math.pi *2 * tau)) + g_st

        plot_values = [lines['tau'].values, lines['g1'].values, lines['g2'].values,
                       lines['g3'].values, lines['g4'].values]


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
                              , y1_max=0.4
                              , y_tick_main=params["y_tick_main"]
                              , y_tick_auxiliary=params["y_tick_auxiliary"]
                              , _fontsize=params["fontsize"]
                              , _x_size_plot=params["x_size_plot"]
                              , _y_size_plot=params["y_size_plot"]
                              , _plot_line_width=params["plot_line_width"]
                              , _grid_line_width=params["grid_line_width"]
                              )
