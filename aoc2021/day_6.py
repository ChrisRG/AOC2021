from typing import List


def load_data(filepath: str):
    with open(filepath, "r") as f:
        return [int(item) for item in f.read().split(",")]


def update_fish(age_groups: List[int]) -> List[int]:
    # Rotate list leftwise (list[0] -> list[8]; list[2] -> list[1]; etc)
    # To account for increase, increment list[7] (i.e. age 6) by however many are currently in list[0]
    age_groups[7] += age_groups[0]
    return age_groups[1:] + age_groups[:1]


def convert_to_ages(fish: List[int]) -> List[int]:
    age_groups = [0] * 9
    for elem in fish:
        age_groups[elem] += 1
    return age_groups


def cycle_timers(fish: List[int], cycles: int) -> List[int]:
    # Updates the 9 element list of age groups by X cycles
    updated_fish = fish
    for _ in range(cycles):
        updated_fish = update_fish(updated_fish)
    return updated_fish


def test_data() -> None:
    print("Testing...")
    data = load_data("inputs/day_6_test.txt")
    fish_ages = convert_to_ages(data)

    updated_fish1 = cycle_timers(fish_ages, 18)
    assert len(updated_fish1), 26
    updated_fish2 = cycle_timers(fish_ages, 80)
    assert len(updated_fish2), 5934
    updated_fish3 = cycle_timers(fish_ages, 256)
    assert len(updated_fish3), 26984457539

    print("Passed tests.")


def main() -> None:
    test_data()
    data = load_data("inputs/day_6_input.txt")
    fish_ages = convert_to_ages(data)

    updated_fish1 = cycle_timers(fish_ages, 80)
    print(f"Part 1: {sum(updated_fish1)}")
    updated_fish2 = cycle_timers(fish_ages, 256)
    print(f"Part 2: {sum(updated_fish2)}")


if __name__ == "__main__":
    main()
