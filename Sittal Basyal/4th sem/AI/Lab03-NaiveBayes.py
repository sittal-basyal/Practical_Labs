"""
Lab 03 - Implementation of Naive Bayes Classifier

We implement the Gaussian Naive Bayes algorithm from scratch
(no ML library used for the core algorithm) and test it on the
classic Iris flower dataset.

Naive Bayes uses Bayes' Theorem:
    P(class | features) proportional_to P(class) * P(features | class)
with the "naive" assumption that features are conditionally
independent given the class.
"""
import math
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dataset
X, y = load_iris(return_X_y=True)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train Gaussian Naive Bayes
classes = set(y_train)
model = {}

for c in classes:
    samples = [X_train[i] for i in range(len(X_train)) if y_train[i] == c]

    means = []
    vars = []

    for j in range(X_train.shape[1]):
        values = [x[j] for x in samples]
        mean = sum(values) / len(values)
        var = sum((v - mean) ** 2 for v in values) / len(values)

        means.append(mean)
        vars.append(max(var, 1e-6))

    prior = len(samples) / len(X_train)
    model[c] = (prior, means, vars)


# Prediction
def predict(x):
    scores = {}

    for c, (prior, means, vars) in model.items():
        score = math.log(prior)

        for value, mean, var in zip(x, means, vars):
            probability = (
                math.exp(-(value - mean) ** 2 / (2 * var))
                / math.sqrt(2 * math.pi * var)
            )
            score += math.log(probability + 1e-12)

        scores[c] = score

    return max(scores, key=scores.get)


# Test
predictions = [predict(x) for x in X_test]

accuracy = sum(
    p == actual for p, actual in zip(predictions, y_test)
) / len(y_test)

print("Gaussian Naive Bayes")
print("Accuracy:", accuracy * 100, "%")