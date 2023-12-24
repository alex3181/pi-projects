# pip install transformers
from transformers import BertForQuestionAnswering, BertTokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"  # BERT model fine-tuned on SQuAD dataset
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Sample text from a book or any passage
file_name = "202-01.txt"
text = ""
try:
    with open(file_name, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print("An error occurred:", e)


# Tokenize the text
tokenized_text = tokenizer.encode_plus(text, return_tensors="pt")

# Ask questions
questions = [
    "What does police officer needs to monitor?",
    "Who do you report to when enter a stationhouse?",
    # Add more questions as needed
]

for question in questions:
    # Tokenize the question
    inputs = tokenizer.encode_plus(question, text, return_tensors="pt")

    # Get the answer from the model
    start_scores, end_scores = model(**inputs)

    # Get the most likely answer
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores) + 1

    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(
            tokenized_text["input_ids"][0][start_index:end_index]
        )
    )
    print(f"Question: {question}")
    print(f"Answer: {answer}")
