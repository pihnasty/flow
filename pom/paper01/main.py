"""Main module to create the plots of harmonics
to analyze the deterministic input flow
"""

import sys
import MechanicalCharacteristics.EngineMechanicalCharacteristics as emc
import dflow.d_flow_analysis as dfh

# universal .csv
from InitData.initialize_data import experiments


def main_emc():
    """Initial framework
    :return:
    """
    experiment = experiments["0001"]
    engine = emc.EngineMechanicalCharacteristics(experiment)
    engine.show()


def main_dfh():
    """Creating  the plots of harmonics
    of the deterministic input flow
    :return:
    """
    experiment = experiments["0002"]
    engine = dfh.DeterministicFlowHarmonics(experiment)
    # print(engine.read_fourier_coefficients())
    engine.show()


if __name__ == "__main__":
    main_dfh()
    sys.exit()
