from pom.stochastic03.utils.Constants import ERR_APPROX_INIT_DIMLESS_FLOW_LINE,\
    ERR_APPROX_INIT_DIMLESS_FLOW_HIST, TAU_SEQUENCE_HIST, \
    INITIAL_DATA_DIMENSIONLESS_RESULT, G_G2, \
    INIT_DIMENSIONLESS_FLOW_LINE, INIT_DIMENSIONLESS_FLOW_HIST, INIT_CORRELATION_LINE, PERIOD

"""
initial data
"""
experiments = {
    "2023_05_23_dataset_2013_KoStBe_CopyForGenerator": {
        "project_structure": {
            "file_name": "dataset_2013_KoStBeCopyForGenerator.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period":50
        , "load_period": 20
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 15
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , INIT_DIMENSIONLESS_FLOW_LINE: {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2012_St_CopyForGenerator": {
        "project_structure": {
            "file_name": "dataset_2012_St_CopyForGenerator.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period":100
        , "load_period": 6
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 15
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2018_BuyCopyForGenerator": {
        "project_structure": {
            "file_name": "dataset_2018_BuyCopyForGenerator.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period": 3
        , "load_period": 192
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 4
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2013_KoStBeCopyForGenerator": {
        "project_structure": {
            "file_name": "dataset_2013_KoStBeCopyForGenerator.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period": 10
        , "load_period": 10
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 25
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2010_JeRiBeStJeMiRaCopyForGenerator": {
        "project_structure": {
            "file_name": "dataset_2010_JeRiBeStJeMiRaCopyForGenerator.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period": 100
        , "load_period": 6
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 6
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2021_BhAsHuHoEvCopyForGenerator": {
        "project_structure": {
            "file_name": "dataset_2021_BhAsHuHoEvCopyForGenerator.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period": 10
        , "load_period": 10
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 30
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 10
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
#                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
#                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2021_BhAsHuHoEvCopyForGenerator2": {
        "project_structure": {
            "file_name": "dataset_2021_BhAsHuHoEvCopyForGenerator2.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period": 10
        , "load_period": 10
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 30
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 10
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 10
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2021_BhAsHuHoEvCopyForGenerator3": {
        "project_structure": {
            "file_name": "dataset_2021_BhAsHuHoEvCopyForGenerator3.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , "period": 10
        , "load_period": 10
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 30
        , "correlation_tau": 0.3


        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 35000
                , "x_tick_main": 10000
                , "x_tick_auxiliary": 5000
                , "y_min": 0
                , "y_max": 0.1
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'b',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name":  r'$z_s(\theta)$' # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }






            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }



            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }




        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50


    },
    "2023_05_23_dataset_2018_Buy_first_flow": {
        "project_structure": {
            "file_name": "dataset_2018_Buy_first_flow.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , INITIAL_DATA_DIMENSIONLESS_RESULT: "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , G_G2: "g_g2"
                , "gamma_optimal_s": "gamma_optimal_s"
                , "test_theory_cor_function_exp": "test_theory_cor_function_exp"
                , "test_theory_cor_function_exp_1_plus_tau": "test_theory_cor_function_exp_1_plus_tau"
                , "test_theory_cor_function_exp_1_minus_tau": "test_theory_cor_function_exp_1_minus_tau"
                , "test_theory_cor_function_exp_cos_betta_tau": "test_theory_cor_function_exp_cos_betta_tau"
            }
        }

        , PERIOD: 10
        , "load_period": 10
        , "correlation_addition_time": 0.0
        , "number_of_harmonics": 30
        , "correlation_tau": 0.3

        , "plot_parameters": {
            "dpi": 1000
            , "initial_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 43000
                , "x_max": 53000
                , "x_tick_main": 2000
                , "x_tick_auxiliary": 1000
                , "y_min": 0.0
                , "y_max": 100.0
                , "y_tick_main": 10.0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$t$'
                , "y_label_name": r'$\lambda(t)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_flow_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\lambda$'
                , "y_label_name": r'f($\lambda$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'b', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 50.0
                , "y_tick_main": 5.0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , ERR_APPROX_INIT_DIMLESS_FLOW_LINE: {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'b', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -2.0
                , "y_max": 2.0
                , "y_tick_main": 0.50
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\epsilon(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_s(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_d_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": -1.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma_d(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_bar": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": ['k']
                , "x_min": 0.0
                , "x_max": 1.0
                , "x_tick_main": 0.5
                , "x_tick_auxiliary": 0.25
                , "y_min": 0.0
                , "y_max": 0.15
                , "y_tick_main": 0.05
                , "y_tick_auxiliary": 0.25
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$n$'
                , "y_label_name": r'$\sigma_n^2/\sigma^2$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.97, "top": 0.9, "bottom": 0.17
                }
            }
            , INIT_DIMENSIONLESS_FLOW_HIST: {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , ERR_APPROX_INIT_DIMLESS_FLOW_HIST: {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , TAU_SEQUENCE_HIST: {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 10
                , "fontsize": 9
                , "x_label_name": r'$T$'
                , "y_label_name": r'f($T$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }, ERR_APPROX_INIT_DIMLESS_FLOW_HIST: {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "gamma_optimum_s_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma_s$'
                , "y_label_name": r'f($\gamma_s$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 2
                , "x_tick_main": 0.2
                , "x_tick_auxiliary": 0.1
                , "y_min": 0
                , "y_max": 2.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\gamma(\tau)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , "initial_dimensionless_flow_hist2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 51
                , "fontsize": 9
                , "x_label_name": r'$\gamma$'
                , "y_label_name": r'f($\gamma$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }

            , "g_g2_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": 0.95
                , "y_max": 1.05
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$z_s(\theta)$'  # r'$f(\theta)=\int_{-1}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , INIT_CORRELATION_LINE: {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": {0: 'k', 1: 'k', 2: 'b', 3: 'g', 4: 'y', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -1.0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\vartheta$'
                , "y_label_name": r'$k(\vartheta$)'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                , "color_line_set": {0: 'k', 1: 'k', 2: 'b', 3: 'g', 4: 'y', 5: 'r'}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.2
                , "y_max": 1.2
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "test_theory_delta_cor_function_exp_line": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5}
                #                , "color_line_set": { 0:'k',  1:'k',  2:'b',  3:'g',  4:'y',  5:'r'}
                , "color_line_set": {0: 'k', 1: 'k', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 1
                , "x_tick_main": 0.1
                , "x_tick_auxiliary": 0.05
                , "y_min": -0.01
                , "y_max": 0.04
                , "y_tick_main": 0.01
                , "y_tick_auxiliary": 0.005
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$\Delta k(\theta)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9  # 8
            }
        }

        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_intervals_xi2": 50

    }
}