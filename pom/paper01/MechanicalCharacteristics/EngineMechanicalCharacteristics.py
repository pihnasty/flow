import math

import pom.stochastic03.utils.FileUtil as file_util
import pom.stochastic03.Graphics.LineCharts.LineChart as line_chart
import pandas as pd
class EngineMechanicalCharacteristics:
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    """
    def __init__(self, experiment):
        self.experiment = experiment
        self.result_data = 'resultData/'
        self.sub_directory_name = ''
        self.file_name_prefix = 'EMCh_'
        self.size=1000
        self.plot_parameters = "plot_parameters"
        self.plot_name ="engine_mechanical_characteristics"

    def m_m0(self, w_w0):
        coef_a = 0
        coef_b = 0
        if 0.0 <= w_w0 < 0.4:
            coef_a = 1.6
            coef_b = 1.0
        if 0.4 <= w_w0 < 0.6:
            coef_a = 2.4
            coef_b = 2.0
        if 0.6 <= w_w0 < 0.74:
            coef_a = 3.31
            coef_b = 2.85
        if 0.74 <= w_w0 < 0.84:
            coef_a = 4.56
            coef_b = 4.0
        if 0.84 <= w_w0 < 0.9:
            coef_a = 7.2
            coef_b = 6.67
        return coef_a - coef_b * w_w0

    def show(self):
        path = self.result_data + self.experiment["file_name"] + self.sub_directory_name
        file_util.make_dir_if_not(path)

        lines = pd.DataFrame()
        temp_size = int(self.size )
        lines['tau'] = [0.0] * round(temp_size)
        lines['harmonic0'] = [0.0] * round(temp_size)
        lines['harmonic1'] = [0.0] * round(temp_size)
        lines['harmonic2'] = [0.0] * round(temp_size)
        lines['harmonic3'] = [0.0] * round(temp_size)
        lines['harmonic4'] = [0.0] * round(temp_size)

        for i in range(temp_size):
            tau = float(i) / self.size
            lines['tau'][i] = tau
            lines['harmonic0'][i] = math.cos(2*math.pi*tau)
            lines['harmonic1'][i] = 2.0*math.cos(3*math.pi*tau)
            lines['harmonic2'][i] = math.cos(4*math.pi*tau)
            lines['harmonic3'][i] = math.cos(5*math.pi*tau)
            lines['harmonic4'][i] = math.cos(5*math.pi*tau)

        plot_values = [lines['tau'].values
            , lines['harmonic0'].values
            , lines['harmonic1'].values
            , lines['harmonic2'].values
            , lines['harmonic3'].values
            , lines['harmonic4'].values
                       ]


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
                              , x_max=1
                              , x_tick_main=params["x_tick_main"]
                              , x_tick_auxiliary=params["x_tick_auxiliary"]
                              , x_axis_order=params["x_axis_order"]
                              , y1_min=-2
                              , y1_max=2
                              , y_tick_main=params["y_tick_main"]
                              , y_tick_auxiliary=params["y_tick_auxiliary"]
                              , _fontsize=params["fontsize"]
                              , _x_size_plot=params["x_size_plot"]
                              , _y_size_plot=params["y_size_plot"]
                              , _plot_line_width=params["plot_line_width"]
                              , _grid_line_width=params["grid_line_width"]
                              )