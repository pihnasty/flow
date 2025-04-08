import math
from copy import deepcopy

from common_utils.flow_constants import TIME, FLOW


def search(f, f_value, i_left, i_reight):
    if f_value -  f[i_left] < 0:
        return -1
    if f_value - f[i_reight] > 0:
        return -1

    midPoint= round((i_left + i_reight) / 2)
    if i_left == i_reight:
        return midPoint
    if i_left +1 == i_reight:
        if (f_value -  f[i_left]) > (f[i_reight] - f_value):
            return i_reight
        else:
            return i_left

    if f_value > f[midPoint]:
        return search(f, f_value, midPoint, i_reight)
    else:
        return search(f, f_value, i_left, midPoint )


def H(x):
    if x >= 0:
        return 1.0
    else:
        return 0.0

# ================= numeric way to calculate the fourier coefficients ==================================================
def numeric_calculate_fourier_series(y, x, number_of_harmonics):
    """
       Compute the cosine and sine harmonic values for the Fourier series expansion of a given dataset.
           y = a0/2 + ai * cos + bi * sin

       This method calculates the Fourier coefficients for the specified number of harmonics
       using the provided x and y data points.

       Parameters:
       -----------
       x : list of float
           The x-coordinates of the data points.
       y : list of float
           The y-coordinates of the data points corresponding to the x-coordinates.
       number_of_harmonics : int
           The number of harmonics to compute.

       Returns:
       --------
       cos_harmonic_values : list of float
           The cosine harmonic values for each harmonic.
       sin_harmonic_values : list of float
           The sine harmonic values for each harmonic.

       Notes:
       ------
       - The method assumes that the input lists x and y have the same length.
       - The x-coordinates are used to compute the intervals and the range over which
         the Fourier series is calculated.
       - The y-coordinates represent the function values at the corresponding x-coordinates.

       Example:
       --------
       >>> x = [0, 1, 2, 3, 4, 5]
       >>> y = [0, 1, 0, -1, 0, 1]
       >>> number_of_harmonics = 3
       >>> cos_harmonics, sin_harmonics = compute_fourier_series(x, y, number_of_harmonics)
       >>> print(cos_harmonics)
       [some_values]
       >>> print(sin_harmonics)
       [some_values]
       :type y: object
       """
    start_x = x.keys().start
    elements_size = len(x)
    x_min = min(x)
    l = max(x) - x_min
    z = 2 * math.pi / l
    delta_x = l / elements_size
    cos_harmonic_values = [0.0] * number_of_harmonics
    sin_harmonic_values = [0.0] * number_of_harmonics
    for num in range(number_of_harmonics):
        sin_harmonic_value = 0.0
        cos_harmonic_value = 0.0
        for n in range(start_x, elements_size + start_x):
            x_ = x[n]
            if num == 0:
                cos_harmonic_value = cos_harmonic_value + 1.0 / l * y[n] * delta_x
            else:
                cos_harmonic_value = cos_harmonic_value + 2.0 / l * y[n] * math.cos(z * num * (x_ - x_min)) * delta_x
                sin_harmonic_value = sin_harmonic_value + 2.0 / l * y[n] * math.sin(z * num * (x_ - x_min)) * delta_x
        cos_harmonic_values[num] = cos_harmonic_value
        sin_harmonic_values[num] = sin_harmonic_value
    return cos_harmonic_values, sin_harmonic_values

# ================= numeric way to calculate the function values =======================================================
def calculate_function(dim_parts, cos_harmonic_values, sin_harmonic_values):
    temp_dim_parts = deepcopy(dim_parts)
    for n in range(len(dim_parts)):
        x_s = temp_dim_parts[n][TIME]
        x_min = min(x_s)
        l = max(x_s) - x_min
        z = 2 * math.pi / l
        start_tau = temp_dim_parts[n][TIME].keys().start
        for i in range(start_tau, len(x_s) + start_tau):
            flow_value = 0.0
            x = x_s[i]
            for k in range(len(cos_harmonic_values[n])):
                flow_value = (flow_value + cos_harmonic_values[n][k] * math.cos(z * k * (x - x_min))
                                  + sin_harmonic_values[n][k] * math.sin(z * k * (x - x_min)))
            temp_dim_parts[n][FLOW][i] = flow_value
    return temp_dim_parts

def calculate_function_by_mean_harmonic_values(dim_parts, cos_harmonic_values, sin_harmonic_values):
    temp_dim_parts = deepcopy(dim_parts)
    for n in range(len(dim_parts)):
        x_s = temp_dim_parts[n][TIME]
        x_min = min(x_s)
        l = max(x_s) - x_min
        z = 2 * math.pi / l
        start_tau = temp_dim_parts[n][TIME].keys().start
        for i in range(start_tau, len(x_s) + start_tau):
            flow_value = 0.0
            x = x_s[i]
            for k in range(len(cos_harmonic_values)):
                flow_value = (flow_value + cos_harmonic_values[k] * math.cos(z * k * (x - x_min))
                              + sin_harmonic_values[k] * math.sin(z * k * (x - x_min)))
            temp_dim_parts[n][FLOW][i] = flow_value
    return temp_dim_parts