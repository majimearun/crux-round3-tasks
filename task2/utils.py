import numpy as np


def initialize_parameters(n, m, method="xavier"):
    """
    function that initializes layer with random weights (based on formula/method chosen) and 0 biases

    reference used: https://machinelearningmastery.com/weight-initialization-for-deep-learning-neural-networks/

    arguments:
    n -- number of neurons in the input layer
    m -- number of neurons in the next layer
    method -- formula/method for initializing weghts (options: xavier, norm_xavier, he)

    returns:
    parameters -- a dictionary containing w (weights) and b (biases)
    """

    parameters = {"w":[], "b":[]}

    if method == "xavier":
        # weight = U [-(1/sqrt(n)), 1/sqrt(n)]
        parameters["w"] = np.random.randn(m, n) / (np.sqrt(n))

    elif method == "norm_xavier":
        # weight = U [-(sqrt(6)/sqrt(n + m)), sqrt(6)/sqrt(n + m)]
        parameters["w"] = np.random.randn(m, n) / (np.sqrt(6/(n + m)))
    
    elif method == "he":
        # weight = U [-(sqrt(2/n)), sqrt(2/n)]
        parameters["w"] = np.random.randn(m, n) / (np.sqrt(2/(n)))

    parameters["b"] = np.zeros((m, 1))

    return parameters



def binary_cross_entropy(y, z, from_logits=False):
    """
    function that computes the binary cross-entropy cost function of our network, the same way Tensorflow and Keras does. 

    reference used: https://rafayak.medium.com/how-do-tensorflow-and-keras-implement-binary-classification-and-the-binary-cross-entropy-function-e9413826da7

    formula: (1/m) * sum(max(z,0) - z*y + log(1+e^(- |z|)))

    arguments:
    y -- labels of data
    prob -- probabilities from sigmoid function
    from_logits -- flag to check if logits are being provided or not (default = False)

    returns:
    cost -- the binary cross entropy cost
    dz -- derivative of cost w.r.t last layer
    """

    if not(from_logits):
        minimum = 1e-07   # 0.000001 
        maximum = 1 - minimum # 0.9999999

        z = np.clip(z, a_min=minimum, a_max=maximum)
        z = np.log(z / (1 - z))

    m = y.shape[1] # number of labels, as shape of y will be is (1,n)
    cost = (1/m) * np.sum(np.maximum(z, 0) - z*y + np.log(1+ np.exp(- np.abs(z))))
    dz = (1/m) * ((1/(1+np.exp(- z))) - y)

    return cost, dz
