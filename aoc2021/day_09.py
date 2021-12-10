from typing import List
from math import prod


def load_data(filepath: str) -> tuple[int, int, dict]:
    with open(filepath, "r") as f:
        lines = f.readlines()
        heightmap = {}
        for y, line in enumerate(lines):
            for x, num in enumerate(list(line.rstrip())):
                heightmap[(x, y)] = num

        return (len(lines[0].rstrip()), len(lines), heightmap)


def get_lowpoints(x_len: int, y_len: int) -> List[tuple[int, int]]:
    lowpoints = []
    for y in range(y_len):
        for x in range(x_len):
            is_low = is_lowpoint((x, y))
            if is_low:
                lowpoints.append((x, y))
    return lowpoints


def is_lowpoint(index: tuple[int, int]) -> bool:
    for neighbor_coord in get_neighbors(index):
        if heightmap[neighbor_coord] <= heightmap[index]:
            return False
    return True


def get_neighbors(index: tuple[int, int]) -> List[tuple[int, int]]:
    # Check for horizontal and vertical neighboring indices, no wrapping
    x, y = index
    neighbors = []
    if heightmap.get((x, y - 1)):
        neighbors.append((x, y - 1))
    if heightmap.get((x, y + 1)):
        neighbors.append((x, y + 1))
    if heightmap.get((x - 1, y)):
        neighbors.append((x - 1, y))
    if heightmap.get((x + 1, y)):
        neighbors.append((x + 1, y))
    return neighbors


def basin_neighbors(index: tuple[int, int]) -> List[tuple[int, int]]:
    # Filter neighbors if value at index is 9
    neighbors = get_neighbors(index)
    if len(neighbors) == 0:
        return []
    else:
        return list(filter(lambda x: int(heightmap[x]) != 9, neighbors))


def get_basins(index: tuple[int, int], basin_list: List[tuple[int, int]]):
    # Recursively check neighbors until reaching an edge or 9
    neighbors = basin_neighbors(index)
    basin_list.append(index)
    if len(neighbors) == 0:
        return []
    else:
        for neighbor in neighbors:
            if neighbor not in basin_list:
                get_basins(neighbor, basin_list)
        return basin_list


def test_data() -> None:
    print("Testing...")
    global heightmap
    (x_len, y_len, heightmap) = load_data("inputs/day_9_test.txt")
    lowpoints = get_lowpoints(x_len, y_len)
    lowpoint_values = list(map(lambda x: int(heightmap[x]), lowpoints))

    print(f"Test part 1: {sum(list(map(lambda x: x + 1, lowpoint_values)))}")

    basins = []
    for lowpoint in lowpoints:
        basins.append(get_basins(lowpoint, []))

    sizes = [len(basin) for basin in list(sorted(basins, key=len, reverse=True))]

    print(f"Test part 2: {prod(sizes[:3])}")


def main() -> None:
    test_data()
    # Functions use global variable heightmap to avoid passing around the dict
    global heightmap
    (x_len, y_len, heightmap) = load_data("inputs/day_9_input.txt")
    lowpoints = get_lowpoints(x_len, y_len)
    lowpoint_values = list(map(lambda x: int(heightmap[x]), lowpoints))

    print(f"Part 1: {sum(list(map(lambda x: x + 1, lowpoint_values)))}")

    basins = []
    for lowpoint in lowpoints:
        basins.append(get_basins(lowpoint, []))

    sizes = [len(basin) for basin in list(sorted(basins, key=len, reverse=True))]

    print(f"Part 2: {prod(sizes[:3])}")


if __name__ == "__main__":
    main()
