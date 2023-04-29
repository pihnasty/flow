
import sys
import MechanicalCharacteristics.EngineMechanicalCharacteristics as emc
import MechanicalCharacteristics.SpeedTransitionPeriod as stp

# universal .csv
from InitData.inizialize_data import experiments

experiment = experiments["0001"]


engine_echanical_characteristics = emc.EngineMechanicalCharacteristics(experiment)
engine_echanical_characteristics.show()

speed_transition_period = stp.SpeedTransitionPeriod(experiment)
speed_transition_period.show()

sys.exit()
