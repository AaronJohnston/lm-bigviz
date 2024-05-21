from bigviz.viz import generate_html
from bigviz.viz import generate_attention


def main():
    attention = generate_attention()
    generate_html(attention)


if __name__ == '__main__':
    main()
