import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        # Initialize weights and biases
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))
        self.learning_rate = learning_rate

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def forward(self, inputs):
        # Forward pass
        self.hidden_inputs = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_outputs = self.sigmoid(self.hidden_inputs)
        self.final_inputs = np.dot(self.hidden_outputs, self.weights_hidden_output) + self.bias_output
        self.final_outputs = self.softmax(self.final_inputs)

        return self.final_outputs

    def backward(self, inputs, targets):
        # Backward pass
        output_error = targets - self.final_outputs
        hidden_error = np.dot(output_error, self.weights_hidden_output.T)
        
        # Update weights and biases
        self.weights_hidden_output += self.learning_rate * np.dot(self.hidden_outputs.T, output_error)
        self.bias_output += self.learning_rate * np.sum(output_error, axis=0, keepdims=True)
        self.weights_input_hidden += self.learning_rate * np.dot(inputs.T, hidden_error * self.hidden_outputs * (1 - self.hidden_outputs))
        self.bias_hidden += self.learning_rate * np.sum(hidden_error * self.hidden_outputs * (1 - self.hidden_outputs), axis=0, keepdims=True)

    def train(self, inputs, targets, epochs):
        # Training loop
        for epoch in range(epochs):
            # Forward pass
            self.forward(inputs)

            # Backward pass and update weights
            self.backward(inputs, targets)

            # Calculate and print the mean squared error
            mse = np.mean((targets - self.final_outputs) ** 2)
            print(f"Epoch {epoch+1}/{epochs}, Mean Squared Error: {mse}")

# Example usage
input_size = 2
hidden_size = 3
output_size = 2

# Create a neural network
nn = NeuralNetwork(input_size, hidden_size, output_size, learning_rate=0.01)

# Example training data
inputs = np.array([[0.8, 0.5], [0.2, 0.1], [0.5, 0.7]])
targets = np.array([[1, 0], [0, 1], [1, 0]])

# Train the neural network
nn.train(inputs, targets, epochs=1000)

# Test the trained network
test_data = np.array([[0.4, 0.3]])
output = nn.forward(test_data)

print("Test Input:", test_data)
print("Test Output:", output)
