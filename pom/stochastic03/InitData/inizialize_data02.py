"""
initial data
"""
experiments = {
    "2023_05_23_dataset_2021_BhAsHuHoEv": {
        "project_structure": {
            "file_name": "dataset_2021_BhAsHuHoEv.csv"
            , "files_category": "files"
            , "result_data_structure": {
                "result_data": "resultData"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
            }
        }

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
                , "x_max": 30000
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
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

            , "initial_dimensionless_flow_line2": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
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
                , "y_min": 0.6
                , "y_max": 1.2
                , "y_tick_main": 0.1
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\theta$'
                , "y_label_name": r'$f(\theta)=\int_{0}^{1}\gamma(\tau)\gamma(\tau+\theta)d\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.88, "bottom": 0.17
                }
            }

            , "initial_correlation_part_first_line": {
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
                , "y_min": -0.6
                , "y_max": 1.0
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







            , "frequency_plot_hist": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "fontsize": 9 #8
            }
        }

        , "period": 100





        , "relative_sigma_correlation": 1.0
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": False
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
    }
}
