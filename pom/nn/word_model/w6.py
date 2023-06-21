import torch
import torch.nn as nn
import torch.optim as optim

# Define the neural network architecture
class SentimentClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SentimentClassifier, self).__init__()
        self.hidden = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.output = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        hidden = self.hidden(x)
        activated = self.relu(hidden)
        output = self.output(activated)
        probabilities = self.softmax(output)
        return probabilities

# Define the dataset
train_data = [
    ([1, 0], [1, 0]),  # happy -> positive
    ([0, 1], [0, 1]),  # sad -> negative
    ([1, 0], [1, 0]),  # amazing -> positive
    ([0, 1], [0, 1])   # terrible -> negative
]

# Convert the dataset to PyTorch tensors
train_data = [(torch.tensor(x), torch.tensor(y)) for x, y in train_data]

# Define hyperparameters
input_size = 2  # number of features (one-hot encoding)
hidden_size = 10  # number of neurons in the hidden layer
output_size = 2  # number of classes (positive and negative sentiment)
learning_rate = 0.1
num_epochs = 100

# Initialize the model
model = SentimentClassifier(input_size, hidden_size, output_size)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    for x, y in train_data:
        # Forward pass
        outputs = model(x.float())
        loss = criterion(outputs.unsqueeze(0), y.argmax().unsqueeze(0))

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch+1) % 10 == 0:
        print(f"Epoch: {epoch+1}/{num_epochs}, Loss: {loss.item()}")

# Testing
test_data = [
    ([1, 0], "happy"),
    ([0, 1], "sad"),
    ([1, 0], "amazing"),
    ([0, 1], "terrible")
]

for x, word in test_data:
    output = model(torch.tensor(x).float())
    predicted_sentiment = "positive" if output.argmax().item() == 0 else "negative"
    print(f"Word: {word}, Predicted Sentiment: {predicted_sentiment}")
