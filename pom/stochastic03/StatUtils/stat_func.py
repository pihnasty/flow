"""
Basic statistical functions.
"""


def density_values(initial_column_data, number_of_bars):
    """
    This function determines the distribution density of a random variable.
    Based on: https://en.wikipedia.org/wiki/Probability_density_function
    :param initial_column_data: sample of random variables.
    :param number_of_bars: number of intervals for building a histogram.
    :return: the distribution density of a random variable.
    """
    min_value = initial_column_data.min()
    max_value = initial_column_data.max()
    delta = (max_value - min_value) / number_of_bars
    column_data = sorted(initial_column_data)
    element_size = len(column_data)
    index_index = 0
    interval_value = min_value + delta
    x_value = [0] * number_of_bars
    y_value = [0] * number_of_bars
    x_value [0] = interval_value
    for value in enumerate(column_data):
        if value[1] < interval_value:
            y_value[index_index] += 1 / element_size / delta
        else:
            index_index += 1
            if index_index < len(x_value):
                interval_value = interval_value + delta
                x_value[index_index] = interval_value
    return_value = [x_value, y_value]
    return return_value
