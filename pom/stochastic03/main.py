import sys
from Graph import DataProcessing as data_processing

file_name = "C:\\A\\Pro\\flow\\pom\\stochastic03\\project\\dataset_2020_ZeYaWuWa\\data.json"
# file_name = "C:\\A\\Pro\\flow\\pom\\stochastic03\\project\\dataset_2018_Buy\\data.json"
# file_name = "C:\\A\\Pro\\flow\\pom\\stochastic03\\project\\dataset_2021_BhAsHuHoEv\\data.json"
# file_name = "C:\\A\\Pro\\flow\\pom\\stochastic03\\project\\dataset_2021_KaKr\\data.json"
data = data_processing.DataProcessing(file_name)
data.data_shows()
sys.exit()
