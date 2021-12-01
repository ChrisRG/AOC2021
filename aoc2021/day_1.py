from typing import List


def load_data() -> List[int]:
    with open("inputs/day_1_input.txt", "r") as f:
        return [int(item.strip()) for item in f.readlines()]
