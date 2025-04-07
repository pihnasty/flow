"""
initial data
"""
experiments = {
    "0002": {
        "training_file_name": "raw_data_tableM_Article_2024_03.csv"
        ,"test_file_name": "raw_data_tableM_Article_2024_03.csv"
        ,"task_type" : "classification"
        ,"model_name":"model_02.pt"
        ,"architecture": {
            "inputFactors": {
                "activation-function" : "Sigmoid"
                , "weight-init-method" : "normal_"
                , "names": (
                    " 2.Atopic dermatitis ",
                    " 4.Bronchial asthma in relatives of second generation ",
                    " 2.Allergic rhinitis ",
                    " 8.Sheep wool ",
                    " 8.Domestic dust ",
                    " 8.Pillow feather ",
                    " 8.Dog hair ",
                    " 4.Bronchial asthma in father ",
                    " 14.age ",
                    " 12.CD25 10*3 cells "

                )
            },
            "outputFactors": {
                "activation-function" : "Softmax"
                , "names": [
                    " 1.SEVERE PERSISTENT ",
                    " 1.MODERATE PERSISTENT ",
                    " 1.MILD PERSISTENT ",
                    " 1.INTERMITTENT "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 15
                    , "activation-function" : "Sigmoid"   #Sigmoid" "ReLU"
                    , "weight-init-method" : "normal_"
                },
                2: {
                    "count-node": 15
                    , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                    , "weight-init-method": "normal_"
                },
                # 2: {
                #     "count-node": 50
                #     , "activation-function" : "Sigmoid"
                #     , "weight-init-method" : "normal_"
                # }
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
            , "seed" : 50
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set" : {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 18
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 5000
                , "x_tick_auxiliary" : 2500
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
                , "color_line_set": { 0:'k',  1:'k',  2:'r',  3:'b',  4:'k',  5:'k'}
                , "color" : "black"
                , "fontsize": 18
                , "alpha_main" : 1.0
                , "alpha_grid" : 0.7
                , "x_tick_main" : 5000
                , "x_tick_auxiliary" :2500
                , "y_tick_main" : 0
                , "y_tick_auxiliary" : 0
                , "x_axis_order" : "forward"      # "back" | "forward"
                , "x_label_name" : r'$epoch$'  # r'$lg_{10}(epoch)$'
                , "y_label_name" : r'$loss, test loss, accurancy$'
                , "x_size_plot" : 160.5
                , "y_size_plot" : 120.0
                , "plot_line_width" : 2.0
                , "grid_line_width" : 1.0
            }
        }
    },
    "0003": {
        "training_file_name": "raw_data_tableM.csv"
        , "test_file_name": "raw_data_tableM.csv"
        , "task_type": "classification"
        , "model_name": "model_02.pt"
        , "architecture": {
            "inputFactors": {
                "activation-function": "Sigmoid"
                , "weight-init-method": "normal_"
                , "names": [
                    " 2.Allergic rhinitis ",
                    " 2.Atopic dermatitis ",
                    " 3.Number of years from the first symptoms ",
                    " 4.Bronchial asthma in relatives of second generation ",
                    " 4.Bronchial asthma in mother ",
                    " 4.Allergic rhinitis in mother ",
                    " 4.Bronchial asthma in father ",
                    " 4.Allergic rhinitis in father ",
                    " 5.RBC ",
                    " 5.HBC ",
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
                "activation-function": "Softmax"
                , "names": [
                    " 1.SEVERE PERSISTENT ",
                    " 1.MODERATE PERSISTENT ",
                    " 1.MILD PERSISTENT ",
                    " 1.INTERMITTENT "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 15
                    , "activation-function": "Sigmoid"
                    , "weight-init-method": "normal_"
                },
                # 2: {
                #     "count-node": 50
                #     , "activation-function" : "Sigmoid"
                #     , "weight-init-method" : "normal_"
                # }
                # ,2: {
                #     "count-node": 5
                #     , "activation-function" : "no"
                #     , "weight-init-method" : "constant_"
                # }
            },
        }
        , "learning": {
            "count_epochs": 20000
            , "lr": 0.001
            , "seed": 50
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "color": "black"
                , "fontsize": 11
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\theta(\tau)$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
            , "loss": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "color": "black"
                , "fontsize": 11
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$epoch$'  # r'$lg_{10}(epoch)$'
                , "y_label_name": r'$loss$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
        }
    },
    "0004": {
        "training_file_name": "raw_data_table.csv"
        , "test_file_name": "raw_data_table.csv"
        , "task_type": "classification"
        , "model_name": "model_02.pt"
        , "architecture": {
            "inputFactors": {
                "activation-function": "Sigmoid"
                , "weight-init-method": "normal_"
                , "names": [
                    " 13.TSLP"
                    ]
            },
            "outputFactors": {
                "activation-function": "Softmax"
                , "names": [
                    " 1.SEVERE PERSISTENT ",
                    " 1.MODERATE PERSISTENT ",
                    " 1.MILD PERSISTENT ",
                    " 1.INTERMITTENT ",
                    " 1.HEALTHY     "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 15
                    , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                    , "weight-init-method": "normal_"
                },
                2: {
                    "count-node": 15
                    , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                    , "weight-init-method": "normal_"
                },
                # 2: {
                #     "count-node": 50
                #     , "activation-function" : "Sigmoid"
                #     , "weight-init-method" : "normal_"
                # }
                # ,2: {
                #     "count-node": 5
                #     , "activation-function" : "no"
                #     , "weight-init-method" : "constant_"
                # }
            },
        }
        , "learning": {
            "count_epochs": 20000
            , "lr": 0.001
            , "seed": 50
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "color": "black"
                , "fontsize": 18
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\theta(\tau)$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
            , "loss": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'k', 2: 'r', 3: 'b', 4: 'k', 5: 'k'}
                , "color": "black"
                , "fontsize": 18
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$epoch$'  # r'$lg_{10}(epoch)$'
                , "y_label_name": r'$loss, test loss, accurancy$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
        }
    },
    "0005": {
        "training_file_name": "raw_data_table.csv"
        , "test_file_name": "raw_data_table.csv"
        , "task_type": "classification"
        , "model_name": "model_02.pt"
        , "architecture": {
            "inputFactors": {
                "activation-function": "Sigmoid"
                , "weight-init-method": "normal_"
                , "names": [
                    " 5.RBC ",
                    " 5.HBC ",
                    " 5.WBC ",
                    " 5.Eosinophils % ",
                    " 5.Basophils % ",
                    " 5.Band neutrophils % ",
                    " 5.Segmented neutrophils % ",
                    " 5.Lymphocytes % ",
                    " 5.Monocytes % ",
                    " 5.ESR ",
                    " 10.Ig E ",
                    # " 12.Leucocytes ",
                    # " 12.Neutrophils % ",
                    # " 12.Neutrophils T ",
                    # " 12.Lymphocytes % ",
                    # " 12.CD3 % ",
                    # " 12.CD4 % ",
                    # " 12.CD4 10*3 cells ",
                    # " 12.CD8 % ",
                    # " 12.CD8 10*3 cells ",
                    # " 12.CD16 % ",
                    # " 12.CD16 10*3 cells ",
                    # " 12.CD22 % ",
                    # " 12.CD22 10*3 cells ",
                    # " 12.CD25 % ",
                    # " 12.CD25 10*3 cells ",
                    # " 12.IgA ",
                    # " 12.IgM ",
                    # " 12.IgG ",
                    # " 12.Phagocytosis of latex % ",
                    # " 12.Phagocytic number ",
                    # " 12.Total complement (СН 50) ",
                    # " 12.Spontaneous NBT tests % ",
                    # " 12.Stimulated NBT test % "
                ]
            },
            "outputFactors": {
                "activation-function": "Softmax"
                , "names": [
                    " 1.SEVERE PERSISTENT ",
                    " 1.MODERATE PERSISTENT ",
                    " 1.MILD PERSISTENT ",
                    " 1.INTERMITTENT ",
                    " 1.HEALTHY     "
                ]
            },
            "hiddenLayers": {
                1: {
                    "count-node": 35
                    , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                    , "weight-init-method": "normal_"
                },
                2: {
                    "count-node": 50
                    , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                    , "weight-init-method": "normal_"
                },
                # 3: {
                #     "count-node": 15
                #     , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                #     , "weight-init-method": "normal_"
                # },
                # 4: {
                #     "count-node": 10
                #     , "activation-function": "Sigmoid"  # Sigmoid" "ReLU"
                #     , "weight-init-method": "normal_"
                # },
                # 2: {
                #     "count-node": 50
                #     , "activation-function" : "Sigmoid"
                #     , "weight-init-method" : "normal_"
                # }
                # ,2: {
                #     "count-node": 5
                #     , "activation-function" : "no"
                #     , "weight-init-method" : "constant_"
                # }
            },
        }
        , "learning": {
            "count_epochs": 20000
            , "lr": 0.001
            , "seed": 50
        }
        , "plot_parameters": {
            "dpi": 1000
            , "output_flow": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "color": "black"
                , "fontsize": 18
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$\tau$'
                , "y_label_name": r'$\theta(\tau)$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
            , "loss": {
                "visual_line_set": {"0": 0, "1": 1, "2": 2, "3": 3, "4": 1, "5": 1}
                , "color_line_set": {0: 'k', 1: 'k', 2: 'r', 3: 'b', 4: 'k', 5: 'k'}
                , "color": "black"
                , "fontsize": 18
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "x_tick_main": 5000
                , "x_tick_auxiliary": 2500
                , "y_tick_main": 0
                , "y_tick_auxiliary": 0
                , "x_axis_order": "forward"  # "back" | "forward"
                , "x_label_name": r'$epoch$'  # r'$lg_{10}(epoch)$'
                , "y_label_name": r'$loss, test loss, accurancy$'
                , "x_size_plot": 160.5
                , "y_size_plot": 120.0
                , "plot_line_width": 2.0
                , "grid_line_width": 1.0
            }
        }
    }
}
