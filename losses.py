import numpy as np 


def mse(y_true, y_pred):
    diff = y_true - y_pred
    return np.mean(diff * diff)


def mse_derivative(y_true, y_pred):
    return 2* (y_pred-y_true) / np.size(y_true)
