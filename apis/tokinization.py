from transformers import AutoTokenizer
# bert-base-uncased prefined model provided by ChatGPT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

text = "Tokenization is Amazing!"
tokens = tokenizer.tokenize(text)

print (tokens)
# ['token', '##ization', 'is', 'amazing', '!']

ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
# [19204, 3989, 2003, 6429, 999]

# [19204] -> convert to vectors -> [0.1, 0.00007,0.878787,....]
# this conversion is called embedding
