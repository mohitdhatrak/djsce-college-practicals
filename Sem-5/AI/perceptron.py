import numpy as np

# Define input vectors X1, X2, X3
X1 = np.array([1, -2, 0, -1])
X2 = np.array([0, 1.5, -0.5, -1])
X3 = np.array([-1, 1, 0.5, -1])
X = [X1, X2, X3]

# Initialize weight vector W and bias term b
W = np.array([1, -1, 0, 0.5])

# Define target outputs (desired classes) for the training examples
d = [-1, -1, 1]

# Set learning rate (step size)
c = 0.1

# number of training epochs
epochs = 1  # algorithm goes through the entire training dataset only once during the training process

for i in range(epochs):
    # Iterate through each training example
    for j in range(len(X)):
        # Compute the net input to the perceptron, does dot product between the vectors
        net = np.dot(X[j], W)

        # as per sign or step activation function
        if net <= -1:
            output = -1
        elif net == 0:
            output = 0
        elif net >= 1:
            output = 1

        # as per perceptron formula
        error = d[j] - output
        dW = c * error * X[j]
        W += dW

        print(f"Weight after iteration {j + 1}: [", end=" ")
        for k in range(len(W)):
            print(f"{W[k]:.1f}", end=" ")
        print("]")

print("Final Weight after", epochs, "epochs: [", end=" ")
for i in range(len(W)):
    print(f"{W[i]:.1f}", end=" ")
print("]")
