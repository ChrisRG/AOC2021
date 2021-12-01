from typing import List
from more_itertools import sliding_window


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]


def count_increases(data: List[int]) -> int:
    total: int = 0
    for index, measure in enumerate(data):
        total = total + 1 if measure > data[index - 1] else total

    return total


def count_window_increases(data: List[int]) -> int:
    total: int = 0
    prev: int = sum(data[0:3])
    for window in sliding_window(data, 3):
        total = total + 1 if sum(window) > prev else total
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
