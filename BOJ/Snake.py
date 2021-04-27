def find_mode(mode, commands, count):
    for s, c in commands:
        if s == count:
            pass


def solve(row, col):
    time = 0
    while True:
        if row < bs and col < bs and board[row][col] != 2:
            time += 1

        else:
            return time


if __name__ == "__main__":
    bs = int(input())
    board = [[0] * bs for _ in range(bs)]
    n_apple = int(input())
    location_apple = []
    commands = []
    for _ in range(n_apple):
        row, col = map(int, input().split())
        board[row, col] = 1

    cs = int(input())

    for _ in range(cs):
        long, c = input().split()
        long = int(long)
        commands.append([long, c])

    solve(0, 0)
