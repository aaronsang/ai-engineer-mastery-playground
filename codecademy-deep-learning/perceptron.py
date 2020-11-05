"""
This module creates a simple perceptron from scratch
"""

# Create the perceptron object
class Perceptron:
    def __init__(self, num_inputs=2, weights=[2,1]):
        self.num_inputs = num_inputs
        self.weights = weights

    def weighted_sum(self, inputs):
        weighted_sum = 0
        # create variable to store weighted sum
        for i in range(self.num_inputs):
            weighted_sum += inputs[i] * self.weights[i]
        return weighted_sum

    def activation(self, weighted_sum):
        if weighted_sum >= 0:
            return 1
        return -1
    def training(self, training_set):
        for inputs in training_set:
            prediction = self.activation(self.weighted_sum))
            actual = training_set[inputs]
            error = actual - prediction

cool_perceptron = Perceptron()
print(cool_perceptron.activation(52))

