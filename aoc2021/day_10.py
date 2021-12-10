from typing import List


def load_data(filepath: str) -> List[List[str]]:
    with open(filepath, "r") as f:
        return [list(item.rstrip()) for item in f.readlines()]


def parse_line(line: List[str]) -> tuple[int, List[str]]:
    # Returns 1 if line is corrupt, 0 if not, along with either the corrupt character or the remaining unclosed characters on the stack
    stack = []
    match = {")": "(", "]": "[", "}": "{", ">": "<"}
    for char in line:
        match char:
            case "(" | "[" | "{" | "<":
                stack.append(char)
            case ")" | "]" | "}" | ">":
                if match[char] != stack.pop():
                    return (1, list(char))
    return (0, stack)


def num_errors(data: List[List[str]]) -> int:
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    for line in data:
        result = parse_line(line)
        # If the result is flagged as corrupt, extract the first (and only) element to score
        if result[0] == 1:
            total += score[result[1][0]]
    return total


def complete_lines(data: List[List[str]]) -> List[List[str]]:
    closures = []
    match = {"(": ")", "[": "]", "{": "}", "<": ">"}
    for line in data:
        result = parse_line(line)
        line_closure = []
        # If result flagged as incomplete, iterate through unclosed chars and append corresponding symbol to closure list
        if result[0] == 0:
            for char in result[1]:
                line_closure.insert(0, match[char])
            closures.append(line_closure)
    return closures


def score_closures(closures: List[List[str]]) -> int:
    totals = []
    score = {")": 1, "]": 2, "}": 3, ">": 4}
    for closure in closures:
        closure_score = 0
        for char in closure:
            closure_score = closure_score * 5 + score[char]
        totals.append(closure_score)

    midpoint = len(totals) // 2
    return sorted(totals)[midpoint]


def test_data():
    print("Testing...")
    data = load_data("inputs/day_10_test.txt")

    assert num_errors(data), 26397

    completed_lines = complete_lines(data)

    assert score_closures(completed_lines), 288957
    print("Test passed.")


def main() -> None:
    test_data()
    data = load_data("inputs/day_10_input.txt")

    print(f"Part 1: {num_errors(data)}")

    completed_lines = complete_lines(data)

    print(f"Part 2: {score_closures(completed_lines)}")


if __name__ == "__main__":
    main()
