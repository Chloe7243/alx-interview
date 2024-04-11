import sys


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)


def is_safe(board, row, col, n):
    # Check for queens in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, n):
    if row == n:
        print_solution(board, n)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # backtrack


def print_solution(board, n):
    solution = ["0"] * n
    for i in range(n):
        solution[board[i]] = str(i + 1)
    print(" ".join(solution))


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    main()
