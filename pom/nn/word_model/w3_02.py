import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import torch
from transformers import AutoTokenizer, AutoModel

# Pretrained language model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


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
        flattened = embedded.view(embedded.size(0), -1)
        hidden = torch.relu(self.fc1(flattened))
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



# ==================================================================
encoded_inputs_word_list = tokenizer(word_list, padding=True, truncation=True, return_tensors='pt')
outputs_word_list = model(**encoded_inputs_word_list)
word_list_embeddings = outputs_word_list.last_hidden_state

encoded_inputs_label_list = tokenizer(label_list, padding=True, truncation=True, return_tensors='pt')
outputs_label_list = model(**encoded_inputs_label_list)
label_list_embeddings = outputs_label_list.last_hidden_state
# ==================================================================
# Create the model instance
model = WordClassifier(vocab_size, embedding_dim, hidden_dim, output_dim)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
for epoch in range(num_epochs):
    optimizer.zero_grad()
    outputs = model(word_list_embeddings)
    loss = criterion(outputs, label_list_embeddings)
    loss.backward()
    optimizer.step()

# Test the model
test_word_list = ['juice', 'lemon', 'ice cream']
test_word_to_index = {word: idx for idx, word in enumerate(test_word_list)}
indexed_test_words = [test_word_to_index[word] for word in test_word_list]

encoded_inputs_test_word_list = tokenizer(test_word_list, padding=True, truncation=True, return_tensors='pt')
outputs_test_word_list = model(**encoded_inputs_test_word_list)
test_word_list_embeddings = outputs_test_word_list.last_hidden_state

for epoch in range(1):
    predicted_labels = model(test_word_list_embeddings).argmax(dim=1)
    predicted_categories = [list(label_to_index.keys())[idx] for idx in predicted_labels]
    print(predicted_categories)




