import torch
from transformers import AutoTokenizer, AutoModel

# Pretrained language model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Test words
test_words = ['kiwi', 'lemon', 'melon']

# Tokenize the test words
encoded_inputs = tokenizer(test_words, padding=True, truncation=True, return_tensors='pt')

# Forward pass through the language model
outputs = model(**encoded_inputs)

# Extract the contextualized word embeddings
word_embeddings = outputs.last_hidden_state

# Do something with the embeddings (e.g., classification, clustering, etc.)

# For example, print the embedding of each word
for i, word in enumerate(test_words):
    embedding = word_embeddings[i]
    print(f"Word: {word}")
    print(f"Embedding: {embedding}")
    print()
