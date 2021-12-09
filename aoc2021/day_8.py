from typing import List


def load_data(filepath: str) -> List[List[str]]:
    with open(filepath, "r") as f:
        return [line.rstrip().split(" | ") for line in f.readlines()]


def signal_combos(signals: List[str]) -> dict:
    # First check all signals to retrieve 1 4 7 8
    combos = decode_1478(signals)
    # Next recheck signals to retrieve other 6 character numbers: 0, 6, 9
    hard_signals = [signal for signal in signals if len(signal) == 6]

    decoded = decode_6s(hard_signals, combos)
    combos.update(decoded)

    return combos


def decode_1478(signals: List[str]) -> dict:
    combos = {}
    for signal in signals:
        match len(signal):
            case 2:
                combos[1] = signal
            case 3:
                combos[7] = signal
            case 4:
                combos[4] = signal
            case 7:
                combos[8] = signal
            case _:
                continue
    return combos


def decode_6s(signals: List[str], combos: dict[int, str]) -> dict:
    new_combos = {}
    # Use signals for seven and four to retrieve other 3 signals
    seven = set(list(combos[7]))
    four = set(list(combos[4]))
    for signal in signals:

        # 0 => difference between signal and difference between four and seven (i.e. middle wire)
        diff_middle_wire = set(signal) - (four - seven)
        if len(diff_middle_wire) > 4:
            new_combos[0] = signal

        # 9 => intersection between signal and seven (3 elements) without already being in combos (i.e. 0)
        if (
            len(set(signal).intersection(seven)) == 3
            and signal not in new_combos.values()
        ):
            new_combos[9] = signal

        # 6 remaining 6 length signal
        if signal not in new_combos.values():
            new_combos[6] = signal

    return new_combos


def wire_mapping(combos: dict[int, str]) -> dict:
    wire_map = {}
    # Using 0, 4, 7, 8, 9, find differences and intersections to locate wires
    zero = set(list(combos[0]))
    four = set(list(combos[4]))
    six = set(list(combos[6]))
    seven = set(list(combos[7]))
    eight = set(list(combos[8]))
    nine = set(list(combos[9]))
    # Set differences create lists, so pop off the first
    wire_map[(seven - four).pop()] = "a"
    wire_map[(four.intersection(zero) - seven).pop()] = "b"
    wire_map[(eight - six).pop()] = "c"
    wire_map[(eight - zero).pop()] = "d"
    wire_map[(eight - nine).pop()] = "e"
    wire_map[(seven - (seven - four) - (eight - six)).pop()] = "f"
    for letter in ["a", "b", "c", "d", "e", "f", "g"]:
        if letter not in wire_map.keys():
            wire_map[letter] = "g"
    return wire_map


def transform(chars: List[str], wire_map: dict) -> str:
    """
     aaaa
    b    c
    b    c
     dddd
    e    f
    e    f
     gggg
    """
    mapping = [wire_map[char] for char in chars]
    match sorted(mapping):
        case ["a", "b", "c", "e", "f", "g"]:
            return "0"
        case ["c", "f"]:
            return "1"
        case ["a", "c", "d", "e", "g"]:
            return "2"
        case ["a", "c", "d", "f", "g"]:
            return "3"
        case ["b", "c", "d", "f"]:
            return "4"
        case ["a", "b", "d", "f", "g"]:
            return "5"
        case ["a", "b", "d", "e", "f", "g"]:
            return "6"
        case ["a", "c", "f"]:
            return "7"
        case ["a", "b", "c", "d", "e", "f", "g"]:
            return "8"
        case ["a", "b", "c", "d", "f", "g"]:
            return "9"


def map_output(wire_map: dict, output: str) -> List[str]:
    res = []
    for digit in output.split():
        decoded = transform(list(digit), wire_map)
        if decoded:
            res.append(decoded)
    return res


def test_data() -> None:
    data = load_data("inputs/day_8_test.txt")
    print("Testing...")
    results = []
    for line in data:
        combos = signal_combos(line[0].split())
        wires = wire_mapping(combos)
        result = map_output(wires, line[1])
        results.append(int("".join(result)))
    print(f"Test: {sum(results)}")
    assert sum(results), 61229


def main() -> None:
    test_data()
    data = load_data("inputs/day_8_input.txt")

    results = []
    for line in data:
        combos = signal_combos(line[0].split())
        wires = wire_mapping(combos)
        result = map_output(wires, line[1])
        results.append(int("".join(result)))
    print(f"Part 2: {sum(results)}")


if __name__ == "__main__":
    main()
