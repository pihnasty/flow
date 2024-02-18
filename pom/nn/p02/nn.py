# https://github.com/KaluginaMarina/small_neural_network
# https://www.youtube.com/watch?v=khvO24NWZsc
# https://www.youtube.com/watch?v=TVFOjP0FNVQ
# https://www.youtube.com/watch?v=49hbIKRI5EE
import sys
import FlowNeuralNet as fnn
# universal .csv
from pom.nn.p02.init_data.inizialize_data import experiments
import pandas as pd
import torch
import pom.nn.p02.util.common_utils as cu


import util.show as show

def predict(net, x, y):
    y_pred = net.forward(x)

def loss(pred, target):
    squares = (pred - target) ** 2
    return squares.mean()


experiment = experiments["0003"]

RESULT_DATA = 'resultData/'
DATA_CATEGORY = 'raw_data/'

fileName = experiment["file_name"]
df = pd.read_csv(DATA_CATEGORY + fileName, sep=";", decimal='.')
input_names = experiment['architecture']['inputFactors']['names']
output_names = experiment['architecture']['outputFactors']['names']

x_train = cu.read_to_tensor(input_names, df)
y_train = cu.read_to_tensor(output_names, df)

flow_neural_net = fnn.FlowNeuralNet(experiment['architecture'])

optimizer = torch.optim.Adam(flow_neural_net.parameters(), lr=0.01)

count_epochs = experiment["learning"]["count_epochs"]
loss_values = [0] * round(count_epochs  )
epoch_values = [0] * round(count_epochs)
i = 0
for epoch_index in range(count_epochs):
    optimizer.zero_grad()
    y_pred = flow_neural_net.forward(x_train)
    loss_val = loss(y_pred, y_train)
    loss_values[i] = loss_val.item()
    epoch_values[i] = i+1 # math.log10(i+1)
    i = i + 1
    loss_val.backward()
    optimizer.step()

print(loss_values[i-1])


# output_flows = [df['   0.NN   '].values, df[' 7.output '].values, cu.tensor_to_array_transpose(y_pred)[0]]
# show.output_flow(experiment, '/output_flow', output_flows, 'output_7_')
# output_flows = [df['   0.NN   '].values, df[' 8.output '].values, cu.tensor_to_array_transpose(y_pred)[1]]
# show.output_flow(experiment, '/output_flow', output_flows, 'output_8_')

output_flows = [epoch_values, loss_values, loss_values]
show.loss(experiment, '/loss', output_flows, 'flow_line')

predict(flow_neural_net, x_train, y_train) ,
sys.exit()