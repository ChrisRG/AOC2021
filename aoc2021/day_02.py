from typing import List


def load_data() -> List[str]:
    with open("inputs/day_2_input.txt", "r") as f:
        return [item.strip() for item in f.readlines()]


def parse_line(line: str) -> List[int]:
    """
    Given a string containing a direction and amount, e.g. 'forward 10',
    returns a pair of integers
    """
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


def calculate_aim(data: List[str]) -> tuple[int, int]:
    """
    For each line, calculate vertical change based on product of given horizontal amount and cumulative aim.
    Update total horizontal and aim amounts.
    Return the pair of horizontal and vertical changes.
    """
    horiz = 0
    vert = 0
    aim = 0
    for line in map(parse_line, data):
        vert += line[0] * aim
        horiz += line[0]
        aim += line[1]
    return (horiz, vert)


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

    horiz_aim_changes, vert_aim_changes = calculate_aim(test_directions)
    assert (horiz_aim_changes * vert_aim_changes) == 900
    print("Test passed")


def main() -> None:
    test_data()
    data = load_data()
    horiz_changes, vert_changes = calculate_changes(data)
    print(f"Part 1: {horiz_changes * vert_changes}")

    horiz_aim_changes, vert_aim_changes = calculate_aim(data)
    print(f"Part 2: {horiz_aim_changes * vert_aim_changes}")


if __name__ == "__main__":
    main()
