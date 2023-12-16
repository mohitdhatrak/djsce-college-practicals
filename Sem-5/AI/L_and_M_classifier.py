import numpy as np

# This is a 5x4 matrix which resembles an L
# 10000
# 10000
# 10000
# 11111

# This is a 5x4 matrix which represents an M
# 10001
# 11011
# 10101
# 10001

input_size = 5

# Define input vectors L and M
# L = np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1])  # L
# M = np.array([1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1])  # M
L = np.array([1, 0, 0, 0, 0])  # L
M = np.array([1, 0, 0, 0, 1])  # M

X = [L, M]

# Initialize weight vector W
# W = np.array([0.5, -0.2, 0.8, -0.3, 0.2, 0.6, -0.4, 0.1, 0.7, -0.5, 0.3, -0.6, 0.4, -0.7, 0.9, -0.1, -0.8, 0.2, 0.5, -0.9])
W = np.random.rand(input_size)

# Define target outputs (desired classes) for the training examples
d = [-1, 1]  # L -> -1, M -> 1

# Set learning rate (step size)
c = 0.1

# number of training epochs
epochs = 2  # algorithm goes through the entire training dataset only once during the training process

for i in range(epochs):
    print(f"Epoch {i + 1}: ")
    # Iterate through each training example
    for j in range(len(X)):
        # Compute the net input to the perceptron, does dot product between the vectors
        net = np.dot(X[j], W)

        # as per sign or step activation function
        if net < 0:
            output = -1
        elif net == 0:
            output = 0
        elif net > 0:
            output = 1

        # as per perceptron formula ->
        # dW = c (d - o) * xi
        # W new = W old + dW
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
