import torch
import torch.nn as nn
import torch.optim as optim

# Define the neural network architecture
class WordClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(WordClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

# Word-to-index mapping
word_list = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew', 'ice cream', 'juice']
word_to_index = {
    'apple': 0,
    'banana': 1,
    'cherry': 2,
    'date': 3,
    'eggplant': 4,
    'fig': 5,
    'grape': 6,
    'honeydew': 7,
    'ice cream': 8,
    'juice': 9
}

# Category labels
categories = ['fruit', 'fruit', 'fruit', 'fruit', 'vegetable', 'fruit', 'fruit', 'fruit', 'dessert', 'beverage']

# Convert words to numerical representations
indexed_words = [word_to_index[word] for word in word_list]

# Convert categories to numerical representations
label_to_index = {category: idx for idx, category in enumerate(set(categories))}
indexed_labels = [label_to_index[category] for category in categories]

# Convert data to tensors
word_tensor = torch.tensor(indexed_words, dtype=torch.float32).view(-1, 1)
label_tensor = torch.tensor(indexed_labels, dtype=torch.long)

# Hyperparameters
input_size = 1
hidden_size = 10
num_classes = len(label_to_index)
learning_rate = 0.001
num_epochs = 10

# Create the model instance
model = WordClassifier(input_size, hidden_size, num_classes)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(word_tensor)
    loss = criterion(outputs, label_tensor)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print loss for monitoring
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}")

# Test the model
test_words = ['kiwi', 'lemon', 'melon']
test_tensor = torch.tensor([word_to_index[word] for word in test_words])
with torch.no_grad():
    outputs = model(test_tensor)
    _, predicted = torch.max(outputs.data, 1)
    predicted_categories = [list(label_to_index.keys())[idx] for idx in predicted]

print(predicted_categories)
