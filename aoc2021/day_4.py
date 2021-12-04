from typing import List


def load_data(filepath: str) -> tuple[List[int], List[List[List[int]]]]:
    with open(filepath, "r") as f:
        split = f.read().split("\n\n")
        nums = [int(item) for item in split[0].split(",")]
        boards = [board.split("\n") for board in split[1:]]
        boards = [parse_board(board) for board in boards]  # So ugly
        return (nums, boards)


def parse_board(board: List[str]) -> List[List[int]]:
    return list(
        filter(  # Filtering to discard any empty lists due to the split
            lambda x: len(x) > 0,
            list(map(lambda x: [int(num) for num in x.split()], board)),
        )
    )


def check_boards(boards: List[List[List[int]]], nums: List[int]) -> int:
    for idx, _ in enumerate(nums):
        for board in boards:
            if check_board(board, nums[:idx]):
                return board_score(board, nums[:idx])
    return 0


def check_last_boards(boards: List[List[List[int]]], nums: List[int]) -> int:
    """
    Iterating over numbers then boards, if a board's index is not in the list of winner and it has passed,
    add its index to the winner list and add the last number used to the number list.
    Break once we've reached maximum winners.
    Return the board score of the last board with the index of the last number.
    """
    board_indices = []
    num_indices = []
    for num_idx, _ in enumerate(nums):
        if len(board_indices) == len(boards):
            break
        for board_idx, board in enumerate(boards):
            if board_idx not in board_indices and check_board(board, nums[:num_idx]):
                board_indices.append(board_idx)
                num_indices.append(num_idx)

    return board_score(boards[board_indices[-1]], nums[0 : num_indices[-1]])


def check_board(board: List[List[int]], nums: List[int]) -> bool:
    # Nice and concise, taken from Cthulahoops: https://github.com/cthulahoops/aoc2021/blob/main/day4.py
    """
    Either there's at least one line in the board where all numbers in a line are in the number list,
    or there's a column at index i for every line on the board where all numbers are in the number list.
    """
    return any(all(x in nums for x in line) for line in board) or any(
        all(line[i] in nums for line in board) for i in range(5)
    )


def board_score(board: List[List[int]], nums: List[int]) -> int:
    """
    Flatten the 2D board to 1D, filter numbers that aren't in the number list, return the sum of those filtered numbers multiplied by the last number given.
    """
    flat_nums = [num for line in board for num in line]
    final_nums = list(filter(lambda num: num not in nums, flat_nums))
    return sum(final_nums) * nums[-1]


def test_data():
    print("Test boards...")
    (nums, boards) = load_data("inputs/day_4_test.txt")
    winning_board = check_boards(boards, nums)
    last_winner = check_last_boards(boards, nums)
    assert winning_board, 4512
    assert last_winner, 1924
    print("Passed.")


def main() -> None:
    test_data()
    (nums, boards) = load_data("inputs/day_4_input.txt")
    print(f"Part 1: {check_boards(boards, nums)}")

    print(f"Part 2: {check_last_boards(boards, nums)}")


if __name__ == "__main__":
    main()
