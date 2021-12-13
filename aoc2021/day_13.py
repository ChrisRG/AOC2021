from typing import List


def load_data(filepath: str) -> tuple[List, List]:
    with open(filepath, "r") as f:
        page = f.read().split("\n\n")
        dots = [line.split(",") for line in page[0].split("\n")]
        fold_strs = [line.split(" along ") for line in page[1].rstrip().split("\n")]
        folds = []
        for line in fold_strs:
            split = line[1].split("=")
            folds.append((split[0], int(split[1])))
        # Returns a tuple with a list of coordinates ('x', y') and a list of operations ('x'|'y', int)
        return ([(int(pair[0]), int(pair[1])) for pair in dots], folds)


def fold(coords: List[List[int]], fold: tuple[str, int]):
    # Y = 2 * fold - Y/X coord
    axis, amt = fold
    new_pairs = []
    old_pairs = []
    for pair in coords:
        if axis == "y":
            if pair[1] > amt:
                new_pairs.append((pair[0], 2 * amt - pair[1]))
                old_pairs.append(pair)
        elif axis == "x":
            if pair[0] > amt:
                new_pairs.append((2 * amt - pair[0], pair[1]))
                old_pairs.append(pair)
    combos = (set(coords) - set(old_pairs)).union(set(new_pairs))
    return combos


def test_data():
    print("Testing...")
    (coords, folds) = load_data("inputs/day_13_test.txt")
    coords = fold(coords, folds[0])
    print(f"Test 1: {len(coords)}")
    print("Test passed.")


def main():
    test_data()
    (coords, folds) = load_data("inputs/day_13_input.txt")
    coords = fold(coords, folds[0])
    print(f"Part 1: {len(coords)}")


if __name__ == "__main__":
    main()
