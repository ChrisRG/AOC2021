from typing import List


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]


def count_increases(data: List[int]) -> int:
    total: int = 0
    for measures in zip(data, data[1:]):
        if measures[1] > measures[0]:
            total = total + 1

    return total


def count_window_increases(data: List[int]) -> int:
    window_data = list(map(sum, zip(data, data[1:], data[2:])))
    return count_increases(window_data)


def main() -> None:
    data = load_data()

    number_increases = count_increases(data)
    print(number_increases)

    window_increases = count_window_increases(data)
    print(window_increases)


if __name__ == "__main__":
    main()
