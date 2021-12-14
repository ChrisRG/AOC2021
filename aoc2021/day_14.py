from typing import List


def load_data(filepath: str) -> tuple[str, List]:
    with open(filepath, "r") as f:
        template, rules = f.read().split("\n\n")
        return (template, [rule.split(" -> ") for rule in rules.rstrip().split("\n")])


def match_rule(pair: str, rules: List[List[str]]) -> str:
    for rule in rules:
        if rule[0] == pair:
            return rule[1]
    return ""


def insertion(template: str, rules: List[List[str]]) -> List[List[str]]:
    new_template = []
    for pair in pairize(template):
        matched = match_rule(pair, rules)
        new_pair = list(pair)
        new_pair.insert(1, matched)
        new_template.append(new_pair)
    return new_template


def merge_elements(elements: List[List[str]]) -> List[str]:
    new_elements = []
    for idx, element in enumerate(elements):
        if idx == len(elements) - 1:
            new_elements.append(element)
            break
        if element[-1] == elements[idx + 1][0]:
            new_elements.append(element[:-1])
        else:
            new_elements.append(element)
    return [j for sub in new_elements for j in sub]


def pairize(template) -> List[str]:
    return [template[i : i + 2] for i in range(0, len(template) - 2 + 1)]


def count_elements(template: str) -> List[int]:
    elements = [template.count(element) for element in set(template)]
    return sorted(elements)


def test_data():
    print("Testing...")
    template, rules = load_data("inputs/day_14_test.txt")
    for _ in range(0, 40):
        new_elements = insertion(template, rules)
        template = "".join(merge_elements(new_elements))
    elements = count_elements(template)
    print(f"Test 1: {elements[-1] - elements[0]}")
    print("Test passed.")


def main():
    test_data()
    template, rules = load_data("inputs/day_14_input.txt")
    for _ in range(0, 10):
        new_elements = insertion(template, rules)
        template = "".join(merge_elements(new_elements))
    elements = count_elements(template)
    print(f"Part 1: {elements[-1] - elements[0]}")


if __name__ == "__main__":
    main()
