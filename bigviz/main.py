from attention import Model
from viz import generate_html


def main():

    text = '''Traditional color theory was built around "pure" or ideal colors, characterized by different sensory experiences rather than attributes of the physical world. This has led to several inaccuracies in traditional color theory principles that are not always remedied in modern formulations. Another issue has been the tendency to describe color effects holistically or categorically, for example as a contrast between "yellow" and "blue" conceived as generic colors instead of the three color attributes generally considered by color science: hue, colorfulness and lightness.'''.strip()

    model = Model()
    html = generate_html(model, text)

    print(html)


if __name__ == '__main__':
    main()
