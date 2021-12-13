from typing import List


def load_data(filepath: str) -> dict:
    with open(filepath, "r") as f:
        lines = f.readlines()
        graph = {}
        for line in lines:
            s_node, e_node = line.rstrip().split("-")
            if s_node in graph:
                graph[s_node].append(e_node)
            else:
                graph[s_node] = [e_node]
            if s_node == "start":
                continue
            if e_node in graph:
                graph[e_node].append(s_node)
            else:
                graph[e_node] = [s_node]
        return graph


def find_paths(graph: dict) -> List[List[str]]:
    paths = []

    def traverse(current: str, path: List[str], visited: List[str]):
        path.append(current)
        if current == "end":
            paths.append(path)
            return
        if current not in graph:
            return
        if current.islower():
            visited.append(current)
        for node in graph[current]:
            if node in visited:
                continue
            else:
                traverse(node, path.copy(), visited.copy())

    traverse("start", [], [])
    return paths


def find_paths2(graph: dict) -> List[List[str]]:
    paths = []

    def traverse(current: str, path: List[str], visited: List[str], double: bool):
        path.append(current)
        if current == "end":
            paths.append(path)
            return
        if current not in graph:
            return
        if current.islower():
            if not double and current in visited:
                double = True
            else:
                visited.append(current)
        for node in graph[current]:
            if node in visited and double is True:
                continue
            elif node == "start":
                continue
            else:
                traverse(node, path.copy(), visited.copy(), double)

    traverse("start", [], [], False)
    return paths


def test_data():
    print("Testing...")
    data = load_data("inputs/day_12_test.txt")
    results = find_paths(data)

    print(f"Test 1: {len(results)}")

    results2 = find_paths2(data)
    print(f"Test 2: {len(results2)}")

    print("Test passed.")


def main():
    test_data()
    data = load_data("inputs/day_12_input.txt")

    results = find_paths(data)
    print(f"Part 1: {len(results)}")

    results2 = find_paths2(data)
    print(f"Part 1: {len(results2)}")


if __name__ == "__main__":
    main()
