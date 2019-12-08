#!/usr/bin/env python3
#
# Run with: python3 main.py < input.txt

import sys

IMAGE_SIZE = (25, 6)
BLACK = 0
WHITE = 1
TRANSPARENT = 2


def main():
    # Part 1
    layers = read_layers(read_raw_image(next(sys.stdin).strip()),
                         IMAGE_SIZE[0],
                         IMAGE_SIZE[1])
    print("Checksum:", checksum(layers))

    # Part 2
    image = compose_image(layers)
    print_image(image, IMAGE_SIZE[0])


def read_raw_image(strdata):
    return [int(x) for x in strdata]


def read_layers(data, width, height):
    layer_size = width * height
    return [data[start:start+layer_size]
            for start in range(0, len(data), layer_size)]


def checksum(layers):
    fewest_zeros = min(layers, key=lambda x: x.count(0))
    return fewest_zeros.count(1) * fewest_zeros.count(2)


def compose_image(layers):
    def first_nontransparent(px):
        return px[0] if px[0] != TRANSPARENT else first_nontransparent(px[1:])
    return [first_nontransparent(px) for px in zip(*layers)]


def print_image(image, width):
    for idx, px in enumerate(image):
        if idx % width == 0:
            print()
        print('#' if px == WHITE else ' ', end='')
    print()


if __name__ == '__main__':
    main()
