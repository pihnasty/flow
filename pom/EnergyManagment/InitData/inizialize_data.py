"""
initial data
"""
experiments = {
    "0001": {
        "file_name": "EnergyManagement"
        , "tau_d" : 720
        , "tau_number" : 100000
        , "gamma0" : {
            "gamma00" : 0.5
            ,"gamma01" : 0.3
        }
        , "gamma2" : {
            "gamma20" : 0.5
            ,"gamma21" : 0.3
        }
        , "mass" : {
            "mass0" : 1.4
            ,"mass_min" : 1.4
        }
        , "n1" : {
            "n10" : 0.5
            ,"n1_min" : 0.1
            ,"n1_max" : 1.9
        }
        , "n2" : {
            "n20" : 0.5
            ,"n2_min" : 0.1
            ,"n2_max" : 1.9
        }
        , "mode_u1" : {0.0001, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 }
        , "mode_u2" : {0.0001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 }
        , "mode_u3" : {0.0001, 0.176, 0.246, 0.316, 0.386, 0.456, 0.526, 0.596, 0.666, 0.736, 0.806, 0.876 }
        , "psi3" : {
            "psi30" : -550.0
        }
        , "z_mode" : "z_escom_night"
        , "plot_parameters": {
            "dpi": 1000
            , "plot_1": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 1, "3": 3, "4": 4, "5": 5}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 8
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 10
                , "x_tick_auxiliary" : 5
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$\tau$'
                , "y_label_name" : r'$m(\tau), u_1(\tau), u_3(\tau), z(\tau)$'
                , "x_size_plot" : 80.5
                , "y_size_plot" : 60.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
            , "plot_psi3": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 8
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 100
                , "x_tick_auxiliary" : 50
                , "y_tick_main" : 100
                , "y_tick_auxiliary" : 50
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$\tau$'
                , "y_label_name" : r'$\psi_3(\tau)$'
                , "x_size_plot" : 80.5
                , "y_size_plot" : 60.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
            , "plot_3": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 2, "4": 2, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 8
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 10
                , "x_tick_auxiliary" : 5
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$\tau$'
                , "y_label_name" : r'$n_1(\tau), n_2(\tau)$'
                , "x_size_plot" : 80.5
                , "y_size_plot" : 60.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
        }
    }
}
