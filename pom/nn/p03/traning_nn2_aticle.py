import copy
import sys
import datetime
import pom.nn.p03.util.FileUtil as file_util
from sklearn.model_selection import train_test_split
import NeuralNet as fnn
from pom.nn.p03.settings.inizialize_data import experiments
import pandas as pd
import torch
import pom.nn.p03.util.common_utils as cu
import util.show as show
import numpy as np

from pom.nn.p03.util import FileUtil

# experiment = experiments["0002"] CMIS 2024
experiment = experiments["0002"]
INPUT_DATA_CATEGORY = 'p03/input/'
OUTPUT_DATA_CATEGORY = 'p03/output/'
fileName = experiment["training_file_name"]

# 1. getting input and output dataset (initial dataset)
input_names = experiment["architecture"]["inputFactors"]["names"]
output_names = experiment["architecture"]["outputFactors"]["names"]
predict_output_names = [sub + '_predict' for sub in output_names]

init_input_df = pd.read_csv(INPUT_DATA_CATEGORY + fileName, sep=";",  dtype=str,  usecols=input_names)
init_output_df = pd.read_csv(INPUT_DATA_CATEGORY + fileName, sep=";",  dtype=str, usecols=output_names)

# Replace "-" values and spaces with NaN
init_input_df = FileUtil.replace_dish_to_mean(init_input_df)
init_output_df = FileUtil.replace_dish_to_mean(init_output_df)

# 2. shuffling the initialization input and output data set and dividing the initialization input and output data set into two data sets: training and test data set.
init_input_df_train, init_input_df_test, init_output_df_train, init_output_df_test = train_test_split(init_input_df,init_output_df,random_state = 51, train_size=0.8, shuffle = False)

# 3. preparing the structure of digitaldata sets for training and testing.

path = OUTPUT_DATA_CATEGORY + experiment["training_file_name"] + "/dataset_train"
file_util.save_to_csv(init_input_df_train, init_output_df_train, path, '/init_train_' + fileName)
file_util.save_to_csv(init_input_df_test, init_output_df_test, path, '/init_test_' + fileName)

# 4. Transforming a sequence of column/domain names (dimention=N) into a matrix in which each row contains the characters of the column/domain name (dimention=MxN),
# where N is the number of column/domain names in the data set; M is the maximum number of characters in the column/domain name.

# 5. Preparing a neural network for training.
# 5.1. creation of a neural network of a given architecture.
# 5.2. determining hyperparameters for neural network training.
# 5.3. initializing weights for a neural network.
# 5.4. casting a dataset for training a neural network into tensor form.
# 5.4. determining the activation function for each layer of the neural network.
model = fnn.NeuralNet(experiment)
lr = experiment["learning"]["lr"]
optimizer = torch.optim.Adam(model.parameters(), lr)

x_train = cu.read_to_tensor(input_names, init_input_df_train)
y_train = cu.read_to_tensor(output_names, init_output_df_train)

x_test = cu.read_to_tensor(input_names, init_input_df_test)
y_test = cu.read_to_tensor(output_names, init_output_df_test)

# 6. neural network training.
# 6.1. defining the loss function for the training and test dataset.
# 6.2. determining the accuracy function for the test set when training a neural network.
# 6.3. determining conditions for interrupting neural network training.
count_epochs = experiment["learning"]["count_epochs"]

loss_values = [0] * round(count_epochs)
test_loss_values = [0] * round(count_epochs)
test_accurancy_values = [0] * round(count_epochs)
epoch_values = [0] * round(count_epochs)

i = 0
#loss = nn.CrossEntropyLoss()
best_test_loss_value = sys.float_info.max
best_test_accuracy_value = 0.0
best_weights = None
best_test_epoch_value = 0

for epoch_index in range(count_epochs):
    optimizer.zero_grad()
    y_pred = model.forward(x_train)
    loss_val = fnn.loss(y_pred, y_train)
    loss_values[i] = loss_val.item()

    y_test_pred = model.forward(x_test)
    test_loss_val = fnn.loss(y_test_pred, y_test)
    test_loss_values[i] = test_loss_val.item()
    test_accurancy = (torch.argmax(y_test_pred, 1)==torch.argmax(y_test, 1)).float().mean()
    test_accurancy_values[i] = float(test_accurancy)
#    if best_test_loss_value > test_loss_val.item() and i > 5000:
    if best_test_accuracy_value < test_accurancy and i > 1000:
        best_test_loss_value = test_loss_val.item()
        best_weights = copy.deepcopy(model.state_dict())
        best_test_accuracy_value = test_accurancy
        best_test_epoch_value = i+1
    epoch_values[i] = i+1 # math.log10(i+1) i+1
    i = i + 1
    loss_val.backward()
    optimizer.step()

# 7. selection of a model with the best predictive performance.
# 7.1. saving model with the best prediction performance for use in the application.
model.load_state_dict(best_weights)

date_suffix = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
path = INPUT_DATA_CATEGORY + "models/"
file_util.make_dir_if_not(path)
torch.save(model.state_dict(), path + "model_" + fileName + '_' + date_suffix + '.pt')

# 8. domain name predictions for a test dataset.
predict_init_output_df_test = model.predict(x_test)
predict_init_output_df_test.columns = predict_output_names
path = OUTPUT_DATA_CATEGORY + experiment["training_file_name"] + "/dataset_train"
column_df = pd.read_csv(INPUT_DATA_CATEGORY + fileName,  sep=";", dtype=str)
file_util.save_to_csv(init_input_df_test.join(init_output_df_test).reset_index(), predict_init_output_df_test, path, '/prediction_' + fileName)

predict_init_output_df_train = model.predict(x_train)
predict_init_output_df_train.columns = predict_output_names

path = OUTPUT_DATA_CATEGORY + experiment["training_file_name"] + "/dataset_train"
column_df = pd.read_csv(INPUT_DATA_CATEGORY + fileName,  sep=";", dtype=str)
file_util.save_to_csv(init_input_df_train.join(init_output_df_train).reset_index(), predict_init_output_df_train, path, '/prediction_train_' + fileName)


# TODO Delete arter testing
#===========================================================
path = INPUT_DATA_CATEGORY
file_util.make_dir_if_not(path)
torch.save(model.state_dict(), path + "/model_02.pt")
#===========================================================

# 9. determining the quality of building a prediction model.
# 9.1. graphical demonstration of prediction results.
output_flows = [epoch_values, loss_values,
                test_loss_values,
                test_accurancy_values]
show.loss(experiment, '/loss', output_flows, 'loss')

print("loss value           : ", loss_values[len(loss_values)-1])
print("best test loss value : ", best_test_loss_value)
print("best test epoch value: ", best_test_epoch_value)
print("best test accuracy   : ", best_test_accuracy_value)

sys.exit()