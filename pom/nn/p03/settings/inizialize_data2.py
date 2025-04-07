"""
initial data
"""
experiments = {
    "0001": {
        "training_file_name": "raw_data_tableM.csv"
        ,"test_file_name": "raw_data_tableM.csv"
        ,"task_type" : ""
        ,"model_name":"model_01.pt"
        ,"architecture": {
            "inputFactors": {
                "count-node": 10
                , "activation-function" : "Sigmoid"
                , "weight-init-method" : "normal_"
                , "names":[
                    " 2.Allergic rhinitis ",
                    " 2.Atopic dermatitis ",
                    " 4.Bronchial asthma in relatives of second generation ",
                    " 8.Dog hair ",
                    " 8.Rabbit hair ",
                    " 8.Pillow feather ",
                    " 8.Sheep wool ",
                    " 11.FEV1 ",
                    " 12.CD8 10*3 cells ",
                    " 14.age "
                ]
            },
            "outputFactors": {
                "count-node": 1
                , "names": [
                    " 1.SEVERE PERSISTENT "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 55
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "normal_"
                }
                ,2: {
                    "count-node": 55
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "normal_"
                }
                ,3: {
                    "count-node": 55
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "normal_"
                }
                ,4: {
                    "count-node": 55
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "normal_"
                }
            },
        }
        , "learning" : {
            "count_epochs" : 10000
            ,"lr" : 0.001
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
                , "x_tick_main" : 1000
                , "x_tick_auxiliary" : 500
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
    },
    "0001_1": {
        "training_file_name": "training_data_set.csv"
        ,"test_file_name": "test_data_set.csv"
        ,"task_type" : ""
        ,"model_name":"model_01_05.pt"
        ,"architecture": {
            "inputFactors": {
                "count-node": 20
                , "activation-function" : "Sigmoid"
                , "weight-init-method" : "normal_"
            },
            "outputFactors": {
                "count-node": 10
            },
            "hiddenLayers": {
                1: {
                    "count-node": 55
                    , "activation-function" : "Sigmoid"
                    , "weight-init-method" : "normal_"
                }
                ,2: {
                    "count-node": 55
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
            "count_epochs" : 20000
            ,"lr" : 0.001
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
                , "x_tick_main" : 1000
                , "x_tick_auxiliary" : 500
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
    },
    "0002": {
        "training_file_name": "training_data_set_02.csv"
        ,"test_file_name": "test_data_set_02.csv"
        ,"task_type" : "classification"
        ,"model_name":"model_02.pt"
        ,"architecture": {
            "inputFactors": {
                "count-node": 12
                , "activation-function" : "Sigmoid"
                , "weight-init-method" : "normal_"
            },
            "outputFactors": {
                "count-node": 3
                , "activation-function" : "Softmax"
            },
            "hiddenLayers": {
                1: {
                    "count-node": 25
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
            "count_epochs" : 20000
            ,"lr" : 0.001
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
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
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 11
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 5000
                , "x_tick_auxiliary" : 2500
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
