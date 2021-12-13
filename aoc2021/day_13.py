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


def print_origami(coords: List[tuple[int, int]]):
    x_size = sorted(coords, key=lambda tup: tup[0])[-1][0]
    y_size = sorted(coords, key=lambda tup: tup[1])[-1][1]
    grid = [[" "] * (x_size + 1) for _ in range(y_size + 1)]
    for pair in coords:
        grid[pair[1]][pair[0]] = "#"
    for line in grid:
        print(f"{' '.join(line)}\n")


def fold(coords: List, fold: tuple[str, int]) -> List[tuple[int, int]]:
    # Y = 2 * fold - Y/X coord
    axis, amt = fold
    new_pairs = []
    old_pairs = []
    # Transform coordinates based on fold, a bit sloppy but functional
    for pair in coords:
        if axis == "y":
            if pair[1] > amt:
                new_pairs.append((pair[0], 2 * amt - pair[1]))
                old_pairs.append(pair)
        elif axis == "x":
            if pair[0] > amt:
                new_pairs.append((2 * amt - pair[0], pair[1]))
                old_pairs.append(pair)
    # To merge points, treat coordinates as sets, removing old pairs and joining new ones
    combos = list((set(coords) - set(old_pairs)).union(set(new_pairs)))
    return combos


def test_data():
    print("Testing...")
    (coords, folds) = load_data("inputs/day_13_test.txt")
    coords = fold(coords, folds[0])
    print(f"Test 1: {len(coords)}")
    for fld in folds[1:]:
        coords = fold(coords, fld)
    print("Test passed.")
    print_origami(coords)


def main():
    test_data()
    (coords, folds) = load_data("inputs/day_13_input.txt")
    coords = fold(coords, folds[0])
    print(f"Part 1: {len(coords)}")

    for fld in folds[1:]:
        coords = fold(coords, fld)
    print("Part 2:")
    print_origami(coords)


if __name__ == "__main__":
    main()
