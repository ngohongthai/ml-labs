from functools import cache
import numpy as np
from icecream import ic 

# =============================================================================
# ===================== HELPER FUNCTIONS ======================================
def _sigmoid(z):
    """
    Compute the sigmoid of z
    """
    return 1.0 / (1.0 + np.exp(-z))

def _relu(z):
    """
    Compute the ReLU of z
    """
    return np.maximum(0, z)

def _sigmoid_derivative(z):
    """
    Compute the derivative of the sigmoid function
    """
    return _sigmoid(z) * (1 - _sigmoid(z))

def _relu_derivative(z):
    """
    Compute the derivative of the ReLU function
    """
    return 1.0 * (z > 0)

def _liner_forward(A, W, b):
    """
    Compute the forward propagation of the linear layer
    """
    return np.dot(W, A) + b

def _liner_activation_forward(A, W, b, activation_type):
    """
    Compute the forward propagation of the linear layer
    """
    caches = []
    if activation_type == 'relu':
        Z = _liner_forward(A, W, b)
        A = _relu(Z)
        caches.append((Z, A))
        return A, caches
    elif activation_type == 'sigmoid':
        Z = _liner_forward(A, W, b)
        A = _sigmoid(Z)
        caches.append((Z, A))
        return A, caches
    else :
        raise ValueError('Invalid activation type')
    

# =============================================================================
# ==================== DEEP NEURAL NETWORK ====================================

# initialize parameters
def _initialize_parameters(layer_dims):
    """
    Initialize the parameters of the model
    """
    np.random.seed(1)
    parameters = {}
    L = len(layer_dims)
    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * 0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
    return parameters

# forward propagation
def _forward_propagation(X, parameters):
    """
    Implement the forward propagation for the model
    """
    caches = []
    A = X
    L = len(parameters) // 2
    for l in range(1, L):
        A_prev = A
        A, cache = _liner_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)], 'relu')
        caches.append(cache)
    AL, cache = _liner_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], 'sigmoid')
    caches.append(cache)
    return AL, caches

# caculate cost

# backward propagation

# update parameters

# deep neural network