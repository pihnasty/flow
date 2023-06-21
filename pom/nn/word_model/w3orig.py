import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# Custom Dataset class
class WordCategoryDataset(Dataset):
    def __init__(self, word_list, label_list):
        self.word_list = word_list
        self.label_list = label_list

    def __len__(self):
        return len(self.word_list)

    def __getitem__(self, idx):
        word = self.word_list[idx]
        label = self.label_list[idx]
        return word, label

# Define the neural network architecture
class WordClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim):
        super(WordClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.fc1 = nn.Linear(embedding_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        embedded = self.embedding(x)
        averaged = torch.mean(embedded, dim=1)
        hidden = self.relu(self.fc1(averaged))
        output = self.fc2(hidden)
        return output

# Hyperparameters
vocab_size = 10000
embedding_dim = 100
hidden_dim = 64
output_dim = 5
learning_rate = 0.001
num_epochs = 10
batch_size = 32

# Sample word list and corresponding labels
word_list = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew', 'ice cream', 'juice']
label_list = ['fruit', 'fruit', 'fruit', 'fruit', 'vegetable', 'fruit', 'fruit', 'fruit', 'dessert', 'beverage']

# Convert words to numerical representations
word_to_index = {word: idx for idx, word in enumerate(word_list)}
label_to_index = {label: idx for idx, label in enumerate(set(label_list))}
indexed_words = [word_to_index[word] for word in word_list]
indexed_labels = [label_to_index[label] for label in label_list]

# Create the dataset and dataloader
dataset = WordCategoryDataset(indexed_words, indexed_labels)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Create the model instance
model = WordClassifier(vocab_size, embedding_dim, hidden_dim, output_dim)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    for words, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(words)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# Test the model
test_words = ['kiwi', 'lemon', 'melon']
indexed_test_words = [word_to_index[word] for word in test_words]
test_tensor = torch.LongTensor(indexed_test_words)
predicted_labels = model(test_tensor).argmax(dim=1)

predicted_categories = [list(label_to_index.keys())[idx] for idx in predicted_labels]

print(predicted_categories)
