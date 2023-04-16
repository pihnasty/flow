
import sys
import MechanicalCharacteristics.EngineMechanicalCharacteristics as emc


# universal .csv
from InitData.inizialize_data import experiments

experiment = experiments["0001"]


engine = emc.EngineMechanicalCharacteristics(experiment)
engine.show()

sys.exit()
