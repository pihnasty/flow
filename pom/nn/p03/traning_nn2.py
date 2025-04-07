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

from pom.nn.p03.util import FileUtil

# experiment = experiments["0002"] CMIS 2024
experiment = experiments["0004"]
INPUT_DATA_CATEGORY = 'input/'
OUTPUT_DATA_CATEGORY = 'output/'
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
init_input_df_train, init_input_df_test, init_output_df_train, init_output_df_test = train_test_split(init_input_df,init_output_df, random_state = 100, train_size=0.8, shuffle = True)
# 1-61 2-50 3-61 4-50 5-50 6-50 7-55 8-55 9-67 10-50 11-44 12-50 13-72 14-50    дублирования процентов
# 1-61 2-33 3-67 4-56 5-38 6-39 7-44 8-44 9-50 10-55 11-44 12-44 13-61 14-27 15-55 16-61 17-44 18-50 19-55 20-50 21-50 22-67!!!  23-55 24-55 25-50 26-55 27-55 28-44 29-61 30-55
# continue 31-61 32-55 33-61 34-44 35-50 36-38 37-61 38-44 39-44 40-67 41=55 42-33 43-44 45-38 46-44 47-50 48-61 49-33 50-38 51-44 52-50 53-61 54-50 55-72!!! 56-55 57-56 58-72 59-55 60-50 61-55 62-50 63-56 64-50 65-56 66-44 67-44 68-44 69-50 70-38
# 71-50 72-44 73-55 74-50 75-33 76-50 77-67 78-44 79-28 80-38 81-61 82-44 83-44 85-50 86-50 87-50 88-55 89-50 90-61 91-50 92-61 93-61 94-44 95-44 96-50 97-28 98-22 99-50 100-67

# 1-44 2-50 3-44 4-61 5-44 6-44 7-55 8-44 9-44 10-44 11-44 12-38 13-50 14-38 15-38 16-55 17-38 17-55 18-55 19-50 20-67 21-38 22-61 23-22 24-50 25-33 26-28 27-50 28-38 29-44 30-39 31-50
# 32-44 33-56 34-44 35-50 36-55 37-44 38-22 39-44 40-33 41-50 42-50 43-44 44-55 45-38 46-33 47-55 48-44 49-50 50-44 51-50 52-50 53-44 54-50 55-50 56-55 57-33 58-44 59-50 60-38 61-50 62-44 63-55 64-44
# 65-67 66-50 67-44 68-61 69-44 70-38 71-38 72-38 73-33 74-50 75-56 76-61 77-50 78-50 79-61 80-44 81-50 82-61 83-61 84-38 85-61 86-33 87-44 88-33 89-50 90-50 91-55 92-55 93-38 94-50 95-38 96-50 97-44 98-44 99-33 100-44

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