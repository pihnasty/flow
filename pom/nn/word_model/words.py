import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

# Custom Dataset class
class WordDataset(Dataset):
    def __init__(self, words, labels):
        self.words = words
        self.labels = labels

    def __len__(self):
        return len(self.words)

    def __getitem__(self, idx):
        word = self.words[idx]
        label = self.labels[idx]
        return word, label

# Sample dataset
words = ['apple', 'banana', 'cherry', 'date']
labels = ['fruit', 'fruit', 'fruit', 'not fruit']

# Convert words to numerical representations
word_to_index = {word: idx for idx, word in enumerate(words)}
index_to_label = {label: idx for idx, label in enumerate(set(labels))}
word_sequences = [word_to_index[word] for word in words]
label_sequences = [index_to_label.index(label) for label in labels]

# Convert to PyTorch tensors
word_sequences = torch.LongTensor(word_sequences)
label_sequences = torch.LongTensor(label_sequences)

# Define the neural network architecture
class WordClassifier(nn.Module):
    def __init__(self, num_words, num_labels, embedding_dim, hidden_dim):
        super(WordClassifier, self).__init__()
        self.embedding = nn.Embedding(num_words, embedding_dim)
        self.fc1 = nn.Linear(embedding_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, num_labels)

    def forward(self, x):
        embedded = self.embedding(x)
        flattened = embedded.view(embedded.size(0), -1)
        hidden = torch.relu(self.fc1(flattened))
        output = self.fc2(hidden)
        return output

# Hyperparameters
embedding_dim = 10
hidden_dim = 10
num_epochs = 10
batch_size = 1
learning_rate = 0.01

# Create the dataset and dataloader
dataset = WordDataset(word_sequences, label_sequences)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Create an instance of the model
model = WordClassifier(len(words), len(index_to_label), embedding_dim, hidden_dim)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    for words, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(words)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# Predict new words
new_words = ['elderberry', 'grape', 'kiwi']

# Create the dataset and dataloader
dataset = WordCategoryDataset(indexed_words, indexed_labels)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)





new_word_sequences = [word_to_index[word] for word in new_words]
new_word_sequences = torch.LongTensor(new_word_sequences)
predictions = model(new_word_sequences)
predicted_labels = [index_to_label[pred.item()] for pred in predictions]

print(predicted_labels)
