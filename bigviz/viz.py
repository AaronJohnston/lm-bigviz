import json
import torch


def generate_html(model, text):
    """Generates HTML for attention visualization."""

    input_tokens, attentions = model.generate_attention(text)
    json_attn_matrix = json.dumps(attn_matrix(attentions).tolist())

    html = f'''
    <div class="bigviz" data-attn="{json_attn_matrix}">
    '''

    for i, token in enumerate(input_tokens[0]):
        token = model.tokenizer.decode(token)
        html += f'<span class="token" data-idx="{i}">{token}</span>'

    html += '''
    </div>
    '''

    return html


def attn_matrix(attentions):
    stacked = torch.stack(attentions)  # Stack layers tuple into tensor
    avg_over_layers = stacked.mean(dim=0)  # Average over 12 layers
    avg_over_heads = avg_over_layers.mean(
        dim=1)  # Average over 12 attention heads
    return avg_over_heads[0]  # Select the single sample in batch
