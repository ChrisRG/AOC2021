from typing import List


def load_data(filepath: str) -> List[List[int]]:
    with open(filepath, "r") as f:
        return [[int(i) for i in list(line.rstrip())] for line in f.readlines()]


def octo_print(octos: List[List[int]]):
    for line in octos:
        print(line)


def neighbors(index: tuple[int, int], octos: List[List[int]]) -> List[tuple[int, int]]:
    neighbors = []
    for y in range(-1, 2):
        for x in range(-1, 2):
            nbor_y = index[0] + y
            nbor_x = index[1] + x
            if nbor_y >= 0 and nbor_y <= 9 and nbor_x >= 0 and nbor_x <= 9:
                if octos[nbor_y][nbor_x] and (nbor_y, nbor_x) != index:
                    neighbors.append((nbor_y, nbor_x))
    return neighbors


def total_flashes(octos: List[List[int]]) -> int:
    total = 0
    for _ in range(0, 100):
        total += step(octos)[0]
    return total


def step(octos: List[List[int]]) -> tuple[int, bool]:
    total = 0
    simul_flash = False
    to_flash = []
    flashed = []
    for y in range(0, 10):
        for x in range(0, 10):
            octos[y][x] = (octos[y][x] + 1) % 10
            if octos[y][x] == 0:
                to_flash.append((y, x))
    while len(to_flash) > 0:
        octo = to_flash.pop()
        total += 1
        flashed.append(octo)
        for nbor in neighbors(octo, octos):
            nbor_y, nbor_x = nbor
            octos[nbor_y][nbor_x] = (octos[nbor_y][nbor_x] + 1) % 10
            if octos[nbor_y][nbor_x] == 0 and nbor not in flashed:
                to_flash.append(nbor)
    if len(flashed) == 100:
        simul_flash = True
    return (total, simul_flash)


def simul_flash(octos: List[List[int]]) -> int:
    n = 0
    simul_flash = False
    while simul_flash == False:
        _, simul_flash = step(octos)
        n += 1
    return n


def test_data():
    print("Testing...")
    octos = load_data("inputs/day_11_test.txt")

    test1 = total_flashes(octos)
    print(f"Total: {test1}")

    octos = load_data("inputs/day_11_test.txt")
    simul = simul_flash(octos)

    print(f"Simul flash: Step {simul}")
    print("Test passed.")


def main():
    test_data()
    octos = load_data("inputs/day_11_input.txt")
    part1 = total_flashes(octos)
    print(f"Part 1: {part1}")
    octos = load_data("inputs/day_11_input.txt")
    simul = simul_flash(octos)
    print(f"Part 2: {simul}")


if __name__ == "__main__":
    main()
