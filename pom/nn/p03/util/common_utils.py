import numpy as np
import torch
def read_to_tensor(input_names, df):
    py_list = []
    for input_name in input_names:
        py_list.append(df[input_name])
    return torch.FloatTensor(np.array(py_list, dtype=np.float16).transpose())

def tensor_to_array_transpose(tensor):
    return tensor.detach().numpy().transpose()

