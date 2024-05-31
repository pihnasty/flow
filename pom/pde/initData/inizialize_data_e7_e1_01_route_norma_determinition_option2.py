from pom.pde.Constants import TECHNOLOGICAL_ROUTE, MAX_OPERATION_TIME, NUMBER_DISTRIBUTION_DENSITY_INTERVALS, \
    DISTRIBUTION_DENSITY_LINE, INITIAL_DATA, RESULT_DATA, X_LABEL_NAME, NUMBER_OPERATION_TIME, SEED, ORDER_SIZE, \
    TECHNOLOGICAL_PATHS_LINE, VISUAL_LINE_SET, COLOR_LINE_SET, Y_MAX, N_TECHNOLOGICAL_PATHS_LINE, \
    N_MIDDLE_TECHNOLOGICAL_PATHS_LINE, N_LAST_TECHNOLOGICAL_PATHS_LINE, RANDOM_STEP, BATCH_TIME_HIST, \
    BATCH_TIME_DENSITY_LINE, NUMBER_BATCH_DENSITY_INTERVALS, PROBABILITY_LINE
from pom.pde.initData.routes.e7_e1_01_route_norma_determinition import e7_e1_01_route_norma_determinition
from pom.pde.initData.routes.e7_e1_01_route_norma_determinition_only_r0 import \
    e7_e1_01_route_norma_determinition_only_r0
from pom.pde.initData.routes.e7_e1_01_route_norma_determinition_option2 import \
    e7_e1_01_route_norma_determinition_option2
from pom.pde.initData.routes.e7_e1_01_route_normal import e7_e1_01_route_normal
from pom.stochastic03.utils.Constants import PLOT_PARAMETERS, Y_LABEL_NAME

"""
initial data
"""

MAX_OPERATION_TIME_VALUE = 2.0

experiments = {
    "e7_e1_01": {
        "project_structure": {
            "file_name": "dataset"
            , "files_category": "files"
            , "result_data_structure": {
                RESULT_DATA: "resultData"
                , INITIAL_DATA: "initial_data"
                , "initial_data_result": "initial"
                , "initial_data_dimensionless_result": "initial_dimensionless"
                , "initial_data_dimensionless_result2": "initial_dimensionless2"
                , "g_g2_result": "g_g2"
            }
        }

        , TECHNOLOGICAL_ROUTE: e7_e1_01_route_norma_determinition_option2
        , MAX_OPERATION_TIME: 2.0
        , NUMBER_DISTRIBUTION_DENSITY_INTERVALS: 200
        , NUMBER_BATCH_DENSITY_INTERVALS: 50
        , NUMBER_OPERATION_TIME: 100000
        , ORDER_SIZE: 60
        , SEED: 1
        , RANDOM_STEP : 61




        , PLOT_PARAMETERS: {
            "dpi": 1000
            , DISTRIBUTION_DENSITY_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , COLOR_LINE_SET: { 0:'k',  1:'k',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": MAX_OPERATION_TIME_VALUE
                , "x_tick_main": (MAX_OPERATION_TIME_VALUE/10)
                , "x_tick_auxiliary": (MAX_OPERATION_TIME_VALUE/20)
                , "y_min": 0
                , "y_max": 24.0
                , "y_tick_main": 2.0
                , "y_tick_auxiliary": 1.0
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$\vartheta_1$'
                , Y_LABEL_NAME: r'$f_1(\vartheta_1)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , BATCH_TIME_DENSITY_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , COLOR_LINE_SET: {0: 'k', 1: 'k', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 18
                , "x_max": 35
                , "x_tick_main": 1.0
                , "x_tick_auxiliary": 0.5
                , "y_min": 0
                , "y_max": 0.16
                , "y_tick_main": 0.04
                , "y_tick_auxiliary": 0.02
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$\tau_b$'
                , Y_LABEL_NAME: r'$f_b(\tau_b)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , PROBABILITY_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , COLOR_LINE_SET: {0: 'k', 1: 'k', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 19
                , "x_max": 35
                , "x_tick_main": 2.0
                , "x_tick_auxiliary": 1.0
                , "y_min": 0
                , "y_max": 1.0
                , "y_tick_main": 0.2
                , "y_tick_auxiliary": 0.1
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$\tau_b$'
                , Y_LABEL_NAME: r'$F_b(\tau_b)$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , TECHNOLOGICAL_PATHS_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
                , "color_line_set": {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k', 6: 'k', 7: 'k', 8: 'k', 9: 'k', 10: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 7
                , "x_tick_main": 1
                , "x_tick_auxiliary": 0.5
                , "y_min": 0
                , Y_MAX: 25.0
                , "y_tick_main": 5.0
                , "y_tick_auxiliary": 2.5
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$m$'
                , Y_LABEL_NAME: r'$\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , N_TECHNOLOGICAL_PATHS_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , COLOR_LINE_SET: { 0:'k',  1:'r',  2:'k',  3:'k',  4:'k',  5:'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 7
                , "x_tick_main": 1
                , "x_tick_auxiliary": 0.5
                , "y_min": 0
                , Y_MAX: 6.0
                , "y_tick_main": 0.6
                , "y_tick_auxiliary": 0.3
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$m$'
                , Y_LABEL_NAME: r'$\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , N_MIDDLE_TECHNOLOGICAL_PATHS_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , COLOR_LINE_SET: {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 7
                , "x_tick_main": 1
                , "x_tick_auxiliary": 0.5
                , "y_min": 6.0
                , Y_MAX: 12.0
                , "y_tick_main": 0.6
                , "y_tick_auxiliary": 0.3
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$m$'
                , Y_LABEL_NAME: r'$\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , N_LAST_TECHNOLOGICAL_PATHS_LINE: {
                VISUAL_LINE_SET: {"0": 0, "1": 1, "2": 2, "3": 1, "4": 1, "5": 1}
                , COLOR_LINE_SET: {0: 'k', 1: 'r', 2: 'k', 3: 'k', 4: 'k', 5: 'k'}
                , "fontsize": 9
                , "alpha_main": 1.0
                , "alpha_grid": 0.7
                , "color": "black"
                , "x_min": 0
                , "x_max": 7
                , "x_tick_main": 1
                , "x_tick_auxiliary": 0.5
                , "y_min": 18.0
                , Y_MAX: 24.0
                , "y_tick_main": 0.6
                , "y_tick_auxiliary": 0.3
                , "x_axis_order": "forward"  # "back" | "forward"
                , X_LABEL_NAME: r'$m$'
                , Y_LABEL_NAME: r'$\tau$'
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "plot_line_width": 1.5
                , "grid_line_width": 1.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
            , BATCH_TIME_HIST: {
                "visual_line_set": {"0": 0, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1}
                , "count_of_intervals_xi2": 50
                , "fontsize": 9
                , "x_label_name": r'$\tau_{b}$'
                , "y_label_name": r'$f_b(\tau_{b}$)'
                , "alpha": 0.7
                , "rwidth": 0.7
                , "x_size_plot": 85.0  # 86.5  #160.5
                , "y_size_plot": 60.0  # 72.0  #120.0
                , "border_adjustment": {
                    "left": 0.15, "right": 0.92, "top": 0.92, "bottom": 0.17
                }
            }
        }
        , "show_prepare_k": False
    }
}

