import sys
from pom.nn.p03.settings.inizialize_data import experiments
import pandas as pd
import torch
import pom.nn.p03.util.common_utils as cu
import NeuralNet as fnn
import pom.nn.p03.util.FileUtil as file_util
from pom.nn.p03.util import FileUtil

experiment = experiments["0005"]
INPUT_DATA_CATEGORY = 'p03/input/'
OUTPUT_DATA_CATEGORY = 'p03/output/'
fileName = experiment["test_file_name"]

# 1. getting a custom dataset.
input_names = experiment["architecture"]["inputFactors"]["names"]
output_names = experiment["architecture"]["outputFactors"]["names"]
predict_output_names = [sub + '_predict' for sub in output_names]
input_df_test = pd.read_csv(INPUT_DATA_CATEGORY + fileName, usecols=input_names, sep=";",  dtype=str)
output_df_test = pd.read_csv(INPUT_DATA_CATEGORY + fileName, usecols=output_names, sep=";",  dtype=str)

# 4. Transforming a sequence of column/domain names (dimention=N) into a matrix in which each row contains the characters of the column/domain name (dimention=MxN),
# where N is the number of column/domain names in the data set; M is the maximum number of characters in the column/domain name.

# 5. Preparing a neural network for training.
# 5.1. creation of a neural network of a given architecture.
# 5.2. loading a saved model to predict a domain name.
# 5.4. casting a dataset for training a neural network into tensor form.
model = fnn.NeuralNet(experiment)
model_name = experiment['model_name']
model_state_distinct = torch.load(INPUT_DATA_CATEGORY + model_name)
model.load_state_dict(model_state_distinct)
# Replace "-" values and spaces with NaN
input_df_test = FileUtil.replace_dish_to_mean(input_df_test)
output_df_test = FileUtil.replace_dish_to_mean(output_df_test)
x_test = cu.read_to_tensor(input_names, input_df_test)
y_test = cu.read_to_tensor(output_names, output_df_test)

# 6. domain name predictions for a custom dataset.
predict_output_df = model.predict(x_test)
predict_output_df.columns = predict_output_names
column_df = pd.read_csv(INPUT_DATA_CATEGORY + fileName,  sep=";", dtype=str)
path = OUTPUT_DATA_CATEGORY + experiment["training_file_name"] + '/predict/'
file_util.save_to_csv(column_df, predict_output_df, path, '/prediction_' + fileName)

# 9. determining the quality of a prediction.
y_test_pred = model.forward(x_test)
test_loss_val = fnn.loss(y_test_pred, y_test)
test_accurancy = (torch.argmax(y_test_pred, 1)==torch.argmax(y_test, 1)).float().mean()

print("loss value           : ", test_loss_val)
print("test accuracy        : ", test_accurancy)

sys.exit()