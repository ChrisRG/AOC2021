from typing import List


def load_data(filepath: str) -> List[List[int]]:
    with open(filepath, "r") as f:
        return [[int(i) for i in list(line.rstrip())] for line in f.readlines()]


def test_data():
    print("Testing...")
    print("Test passed.")


def main():
    test_data()


if __name__ == "__main__":
    main()
