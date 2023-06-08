"""
initial data
"""
experiments = {
    "2023_05_23_PiSo_Template": {
        "file_name": "dataset_2016_SeStBeSeSt.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "initial_dimension_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 1.0 #0.7
                , "color": "black"
                , "x_tick_main": 200
                , "x_tick_auxiliary": 0
                , "y_tick_main": 200
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 79.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.92, "bottom": 0.17}
            }
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }
    },
    "2023_05_23_PiSo_Template_2016_SeStBeSeSt": {
        "file_name": "dataset_2016_SeStBeSeSt.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "initial_dimension_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_tick_main": 1.0
                , "x_tick_auxiliary": 0.1
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 79.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.12, "right": 0.98, "top": 0.92, "bottom": 0.17}
            }
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "2023_05_23_PiSo_Template_2021_DoKrWa": {
        "file_name": "dataset_2021_DoKrWa.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "initial_dimension_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_tick_main": 3000.0
                , "x_tick_auxiliary": 200
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 79.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.12, "right": 0.98, "top": 0.92, "bottom": 0.17}
            }
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "dataset_2021_DoKrWa.csv": {
        "file_name": "dataset_2021_DoKrWa.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "initial_dimension_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 11
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_tick_main": 3000.0
                , "x_tick_auxiliary": 200
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0001": {
        "file_name": "dataset_2013_KoStBe.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "initial_dimension_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_tick_main": 500.0
                , "x_tick_auxiliary": 50
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 86.5
                , "y_size_plot": 65.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0002": {
        "file_name": "dataset_2019_ReAvRyFe.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0003": {
        "file_name": "dataset_2019_Stadnyk_3b.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0004": {
        "file_name": "dataset_2012_St.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0005": {
        "file_name": "dataset_2012_Stav.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0006": {
        "file_name": "dataset_2019_St.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    },
    "0007": {
        "file_name": "dataset_2019_StSeBeViTk_3a.csv"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    }
    , "default": {
        "file_name": "dataset_2021_BhAsHuHoEv.csv"
        , "tau_correlation": 0.025
        , "relative_sigma_correlation": 0.0625
        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 200
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "show_flow_density": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 10
            }
            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 8
            }
        }
    }
}
