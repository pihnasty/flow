"""
initial data
"""
experiments = {
    "0001": {
        "file_name": "EngineMechanicalCharacteristics"
        , "tau_correlation": 0.025

        , "relative_sigma_correlation": 1.0

        , "period": 200
        , "c0_show_var2": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
        , "quality_criterion": {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
        , "show_prepare_k": True
        , "number_of_harmonics": 50
        , "number_of_intervals_xi2": 50
        , "plot_parameters": {
            "dpi": 1000
            , "engine_mechanical_characteristics": {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "fontsize": 14
                , "alpha_main" : 1.0
                , "alpha_grid" : 1.0
                , "color" : "black"
                , "x_tick_main" : 0.05
                , "x_tick_auxiliary" : 0.05
                , "x_axis_order" : "back"      # "back" | "forward"
                , "y_tick_main" : 0.05
                , "y_tick_auxiliary" : 0.05
                , "x_label_name" : r'$\omega$/$\omega_0$'
                , "y_label_name" : r'$M/M_0$'
                , "x_size_plot" : 172.8 # 86.5
                , "y_size_plot" : 130.0 #65.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
        }
    }
}
