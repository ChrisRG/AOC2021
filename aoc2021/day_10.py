from typing import List


def load_data(filepath: str) -> List[List[str]]:
    with open(filepath, "r") as f:
        return [list(item.rstrip()) for item in f.readlines()]


def test_data():
    print("Testing...")
    data = load_data("inputs/day_10_test.txt")
    print(data)


def main() -> None:
    test_data()
    data = load_data("inputs/day_10_input.txt")


if __name__ == "__main__":
    main()
