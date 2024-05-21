from transformers import AutoModelForCausalLM, AutoTokenizer


class Model:
    def __init__(self, model_name='gpt2'):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_attention(self, text):
        """Generates attention for a given text."""
        input_tokens = self.tokenizer.encode(text, return_tensors='pt')
        outputs = self.model(input_tokens, output_attentions=True)
        return input_tokens, outputs.attentions[0]
