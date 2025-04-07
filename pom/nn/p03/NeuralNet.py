import pandas as pd
import torch


class NeuralNet(torch.nn.Module):
    def __init__(self, parameters):
        super(NeuralNet, self).__init__()
        architecture = parameters['architecture']
        seed = parameters["learning"]["seed"]
        input_nodes_count = len(architecture["inputFactors"]["names"])
        output_nodes_count = len(architecture["outputFactors"]["names"])
        hiddenLayers = architecture["hiddenLayers"]
        self.layer_count_with_input_output = 2 + len(architecture["hiddenLayers"]);
        self.fc = [0] * round(self.layer_count_with_input_output-1)
        self.act = [0] * round(self.layer_count_with_input_output-1)

        self.fc = [0] * round(self.layer_count_with_input_output-1)
        self.act = [0] * round(self.layer_count_with_input_output-1)

        for i in range(self.layer_count_with_input_output - 1):
            if i == 0:
                self.fc[i] = torch.nn.Linear(input_nodes_count, hiddenLayers[i + 1]["count-node"])
                self.act[i] = self.get_activation_function(architecture['inputFactors']["activation-function"])
                self.weight_init(self.fc[i], architecture['inputFactors']["weight-init-method"], seed )
            if i == self.layer_count_with_input_output - 2:
                self.fc[i] = torch.nn.Linear(hiddenLayers[i]["count-node"], output_nodes_count)
                self.act[i] = self.get_activation_function(hiddenLayers[i]["activation-function"])
                self.weight_init(self.fc[i], hiddenLayers[i]["weight-init-method"], seed )
            if 0< i and i < self.layer_count_with_input_output - 2:
                self.fc[i] = torch.nn.Linear(hiddenLayers[i]["count-node"], hiddenLayers[i +1]["count-node"] )
                self.act[i] = self.get_activation_function(hiddenLayers[i]["activation-function"])
                self.weight_init(self.fc[i], hiddenLayers[i]["weight-init-method"], seed )
        self.output_act = self.get_activation_function(architecture["outputFactors"]["activation-function"])

        # self.f = torch.nn.Linear(len(input_names), 15)
        # # https://www.geeksforgeeks.org/initialize-weights-in-pytorch/
        # # https://discuss.pytorch.org/t/random-initialization-of-weights-with-torch-nn-init/79831

        if self.layer_count_with_input_output == 3:
            self.init_1_hidden()
        if self.layer_count_with_input_output == 4:
            self.init_2_hidden()
        if self.layer_count_with_input_output == 5:
            self.init_3_hidden()
        if self.layer_count_with_input_output == 6:
            self.init_4_hidden()

    def forward(self, x):
        if self.layer_count_with_input_output == 3:
            x = self.forward_1_hidden(x)
        if self.layer_count_with_input_output == 4:
            x = self.forward_2_hidden(x)
        if self.layer_count_with_input_output == 5:
            x = self.forward_3_hidden(x)
        if self.layer_count_with_input_output == 6:
            x = self.forward_4_hidden(x)
        if(self.output_act != ""):
            x = self.output_act(x)
        return x


    # This code runs only in python 3.10 or above versions
    def get_activation_function(self, function_name):
        if function_name == "Sigmoid":
            return torch.nn.Sigmoid()
        elif function_name == "ReLU":
            return torch.nn.ReLU()
        elif function_name == "Softmax":
            return torch.nn.Softmax(dim=1)
        else:
            return ""

    def weight_init(self, layer, method, seed):
        if method == "constant_":
            torch.nn.init.constant_(layer.weight, 0.5)
            torch.nn.init.constant_(layer.bias, 0)
        elif method == "normal_":
            self.init_with_seed(seed)
            torch.nn.init.normal_( layer.weight, mean=0, std=1)
            self.init_with_seed(seed)
            torch.nn.init.normal_(layer.bias, mean=0, std=1)
        else:
            self.init_with_seed(seed)
            torch.nn.init.uniform_(layer.weight, 0.5)
            self.init_with_seed(seed)
            torch.nn.init.uniform_(layer.bias, 0)

    def init_with_seed(self, seed):
        if(seed is not 0):
            torch.manual_seed(seed)
#--------------------------------------------
    def init_1_hidden(self):
        self.fc1 = self.fc[0]
        self.act1 = self.act[0]
        self.fc2 = self.fc[1]

    
    def forward_1_hidden(self, x):
        x = self.fc1(x)
        x = self.act1(x)
        x = self.fc2(x)
        return x
    #--------------------------------------------
    def init_2_hidden(self):
        self.init_1_hidden()
        self.act2 = self.act[1]
        self.fc3 = self.fc[2]

    def forward_2_hidden(self, x):
        x = self.forward_1_hidden(x)
        x = self.act2(x)
        x = self.fc3(x)
        return x
    #--------------------------------------------
    def init_3_hidden(self):
        self.init_2_hidden()
        self.act3 = self.act[2]
        self.fc4 = self.fc[3]

    def forward_3_hidden(self, x):
        x = self.forward_2_hidden(x)
        x = self.act3(x)
        x = self.fc4(x)
        return x
    #--------------------------------------------
    def init_4_hidden(self):
        self.init_3_hidden()
        self.act4 = self.act[3]
        self.fc5 = self.fc[4]

    def forward_4_hidden(self, x):
        x = self.forward_3_hidden(x)
        x = self.act4(x)
        x = self.fc5(x)
        return x

    def predict(self, x):
        y_pred = self.forward(x)
        return pd.DataFrame(y_pred.detach().numpy())

def loss(pred, target):
    """
    the loss function for the training dataset.
    :param pred: predicted value.
    :param target: expected value.
    :return: the value of the loss function.
    """
    squares = (pred - target) ** 2
    return squares.mean()

