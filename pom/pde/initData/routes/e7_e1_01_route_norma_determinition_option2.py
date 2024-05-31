from pom.pde.Constants import DISTRIBUTION_DENSITY, NORMAL_DISTRIBUTION, MEAN, STD, MIN, \
    MAX, NORMALIZATION_FACTOR

HALF_WIDTH_DELTA_FUNCTION = 0.00001
STD0_KOEF = 0.00001
MEAN_KOEF = 0.5

e7_e1_01_route_norma_determinition_option2 = {
    1: {
        0: {
            DISTRIBUTION_DENSITY : NORMAL_DISTRIBUTION,
            MEAN : 0.101,
            STD : 0.101 * STD0_KOEF,
            MIN : 0.0,
            MAX : 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.361 * MEAN_KOEF,
            STD: 0.361 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.036
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.303 * MEAN_KOEF,
            STD: 0.303 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.020
        },
        3: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.606 * MEAN_KOEF,
            STD: 0.606 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.024
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.909 * MEAN_KOEF,
            STD: 0.909 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.072
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101 * MEAN_KOEF,
            STD: 0.101 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.006
        },
        6: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.606 * MEAN_KOEF,
            STD: 0.606 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.008
        }
    },
    2: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.087,
            STD: 0.087 * STD0_KOEF,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.173 * MEAN_KOEF,
            STD: 0.173 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.002
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.173 * MEAN_KOEF,
            STD: 0.173 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.002
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.779 * MEAN_KOEF,
            STD: 0.779 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.009
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.086 * MEAN_KOEF,
            STD: 0.086 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.024
        },
    },
    3: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101,
            STD: 0.101 * STD0_KOEF,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.173 * MEAN_KOEF,
            STD: 0.173 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.002
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.202 * MEAN_KOEF,
            STD: 0.202 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.004
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.909 * MEAN_KOEF,
            STD: 0.909 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.006
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101 * MEAN_KOEF,
            STD: 0.101 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.024
        },
    },
    4: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.235,
            STD: 0.235 * STD0_KOEF,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.490 * MEAN_KOEF,
            STD: 0.490 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.048
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.924 * MEAN_KOEF,
            STD: 0.924 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.025
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 1.443 * MEAN_KOEF,
            STD: 1.443 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.015
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.231 * MEAN_KOEF,
            STD: 0.231 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.016
        },
    },
    5: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101,
            STD: 0.101 * STD0_KOEF,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.288 * MEAN_KOEF,
            STD: 0.288 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.025
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.144 * MEAN_KOEF,
            STD: 0.144 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.042
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 1.443 * MEAN_KOEF,
            STD: 1.443 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.006
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101 * MEAN_KOEF,
            STD: 0.101 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.024
        },
    },
    6: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.202,
            STD: 0.202 * STD0_KOEF,
            MIN: 0.0,
            MAX: 0.4
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.519 * MEAN_KOEF,
            STD: 0.519 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.012
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 1.010 * MEAN_KOEF,
            STD: 1.010 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.010
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 1.371 * MEAN_KOEF,
            STD: 1.371 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.006
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.202 * MEAN_KOEF,
            STD: 0.202 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.016
        },
    },
    7: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.173,
            STD: 0.173 * STD0_KOEF,
            MIN: 0.0,
            MAX: 0.4
        },
        1: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.188 * MEAN_KOEF,
            STD: 0.188 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.003
        },
        2: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.721 * MEAN_KOEF,
            STD: 0.721 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.009
        },
        3: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.865 * MEAN_KOEF,
            STD: 0.865 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.012
        },
        4: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 1.298 * MEAN_KOEF,
            STD: 1.298 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.036
        },
        5: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.173 * MEAN_KOEF,
            STD: 0.173 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.012
        },
        6: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.886 * MEAN_KOEF,
            STD: 0.886 * HALF_WIDTH_DELTA_FUNCTION,
            NORMALIZATION_FACTOR: 0.048
        }
    }
}


# 0,101	0,361	0,303	0,606	0,909	0,101	0,606
# 0,087	0,173	0,173	0,519	0,779	0,086	0,519
# 0,101	0,173	0,202	0,606	0,909	0,101	0,606
# 0,235	0,490	0,924	1,010	1,443	0,231	1,010
# 0,101	0,288	0,144	1,038	1,443	0,101	1,038
# 0,202	0,519	1,010	0,981	1,371	0,202	0,981
# 0,173	0,188	0,721	0,865	1,298	0,173	0,866
# 1,00
#
# 0.834 	0.036	0.020	0.024 	0.072 	0.006 	0.008
# 0.963  	0.002	0.002			0.009	0.024
# 0.964	0.002	0.004			0.006	0.024
# 0.896	0.048	0.025			0.015	0.016
# 0.903	0.025	0.042			0.006	0.024
# 0.956	0.012	0.010	 		0.006	0.016
# 0.880 	0,003	0,009	0,012	0,036	0.012	0.048
