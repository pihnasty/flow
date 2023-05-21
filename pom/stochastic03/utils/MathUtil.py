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


