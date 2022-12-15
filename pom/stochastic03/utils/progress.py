"""
This module includes a function that displays progress bar in console.
Based on:
https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
"""

import sys


def progress(count, total, suffix=''):
    """
    Call in a loop to create terminal progress bar.
    :param count:   - Required: current iteration (Int)
    :param total:   - Required: total iterations (Int)
    :param suffix:  - Optional: arbitrary suffix (default '')
    :return:
    """
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar_ = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write(f'\r[{bar_}] {percents}% {suffix}')
    sys.stdout.flush()  # As suggested by Rom Ruben
