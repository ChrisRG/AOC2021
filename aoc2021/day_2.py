from os import wait
from typing import List


def load_data() -> List[str]:
    with open("inputs/day_2_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def parse_line(line: str) -> List[int]:
    match line.split():
        case ["forward", amount]:
            return [int(amount), 0]
        case ["down", amount]:
            return [0, int(amount)]
        case ["up", amount]:
            return [0, -int(amount)]
        case _:
            return [0, 0]


def calculate_changes(data: List[str]) -> tuple[int, int]:
    """
    Maps each str line to its corresponding pair of int changes.
    Unzip the pairs to two separate lists and returns the sum as a single pair.
    """
    horiz_changes, vert_changes = zip(*list(map(parse_line, data)))
    return (sum(horiz_changes), sum(vert_changes))


def test_data():
    test_directions = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    horiz_changes, vert_changes = zip(*list(map(parse_line, test_directions)))
    assert (sum(horiz_changes) * sum(vert_changes)) == 150
    print("Test passed.")


def main() -> None:
    test_data()
    data = load_data()
    horiz_changes, vert_changes = calculate_changes(data)
    print(horiz_changes * vert_changes)


if __name__ == "__main__":
    main()
