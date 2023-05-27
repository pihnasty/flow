"""Creating plots of harmonics to analyze the deterministic part of input flow
"""

import math
import pandas as pd

import pom.stochastic03.utils.FileUtil as file_util
import pom.stochastic03.Graphics.LineCharts.LineChart as line_chart


class DeterministicFlowHarmonics:
    """
    Visualization of the deterministic flow harmonics
    :param experiment: experiment conditions.
    """

    def __init__(self, experiment):
        self.experiment = experiment
        self.result_data = 'resultData/'
        self.sub_directory_name = experiment["dataset_result_folder_name"]
        self.file_name_prefix = 'd_flow_harm_'
        self.size = 1000
        self.plot_parameters = 'plot_parameters'
        self.plot_name = 'd_flow_harmonics'

    def show(self):
        """ Visualization of the deterministic flow harmonics"""
        path = (self.result_data
                + self.experiment['file_name'] + '/'
                + self.sub_directory_name)
        file_util.make_dir_if_not(path)
        fourier_df = self.read_fourier_coefficients()

        lines = pd.DataFrame()
        temp_size = int(self.size)
        lines['tau'] = [0.0] * round(temp_size)
        lines['harmonic0'] = [0.0] * round(temp_size)
        lines['harmonic1'] = [0.0] * round(temp_size)
        lines['harmonic2'] = [0.0] * round(temp_size)
        lines['harmonic3'] = [0.0] * round(temp_size)
        lines['harmonic4'] = [0.0] * round(temp_size)
        lines['harmonic5'] = [0.0] * round(temp_size)
        lines['summ'] = [0.0] * round(temp_size)

        for i in range(temp_size):
            tau = float(i) / self.size
            lines['tau'][i] = tau
            lines['harmonic0'][i] = fourier_df["fourier coefficient"][0] / 2
            lines['harmonic1'][i] = (fourier_df["fourier coefficient"][1]
                                     * math.cos(1 * math.pi * tau))
            lines['harmonic2'][i] = (fourier_df["fourier coefficient"][2]
                                     * math.cos(2 * math.pi * tau))
            lines['harmonic3'][i] = (fourier_df["fourier coefficient"][3]
                                     * math.cos(3 * math.pi * tau))
            lines['harmonic4'][i] = (fourier_df["fourier coefficient"][4]
                                     * math.cos(4 * math.pi * tau))
            lines['harmonic5'][i] = (fourier_df["fourier coefficient"][5]
                                     * math.cos(5 * math.pi * tau))
        lines['summ'] = (lines['harmonic0']
                         + lines['harmonic1']
                         + lines['harmonic2']
                         + lines['harmonic3']
                         + lines['harmonic4']
                         + lines['harmonic5']
                         )

        plot_values = [lines['tau'].values
            , lines['harmonic0'].values
            , lines['harmonic1'].values
            , lines['harmonic2'].values
            , lines['harmonic3'].values
            , lines['harmonic4'].values
            , lines['harmonic5'].values
            , lines['summ'].values
                       ]

        x_values = plot_values[0]
        y_values = line_chart.visual_lines(plot_values, self.experiment, self.plot_name)
        params = self.experiment[self.plot_parameters][self.plot_name]
        line_chart.line_plot3(path + '/' + self.file_name_prefix
                              , x_values
                              , y_values
                              , xlabel_name=params['x_label_name']
                              , title=params['y_label_name']
                              , _alpha_main=params['alpha_main']
                              , _alpha_grid=params['alpha_grid']
                              , _color=params['color']
                              , _dpi=self.experiment[self.plot_parameters]['dpi']
                              , x_min=min(x_values)
                              , x_max=1
                              , x_tick_main=params['x_tick_main']
                              , x_tick_auxiliary=params['x_tick_auxiliary']
                              , x_axis_order=params['x_axis_order']
                              , y1_min=-1
                              , y1_max=2
                              , y_tick_main=params['y_tick_main']
                              , y_tick_auxiliary=params['y_tick_auxiliary']
                              , _fontsize=params['fontsize']
                              , _x_size_plot=params['x_size_plot']
                              , _y_size_plot=params['y_size_plot']
                              , _plot_line_width=params['plot_line_width']
                              , _grid_line_width=params['grid_line_width']
                              , _adjust_left
                              =params["border_adjustment"]["left"]
                              , _adjust_right
                              =params["border_adjustment"]["right"]
                              , _adjust_top
                              =params["border_adjustment"]["top"]
                              , _adjust_bottom
                              =params["border_adjustment"]["bottom"]
                              )

    def read_fourier_coefficients(self):
        """Read fourier coefficients from csv file
        in panda data frame"""
        path = ('../stochastic03/resultData/' +
                self.sub_directory_name +
                '/output/fourier_coefficients_gamma_d.csv')
        return pd.read_csv(path, sep=';', index_col=0
                           , dtype={'fourier coefficient': 'float64'}
                           , decimal=',')
