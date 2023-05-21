import math
import pom.stochastic03.utils.MathUtil as mu
import pandas as pd
import pom.stochastic03.utils.FileUtil as file_util
import pom.stochastic03.Graphics.LineCharts.LineChart as line_chart

class Flows:
    """
    Visualization of the distribution density of a random variable
    :param experiment: experiment conditions.
    """
    def __init__(self, experiment):
        self.gamma0_init = experiment["gamma0"]
        self.gamma2_init = experiment["gamma2"]
        self.mass_init = experiment["mass"]
        self.psi3_init = experiment["psi3"]
        self.mode_u1 = experiment["mode_u1"]
        self.mode_u2 = experiment["mode_u2"]
        self.mode_u3 = experiment["mode_u3"]
        self.z_mode = experiment["z_mode"]
        self.tau_d = experiment["tau_d"]
        self.tau_number = experiment["tau_number"]
        self.delta_tau_d = self.tau_d / self.tau_number

        self.n1_init = experiment["n1"]
        self.n2_init = experiment["n2"]

        self.G = [0.0] * self.tau_number
        self.tau = [0.0] * self.tau_number
        self.u1 = [0.0] * self.tau_number
        self.u2 = [0.0] * self.tau_number
        self.u3 = [0.0] * self.tau_number
        self.mass = [0.0] * self.tau_number
        self.psi3 = [0.0] * self.tau_number
        self.n1 = [0.0] * self.tau_number
        self.n2 = [0.0] * self.tau_number
        self.criterium_with_z = [0.0] * self.tau_number
        self.criterium_without_z = [0.0] * self.tau_number
        self.z_value = [0.0] * self.tau_number


        self.experiment = experiment
        self.result_data = 'resultData/'
        self.sub_directory_name = '/plot'
        self.file_name_prefix = 'STP_'
        self.size=1000
        self.plot_parameters = "plot_parameters"


    def set_criterium_with_z(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.criterium_with_z[0] = 0.0
        else:
            self.criterium_with_z[i] = self.criterium_with_z[i - 1]\
                                       + self.mass[i - 1] * self.u3[i - 1] * self.z(tau) * self.delta_tau_d

    def set_criterium_without_z(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.criterium_without_z[0] = 0.0
        else:
            self.criterium_without_z[i] = self.criterium_without_z[i - 1] \
                                       + self.mass[i - 1] * self.u3[i - 1] * self.delta_tau_d

    def get_criterium_r(self):
        return max(self.criterium_with_z)/max(self.criterium_without_z)

    def gamma0(self, tau):
        return self.gamma0_init["gamma00"] + self.gamma0_init["gamma01"] * math.sin(2 * math.pi /24 * tau)

    def get_u1(self, tau):
        i = self.get_i(tau)
        return self.u1[i]

    def set_u1(self, tau, u1_assume):
        i = self.get_i(tau)
        self.u1[i] = u1_assume

    def get_mode_u1(self):
        return self.mode_u1

    def gamma2_plan(self, tau):
        return self.gamma2_init["gamma20"] + self.gamma2_init["gamma21"] * math.sin(2 * math.pi /24 * tau)

    def get_u2(self, tau):
        i = self.get_i(tau)
        return self.u2[i]

    def set_u2(self, tau, u2_assume):
        i = self.get_i(tau)
        self.u2[i] = u2_assume

    def get_mode_u2(self):
        return self.mode_u2

    def get_u3(self, tau):
        i = self.get_i(tau)
        return self.u3[i]

    def set_u3(self, tau, u3_assume):
        i = self.get_i(tau)
        self.u3[i] = u3_assume

    def get_mode_u3(self):
        return self.mode_u3

    def get_mass(self, tau):
        i = self.get_i(tau)
        return self.mass[i]

    def set_mass(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.mass[0] = self.mass_init["mass0"]
        else:
            prev_tau = tau - self.delta_tau_d
            self.mass[i] = self.mass[i - 1] + (self.get_u1(prev_tau) - self.tetta_output_1(prev_tau)) * self.delta_tau_d
            if self.mass[i] < self.mass_init["mass_min"]:
                self.mass[i] = self.mass_init["mass_min"]
    def get_n1(self, tau):
        i = self.get_i(tau)
        return self.n1[i]

    def get_n1_min(self):
        return self.n1_init["n1_min"]

    def get_n1_max(self):
        return self.n1_init["n1_max"]

    def set_n1(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.n1[0] = self.n1_init["n10"]
        else:
            prev_tau = tau - self.delta_tau_d
            self.n1[i] = self.n1[i - 1] + (self.gamma0(prev_tau) - self.get_u1(prev_tau)) * self.delta_tau_d
            # if self.mass[i] < self.mass_init["mass_min"]:
            #     self.mass[i] = self.mass_init["mass_min"]

    def get_n2(self, tau):
        i = self.get_i(tau)
        return self.n2[i]


    def get_n2_min(self):
        return self.n2_init["n2_min"]

    def get_n2_max(self):
        return self.n2_init["n2_max"]

    def set_n2(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.n2[0] = self.n2_init["n20"]
        else:
            prev_tau = tau - self.delta_tau_d
            self.n2[i] = self.n2[i - 1] + (self.tetta_output_1(prev_tau) - self.get_u2(prev_tau)) * self.delta_tau_d
            # if self.mass[i] < self.mass_init["mass_min"]:
            #     self.mass[i] = self.mass_init["mass_min"]
    def Hamiltonian(self, tau, u1_assume, u2_assume, u3_assume):

        ksi = 1 - self.get_G(tau)
        if ksi > 0.0:
            psi3_expression = u1_assume - self.psi_flow(ksi) * u3_assume
        else:
            tau1 = self.get_tau1(tau)
            try:
                psi3_expression = u1_assume - self.get_u1(tau1) / self.get_u3(tau1) * u3_assume
            except:
                print("An exception has occurred!")

        return -self.z(tau) * u3_assume * self.get_mass(tau) + self.get_psi3(tau) * psi3_expression

    def get_psi3(self, tau):
        i = self.get_i(tau)
        return self.psi3[i]

    def set_psi3(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.psi3[0] =self.psi3_init["psi30"]
        else:
            self.psi3[i] = self.psi3[i-1] + self.z(tau)* self.get_u3(self.tau[i-1]) * self.delta_tau_d

    def psi_flow(self, ksi):
        return 0


    def z(self, tau):
        if self.z_mode == "z_escom_night":
            return self.z_escom_night(tau)
        return 0

    def z_escom_night(self, tau):
        z = 0.85
        day_tau = tau % 24
        if (6 < day_tau and day_tau < 22):
            z = 1.09
        return z

    def set_z(self, tau):
        i = self.get_i(tau)
        self.z_value[i] = self.z(tau)

    def get_G(self, tau):
        i = self.get_i(tau)
        return self.G[i]

    def set_G(self, tau):
        i = self.get_i(tau)
        if i == 0:
            self.G[i] = 0.0
        else:
            self.G[i] = self.u3[i-1] * self.delta_tau_d + self.G[i - 1]

    def get_tau1(self, tau):
        i = self.get_i(tau)
        G1 = self.G[i] - 1
        if G1<0:
            return -1.0
        else:
            i_tau1 = mu.search(self.G, G1, 0, i - 1)
            return self.tau[i_tau1]

    def tetta_output_1(self, tau):
        ksi = 1 - self.get_G(tau)
        if ksi > 0:
            return self.psi_flow(ksi) * self.get_u3(tau)
        else:
            tau1 = self.get_tau1(tau)
            return self.get_u1(tau1) / self.get_u3(tau1) * self.get_u3(tau)

    def get_tau(self, tau):
        i = self.get_i(tau)
        return self.tau[i]

    def set_tau(self, tau):
        i = self.get_i(tau)
        self.tau[i] = tau

    def get_i(self, tau):
        return  round(tau / self.delta_tau_d)

    def show_1(self):
        """
        The method visualizes the calculated results.
        """
        path = self.result_data + self.experiment["file_name"] + self.sub_directory_name
        file_util.make_dir_if_not(path)
        self.plot_name = "plot_1"

        plot_values = [self.tau, self.u1, self.u2, self.u3, self.mass, self.z_value]


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
                              , x_max=100 # max(x_values)
                              , x_tick_main=params["x_tick_main"]
                              , x_tick_auxiliary=params["x_tick_auxiliary"]
                              , x_axis_order=params["x_axis_order"]
                              , y1_min=0
                              , y1_max=2.5
                              , y_tick_main=params["y_tick_main"]
                              , y_tick_auxiliary=params["y_tick_auxiliary"]
                              , _fontsize=params["fontsize"]
                              , _x_size_plot=params["x_size_plot"]
                              , _y_size_plot=params["y_size_plot"]
                              , _plot_line_width=params["plot_line_width"]
                              , _grid_line_width=params["grid_line_width"]
                              )

    def show_2(self):
        path = self.result_data + self.experiment["file_name"] + self.sub_directory_name
        file_util.make_dir_if_not(path)
        self.plot_name = "plot_psi3"

        plot_values = [self.tau, self.psi3, self.psi3, self.psi3, self.psi3]

        print(max(self.psi3))
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
                              , x_max=720 # max(x_values)
                              , x_tick_main=params["x_tick_main"]
                              , x_tick_auxiliary=params["x_tick_auxiliary"]
                              , x_axis_order=params["x_axis_order"]
                              , y1_min=-600
                              , y1_max=0.1
                              , y_tick_main=params["y_tick_main"]
                              , y_tick_auxiliary=params["y_tick_auxiliary"]
                              , _fontsize=params["fontsize"]
                              , _x_size_plot=params["x_size_plot"]
                              , _y_size_plot=params["y_size_plot"]
                              , _plot_line_width=params["plot_line_width"]
                              , _grid_line_width=params["grid_line_width"]
                              )


    def show_3(self):
        """
        The method visualizes the calculated results.
        """
        path = self.result_data + self.experiment["file_name"] + self.sub_directory_name
        file_util.make_dir_if_not(path)
        self.plot_name = "plot_3"

        plot_values = [self.tau, self.n1, self.n2, self.n1, self.n1]


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
                              , x_max=100 # max(x_values)
                              , x_tick_main=params["x_tick_main"]
                              , x_tick_auxiliary=params["x_tick_auxiliary"]
                              , x_axis_order=params["x_axis_order"]
                              , y1_min=0
                              , y1_max=1
                              , y_tick_main=params["y_tick_main"]
                              , y_tick_auxiliary=params["y_tick_auxiliary"]
                              , _fontsize=params["fontsize"]
                              , _x_size_plot=params["x_size_plot"]
                              , _y_size_plot=params["y_size_plot"]
                              , _plot_line_width=params["plot_line_width"]
                              , _grid_line_width=params["grid_line_width"]
                              )