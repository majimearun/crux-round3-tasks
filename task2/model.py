import numpy as np
from utils import initialize_parameters, binary_cross_entropy

# references used:
# 1. https://www.analyticsvidhya.com/blog/2021/04/activation-functions-and-their-derivatives-a-quick-complete-guide/


class Layer:
    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.type = "abstract"


class Linear(Layer):
    def __init__(self, input_shape, n_out, method):
        """
        input_shape -- input shape of Data/Activations
        n_out -- number of neurons in layer
        method -- initialization formula/method for weight parameters
        """
        Layer.__init__(self, input_shape)
        self.parameters = initialize_parameters(input_shape[0], n_out, method)
        self.z = np.zeros((self.parameters["w"].shape[0], input_shape[1]))
        self.type = "linear"

    def forward(self, prev):
        """
        method that performs forward propagation

        arguments:
        prev -- input coming from the previous layer
        """

        self.prev = prev
        self.z = np.dot(self.parameters["w"], self.prev) + self.parameters["b"]

    def backward(self, grad):
        """
        method that performs backward propagation

        arguments:
        grad -- gradient of the upper/next/higher layer
        """

        # derivative of cost w.r.t W
        self.dw = np.dot(grad, self.prev.T)

        # derivative of cost w.r.t b
        self.db = np.sum(grad, axis=1, keepdims=True)

        # derivative of cost w.r.t prev
        self.dprev = np.dot(self.parameters["w"].T, grad)

    def update_params(self, learning_rate=0.01):
        """
        method that helps implement the gradient descent algorithm to update weights and biases in a stepwise fashion

        arguments:
        learning_rate -- learning rate of the network (default = 0.01)
        """

        self.parameters["w"] = self.parameters["w"] - learning_rate * self.dw
        self.parameters["b"] = self.parameters["b"] - learning_rate * self.db


class Sigmoid(Layer):
    def __init__(self, input_shape):
        """
        input_shape -- shape of input to the layer
        """
        Layer.__init__(self, input_shape)
        self.type = "sigmoid"

        self.sig = np.zeros(self.input_shape)

    def forward(self, z):
        """
        function that performs forward propagation (through activations)
        arguments:
        z: input from previous (linear) layer
        """
        self.sig = 1 / (1 + np.exp(-z))

    def backward(self, grad):
        """
        function that performs backward propagation (through activations)

        arguments:
        grad -- gradient of the upper/next/higher (activation) layer
        """
        # derivative of sigmoid = f(x)*(1-f(x))
        self.dz = grad * self.sig * (1 - self.sig)



class SequentialNN:
    def __init__(self):
        self.layers = []
        self.costs = []

    def add(self, layer: Layer):
        """
        method that adds a layer to the model (similar to keras sequential)
        """
        self.layers.append(layer)

    def compile(self, cost_func, epochs, learning_rate):
        self.cost_func = cost_func
        self.epochs = epochs
        self.learning_rate = learning_rate

    def fit(self, X, y):
        """
        method that fits the model to the data using the gradient descent algorithm`

        arguments:
        X -- input data
        y -- target data
        """

        for epoch in range(self.epochs):
            prev_lin = np.zeros((1, X.shape[0]))
            prev_activation = X

            # forward propagation
            for layer in self.layers:
                if layer.type == "linear":
                    layer.forward(prev_activation)
                    prev_lin = layer.z
                elif layer.type == "sigmoid":
                    layer.forward(prev_lin)
                    prev_activation = layer.sig

            cost, _dz = self.cost_func(y=y, z=prev_lin, from_logits=True)

            if (epoch % 100) == 0 or epoch == self.epochs - 1:
                print(f"epoch {epoch}: cost = {cost}")
                self.costs.append(cost)

            # backward propagation
            prev_lin_der = _dz
            prev_activation_der = np.zeros((1, _dz.shape[0]))
            for layer in self.layers[-2::-1]:
                if layer.type == "linear":
                    layer.backward(prev_lin_der)
                    prev_activation_der = layer.dprev
                elif layer.type == "sigmoid":
                    layer.backward(prev_activation_der)
                    prev_lin_der = layer.dz

            # update parameters
            for layer in self.layers[::-1]:
                if layer.type == "linear":
                    layer.update_params(learning_rate=self.learning_rate)

    def predict(self, X, thresh=0.5):
        """
        method that predicts the output computed by the final model on the guven test set

        rounds the output to binary values: 1 or 0, depending on outputted probability by the model, and the threshold set (0.5)

        arguments:
        X -- input data (X_test while evaluating and in general any scaled input to predict)
        thresh -- threshold for rounding the output (default = 0.5)

        returns:
        pred -- predicted output (an array of 1s and 0s)

        """
        prev_lin = None
        prev_activation = X

        pred = np.zeros((1, X.shape[1]))

        for layer in self.layers:
            if layer.type == "linear":
                layer.forward(prev_activation)
                prev_lin = layer.z
            elif layer.type == "sigmoid":
                layer.forward(prev_lin)
                prev_activation = layer.sig

        probabilities = prev_activation

        for i in range(0, probabilities.shape[1]):
            if probabilities[0, i] >= thresh:
                pred[0, i] = 1
            else:
                pred[0, i] = 0
        return pred

