import random
COLOR_COUNT = 1024
SIZE = 64


def random_color():
    return '#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)])


def main():
    colors = set()
    while len(colors) < COLOR_COUNT:
        colors.add(random_color())

    for idx, c in enumerate(colors):
        print('convert -size {0}x{0} xc:"{1}" bits/{2}.png'.format(SIZE, c, idx))


if __name__ == "__main__":
    main()
