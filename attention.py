from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('gpt2')
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained('gpt2')


def generate_attention(text):
    """Generates attention for a given text."""
    inputs = tokenizer.encode(text, return_tensors='pt')
    outputs = model(inputs, output_attentions=True)
    return outputs.attentions[0]
