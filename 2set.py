COLOR_COUNT = 1024
COLUMNS = 8


def main():
    bytes_count = 0
    grid = COLUMNS * COLUMNS
    for idx in range(0, COLOR_COUNT, grid):
        print(
            'montage -tile {0}x0 {1} bytes/{2}.png'.format(
                COLUMNS, ' '.join(
                    ['bits/{}.png'.format(j)
                     for j in range(idx, idx + grid)]
                ),
                bytes_count)
        )
        bytes_count += 1


if __name__ == "__main__":
    main()
