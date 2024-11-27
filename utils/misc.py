import numpy as np


def softmax(x):

    e_x = np.exp(x - np.max(x))
    return (e_x/e_x.sum()).tolist()
    

def get_model_list():

    return ["MINISTRAL-8B-INSTRUCT", "LLAMA-3.2-3B", "GEMMA-2-2B", "LLAMA-3.1-8B", "GEMMA-2-9B", "GEMMA-2-27B"]