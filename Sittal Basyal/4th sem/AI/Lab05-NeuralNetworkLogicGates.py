"""
Lab 05 - Implementation of Neural Networks for realization of Logic Gates

Part 1: A single-layer Perceptron implements linearly separable
         gates: AND, OR, NOT, NAND, NOR.
Part 2: A small Multi-Layer Perceptron (with backpropagation, reusing
         the same idea as Lab 4) implements XOR, which a single
         perceptron CANNOT represent (not linearly separable).
"""
import numpy as np

class Perceptron:
    def __init__(self, lr=0.1, epochs=20):
        self.weights = np.zeros(2)
        self.bias = 0
        self.lr = lr
        self.epochs = epochs

    def predict(self, x):
        return 1 if np.dot(self.weights, x) + self.bias >= 0 else 0

    def train(self, X, y):
        for _ in range(self.epochs):
            for x, target in zip(X, y):
                error = target - self.predict(x)
                self.weights += self.lr * error * x
                self.bias += self.lr * error


X = np.array([[0,0], [0,1], [1,0], [1,1]])

# AND
and_y = [0, 0, 0, 1]
and_model = Perceptron()
and_model.train(X, and_y)

print("AND Gate")
for x in X:
    print(x, "->", and_model.predict(x))

# OR
or_y = [0, 1, 1, 1]
or_model = Perceptron()
or_model.train(X, or_y)

print("\nOR Gate")
for x in X:
    print(x, "->", or_model.predict(x))