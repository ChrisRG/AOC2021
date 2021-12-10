from typing import List
from itertools import chain


def load_data(filepath: str) -> tuple[List[int], List[tuple[int, int, int, int]]]:
    with open(filepath, "r") as f:
        stripped_lines = [line.split(" -> ") for line in f.readlines()]
        vectors = []
        maxes = [0, 0]
        for line in stripped_lines:
            vector = parse_vector(line)
            vectors.append(vector)
            # Check max size of matrix as we parse vectors using X2 and Y2
            if vector[1] > maxes[0]:
                maxes[0] = vector[1]
            if vector[3] > maxes[1]:
                maxes[1] = vector[3]
        return (maxes, vectors)


def parse_vector(vector_str: List[str]) -> tuple[int, int, int, int]:
    # Each vector is a 4-part tuple of X1,Y1,X2,Y2
    xs, ys = vector_str
    xs = [int(x) for x in xs.split(",")]
    ys = [int(y) for y in ys.split(",")]
    return (xs[0], xs[1], ys[0], ys[1])


def update_matrix(
    matrix: List[List[int]], vectors: List[tuple[int, int, int, int]]
) -> List[List[int]]:
    for vec in vectors:
        # Swap points if second Y is less than first
        if vec[3] < vec[1]:
            point1 = (vec[2], vec[3])
            point2 = (vec[0], vec[1])
        else:
            point1 = (vec[0], vec[1])
            point2 = (vec[2], vec[3])
        # Check diagonals
        if point1[0] != point2[0] and point1[1] != point2[1]:
            # For part 1, to ignore diagonals replace the following block with 'continue'
            for idx, y in enumerate(range(point1[1], point2[1] + 1)):
                if point1[0] <= point2[0]:
                    x = point1[0] + idx
                else:
                    x = point1[0] - idx
                matrix[y][x] += 1
        else:
            for y in range(point1[1], point2[1] + 1):
                # Swap points if second X is less than first
                if vec[2] < vec[0]:
                    point1 = (vec[2], vec[3])
                    point2 = (vec[0], vec[1])
                for x in range(point1[0], point2[0] + 1):
                    matrix[y][x] += 1
    return matrix


def test_data() -> None:
    print("Testing...")
    maxes, vectors = load_data("inputs/day_5_test.txt")
    # Instantiate an empty matrix of 0s of size maxes[0], maxes[1]
    matrix = [[0 for _ in range(maxes[1] + 1)] for _ in range(maxes[0] + 1)]
    final_matrix = update_matrix(matrix, vectors)
    final_num = len(list(filter(lambda x: x > 1, list(chain(*final_matrix)))))

    # Part 1: assert final_num, 5
    assert final_num, 12

    print("Tests passed.")


def main() -> None:
    test_data()

    maxes, vectors = load_data("inputs/day_5_input.txt")
    matrix = [[0 for _ in range(maxes[1] + 1)] for _ in range(maxes[0] + 1)]
    # Retrieve the final updated matrix, flatten the 2D array, filter for numbers greater than 1, return length
    final_matrix = update_matrix(matrix, vectors)
    final_num = len(list(filter(lambda x: x > 1, list(chain(*final_matrix)))))

    print(f"Part 2: {final_num}")


if __name__ == "__main__":
    main()
