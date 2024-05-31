from pom.pde.Constants import DISTRIBUTION_DENSITY, NORMAL_DISTRIBUTION, MEAN, STD, MIN, \
    MAX, NORMALIZATION_FACTOR, \
    UNIFORM_DISTRIBUTION

WIDTH_DELTA_FUNCTION = 0.1

e7_e1_01_route_normal_and_uniform = {
    1 : {
        0 : {
            DISTRIBUTION_DENSITY : NORMAL_DISTRIBUTION,
            MEAN : 0.101,
            STD : 0.101 * 0.2,
            MIN : 0.0,
            MAX : 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.361,
            MIN: 0.361 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.036
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.303,
            MIN: 0.303 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.020
        },
        3: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.606,
            MIN: 0.606 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.024
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.909,
            MIN: 0.909 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.072
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.101,
            MIN: 0.101 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.006
        },
        6: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.606,
            MIN: 0.606 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.008
        }
    },
    2: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.087,
            STD: 0.087 * 0.2,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.173,
            MIN: 0.173 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.002
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.173,
            MIN: 0.173 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.002
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.779,
            MIN: 0.779 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.009
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.086,
            MIN: 0.086 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.024
        },
    },
    3: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101,
            STD: 0.101 * 0.2,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.173,
            MIN: 0.173 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.002
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.202,
            MIN: 0.202 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.004
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.909,
            MIN: 0.909 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.006
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.101,
            MIN: 0.101 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.024
        },
    },
    4: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.235,
            STD: 0.235 * 0.2,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.490,
            MIN: 0.490 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.048
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.924,
            MIN: 0.924 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.025
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 1.443,
            MIN: 1.443 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.015
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.231,
            MIN: 0.231 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.016
        },
    },
    5: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.101,
            STD: 0.101 * 0.2,
            MIN: 0.0,
            MAX: 0.2
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.288,
            MIN: 0.288 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.025
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.144,
            MIN: 0.144 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.042
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 1.443,
            MIN: 1.443 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.006
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.101,
            MIN: 0.101 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.024
        },
    },
    6: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.202,
            STD: 0.202 * 0.2,
            MIN: 0.0,
            MAX: 0.4
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.519,
            MIN: 0.519 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.012
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 1.010,
            MIN: 1.010 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.010
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 1.371,
            MIN: 1.371 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.006
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.202,
            MIN: 0.202 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.016
        },
    },
    7: {
        0: {
            DISTRIBUTION_DENSITY: NORMAL_DISTRIBUTION,
            MEAN: 0.173,
            STD: 0.173 * 0.2,
            MIN: 0.0,
            MAX: 0.4
        },
        1: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.188,
            MIN: 0.188 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.003
        },
        2: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.721,
            MIN: 0.721 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.009
        },
        3: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.865,
            MIN: 0.865 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.012
        },
        4: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 1.298,
            MIN: 1.298 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.036
        },
        5: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.173,
            MIN: 0.173 * (1-WIDTH_DELTA_FUNCTION/2.0),
            NORMALIZATION_FACTOR: 0.012
        },
        6: {
            DISTRIBUTION_DENSITY: UNIFORM_DISTRIBUTION,
            MEAN: 0.886,
            MIN: 0.886 * (1-WIDTH_DELTA_FUNCTION/2.0),
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
