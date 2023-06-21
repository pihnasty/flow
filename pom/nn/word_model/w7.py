import torch
import torch.nn as nn
import torch.optim as optim

# Step 1: Data Preparation
# Assuming you have your dataset stored in lists of words and categories
words = ['apple', 'banana', 'orange', 'carrot']
categories = ['fruit', 'fruit', 'fruit', 'vegetable']

# Create a vocabulary and map each word to a unique index
vocab = {word: idx for idx, word in enumerate(words)}

# Convert words to numerical representations (one-hot encodings)
num_words = len(words)
input_size = len(vocab)
word_to_idx = lambda word: torch.tensor([vocab[word]], dtype=torch.long)
words_onehot = torch.eye(input_size)[torch.tensor([vocab[word] for word in words], dtype=torch.long)]

# Convert categories to numerical representations
categories_set = list(set(categories))
num_categories = len(categories_set)
category_to_idx = {cat: idx for idx, cat in enumerate(categories_set)}
categories_idx = torch.tensor([category_to_idx[cat] for cat in categories], dtype=torch.long)

# Split the data into training and testing sets
train_ratio = 0.8
train_size = int(train_ratio * num_words)
train_words, train_labels = words_onehot[:train_size], categories_idx[:train_size]
test_words, test_labels = words_onehot[train_size:], categories_idx[train_size:]

# Step 2: Define the Model
class WordClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(WordClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

# Step 3: Define the Loss Function
criterion = nn.CrossEntropyLoss()

# Step 4: Define the Optimizer
learning_rate = 0.01
hidden_size = 16
output_size = num_categories

model = WordClassifier(input_size, hidden_size, output_size)
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Step 5: Training Loop
num_epochs = 1000

for epoch in range(num_epochs):
    # Forward pass
    outputs = model(train_words)
    loss = criterion(outputs, train_labels)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print the loss at every 10 epochs
    if (epoch+1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Step 6: Evaluation
with torch.no_grad():
    model.eval()
    test_outputs = model(test_words)
    _, predicted = torch.max(test_outputs, 1)
    accuracy = (predicted == test_labels).sum().item() / test_labels.size(0)
    print(f'Test Accuracy: {accuracy:.4f}')

# Step 7: Inference
new_words = ['carrot', 'carrot']
new_words_onehot = torch.eye(input_size)[torch.tensor([vocab[word] for word in new_words], dtype=torch.long)]
with torch.no_grad():
    model.eval()
    new_outputs = model(new_words_onehot)
    _, predicted_categories = torch.max(new_outputs, 1)

    # Map predicted category indices back to category names
    idx_to_category = {idx: cat for cat, idx in category_to_idx.items()}
    predicted_categories = [idx_to_category[idx.item()] for idx in predicted_categories]

    print("Predicted Categories:")
    for word, category in zip(new_words, predicted_categories):
        print(f"{word}: {category}")