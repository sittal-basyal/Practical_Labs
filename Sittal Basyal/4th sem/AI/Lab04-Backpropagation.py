"""
Lab 04 - Implementation of Backpropagation Algorithm

A simple feed-forward neural network (1 hidden layer) trained using
the backpropagation algorithm, implemented from scratch using NumPy.
Demonstrated on the XOR problem (a classic non-linearly separable
problem that requires backpropagation / hidden layers to solve).
"""
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


# XOR data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

# Initialize weights
np.random.seed(1)
W1 = np.random.uniform(-1, 1, (2, 4))
W2 = np.random.uniform(-1, 1, (4, 1))
b1 = np.zeros((1, 4))
b2 = np.zeros((1, 1))

lr = 0.5

# Backpropagation
for epoch in range(10000):

    # Forward propagation
    h = sigmoid(X @ W1 + b1)
    output = sigmoid(h @ W2 + b2)

    # Backpropagation
    error = y - output
    d_output = error * sigmoid_derivative(output)
    d_hidden = (d_output @ W2.T) * sigmoid_derivative(h)

    # Update weights
    W2 += lr * h.T @ d_output
    b2 += lr * np.sum(d_output, axis=0, keepdims=True)
    W1 += lr * X.T @ d_hidden
    b1 += lr * np.sum(d_hidden, axis=0, keepdims=True)


# Results
print("XOR using Backpropagation:")
for x, actual, pred in zip(X, y, output):
    print(x, "Actual:", actual[0],
          "Predicted:", round(pred[0]))