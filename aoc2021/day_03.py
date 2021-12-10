from typing import List
import collections


def load_data(filepath: str) -> List[int]:
    with open(filepath, "r") as f:
        return [int(item.strip(), 2) for item in f.readlines()]


def common_bits(data: List[int], length: int, default: int) -> List[int]:
    """
    For every number in the dataset, to retrieve bit in position N, bitwise shift to the right N times and apply an 0b1 mask to get the single bit.

    """
    most_common_bits = []
    for bit_pos in reversed(range(length)):
        bits = [bin((num >> bit_pos) & 0b1) for num in data]
        top_bit = select_top_bit(bits, default)
        most_common_bits.append(top_bit)
    return most_common_bits


def select_top_bit(bits: List[str], default: int) -> int:
    top_bit = collections.Counter(bits).most_common()[0]
    if top_bit[1] == len(bits) / 2:
        return default
    else:
        return int(top_bit[0], 2)


def flip_bits(bit_list: List[int]) -> List[int]:
    return [item ^ 1 for item in bit_list]


def list2int(bit_list: List[int]) -> int:
    str_nums = [str(bit) for bit in bit_list]
    return int("".join(str_nums), 2)


def check_bit(num: int, bit_pos: int, target: int) -> bool:
    return (num >> bit_pos) & 0b1 == target


def oxygen_rating(data: List[int], length: int) -> int:
    for bit_pos in reversed(range(length)):
        if len(data) == 1:
            break
        most_common = list(reversed(common_bits(data, length, 1)))
        data = list(
            filter(lambda num: check_bit(num, bit_pos, most_common[bit_pos]), data)
        )
    return data[0]


def co2_rating(data: List[int], length: int) -> int:
    for bit_pos in reversed(range(length)):
        if len(data) == 1:
            break
        most_common = list(reversed(common_bits(data, length, 1)))
        least_common = flip_bits(most_common)
        data = list(
            filter(lambda num: check_bit(num, bit_pos, least_common[bit_pos]), data)
        )
    return data[0]


def test_data():
    data = load_data("inputs/day_3_test.txt")
    most_common = common_bits(data, 5, 1)
    least_common = flip_bits(most_common)

    # Part 1
    assert list2int(most_common) * list2int(least_common) == 198

    # Part 2
    assert oxygen_rating(data, 5), 23
    assert co2_rating(data, 5), 10

    print("Test passed")


def main() -> None:
    data = load_data("inputs/day_3_input.txt")
    test_data()

    most_common = common_bits(data, 12, 1)
    least_common = flip_bits(most_common)
    part1 = list2int(most_common) * list2int(least_common)
    print(f"Part 1: {part1}")

    oxygen = oxygen_rating(data, 12)
    co2 = co2_rating(data, 12)
    print(f"Part 2: {oxygen * co2}")


if __name__ == "__main__":
    main()
