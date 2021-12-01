from typing import List
from more_itertools import sliding_window


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]


def count_increases(data: List[int]) -> int:
    """
    Iterate over pairs of list L, increase total if Lx > Lx - 1
    """
    total: int = 0
    for index, measure in enumerate(data):
        if measure > data[index - 1]:
            total = total + 1

    return total


def count_window_increases(data: List[int]) -> int:
    """
    Iterate over overlapping 3-element tuples of list L, increase total if sum L(x) > sum L(x - 1)
    """
    total: int = 0
    prev: int = sum(data[0:3])
    for window in sliding_window(data, 3):
        if sum(window) > prev:
            total = total + 1
        prev = sum(window)

    return total


def main() -> None:
    data = load_data()

    number_increases = count_increases(data)
    print(number_increases)

    window_increases = count_window_increases(data)
    print(window_increases)


if __name__ == "__main__":
    main()
