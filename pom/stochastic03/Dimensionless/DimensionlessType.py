from enum import Enum

class DimensionlessType(Enum):
    """
    DimensionlessType.

    Defines the type of reduction to dimensionless form.
    """
    MEAN_TIME_M1_1 = 1  # TIME_M1_1 -> min = - std;    max = +std.
    STD_TIME_M1_1 = 2   # TIME_M1_1 -> min = - std;    max = +std.
