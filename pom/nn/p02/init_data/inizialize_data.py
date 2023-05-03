"""
initial data
"""
experiments = {
    "0001": {
        "file_name": "raw_data_table.csv"
        ,"architecture" : {
            "inputFactors": {
                "names" :[
                    " 1.input ",
                    " 1.speed ",
                    " 2.input ",
                    " 2.speed ",
                    " 3.speed ",
                    " 4.input ",
                    " 4.speed ",
                    " 5.input ",
                    " 5.speed ",
                    " 6.speed ",
                    " 7.speed ",
                    " 8.speed "
                ]
                , "activation-function" : "Sigmoid"
                , "weight-init-method" : "constant_"
            },
            "outputFactors": {
                "names" : [
                    " 7.output ",
                    " 8.output "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 15
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "constant_"
                }
                ,2: {
                    "count-node": 5
                    , "activation-function" : "no"
                    , "weight-init-method" : "constant_"
                }
            },
        }
        , "learning" : {
          "count_epochs" : 1000
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 11
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 1
                , "x_tick_auxiliary" : 0.5
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$\tau$'
                , "y_label_name" : r'$\theta(\tau)$'
                , "x_size_plot" : 160.5
                , "y_size_plot" : 120.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
            , "loss": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 11
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 2000
                , "x_tick_auxiliary" : 1000
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$epoch$'  # r'$lg_{10}(epoch)$'
                , "y_label_name" : r'$loss$'
                , "x_size_plot" : 160.5
                , "y_size_plot" : 120.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
        }
    }
    ,
    "0002": {
        "file_name": "raw_data_table.csv"
        ,"architecture" : {
            "inputFactors": {
                "names" :[
                    " 1.input ",
                    " 1.speed ",
                    " 2.input ",
                    " 2.speed ",
                    " 4.input ",
                    " 4.speed ",
                    " 5.input ",
                    " 5.speed "
                ]
                , "activation-function" : "Sigmoid"
                , "weight-init-method" : "normal_"
            },
            "outputFactors": {
                "names" : [
                    " 7.output ",
                    " 8.output "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 15
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "normal_"
                }
                # ,2: {
                #     "count-node": 5
                #     , "activation-function" : "no"
                #     , "weight-init-method" : "constant_"
                # }
            },
        }
        , "learning" : {
            "count_epochs" : 50000
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 11
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 1
                , "x_tick_auxiliary" : 0.5
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$\tau$'
                , "y_label_name" : r'$\theta(\tau)$'
                , "x_size_plot" : 160.5
                , "y_size_plot" : 120.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
            , "loss": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 11
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 10000
                , "x_tick_auxiliary" : 5000
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$epoch$'  # r'$lg_{10}(epoch)$'
                , "y_label_name" : r'$loss$'
                , "x_size_plot" : 160.5
                , "y_size_plot" : 120.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
        }
    }
}
