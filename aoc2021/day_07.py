from typing import List, Callable


def load_data(filepath: str) -> List[int]:
    with open(filepath, "r") as f:
        return [int(item) for item in f.read().split(",")]


def find_position(crabs: List[int], calculate_fuel: Callable) -> int:
    # After sorting given list of crabs, taken midpoint position as plausible first guess for lowest fuel cost
    # Check lower positions to the left until higher number reached
    # Check higher positions to the right until higher number reached, by then lowest fuel cost should have been encountered
    sorted_crabs = sorted(crabs)

    midpoint = len(sorted_crabs) // 2
    lowest = calculate_fuel(sorted_crabs, midpoint)

    lo = midpoint - 1

    while lo > 0:
        lo_fuel = calculate_fuel(sorted_crabs, lo)
        if lo_fuel <= lowest:
            lowest = lo_fuel
            lo -= 1
        else:
            break

    hi = midpoint + 1

    while hi < len(sorted_crabs):
        hi_fuel = calculate_fuel(sorted_crabs, hi)
        if hi_fuel <= lowest:
            lowest = hi_fuel
            hi += 1
        else:
            break

    return lowest


def calculate_normal_fuel(crabs: List[int], position: int) -> int:
    # Fuel cost => absolute distance between crab position and given position
    return sum(list(map(lambda x: abs(x - position), crabs)))


def calculate_expensive_fuel(crabs: List[int], position: int) -> int:
    # Fuel cost => sum of numbers from 1 to N inclusive, where N is absolute distance between crab pos and given pos
    # Alternative equation for triangular numbers: n * (n + 1) // 2
    return sum(
        list(map(lambda x: abs(x - position) * (abs(x - position) + 1) // 2, crabs))
    )


def test_data() -> None:
    data = load_data("inputs/day_7_test.txt")
    print("Testing...")

    final_pos1 = find_position(data, calculate_normal_fuel)
    assert final_pos1, 37

    final_pos2 = find_position(data, calculate_expensive_fuel)
    assert final_pos2, 168

    print("Passed tests.")


def main() -> None:
    test_data()
    data = load_data("inputs/day_7_input.txt")

    final_pos1 = find_position(data, calculate_normal_fuel)
    print(f"Part 1: {final_pos1}")

    final_pos2 = find_position(data, calculate_expensive_fuel)
    print(f"Part 1: {final_pos2}")


if __name__ == "__main__":
    main()
