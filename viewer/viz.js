bigvizes = Array.from(document.getElementsByClassName('bigviz'));
console.log(bigvizes);
bigvizes.forEach((viz) => {
    data = JSON.parse(viz.dataset.attn);
    tokens = Array.from(viz.getElementsByClassName('token'));

    for (const token of tokens) {
        token.addEventListener('mouseover', (e) => {
            token_id = parseInt(token.dataset.idx);
            token_attns = data[token_id];

            token_attns.forEach((attn, i) => {
                tokens[i].style.backgroundColor = `rgba(255, 0, 0, ${attn})`;
            });
        });
        token.addEventListener('mouseout', (e) => {
            tokens.forEach((token) => {
                token.style.backgroundColor = '';
            });
        });
    }
});