from enum import Enum

class ApproximateType(Enum):
    """
    DimensionlessType.

    Defines the type of reduction to dimensionless form.
    """
    NONE = 1
    STOCHASTIC_TELEGRAPH_WAVE = 2
    STOCHASTIC_TELEGRAPH_WAVE_FIXED_SEPARATED_INTERVAL = 3

