from collections import deque


def solve(maze, commands, sr, sc):
    dir = [
        [1, 5, 3, 6, 4, 2],
        [1, 6, 3, 5, 2, 4],
        [2, 3, 4, 1, 5, 6],
        [4, 1, 2, 3, 5, 6],  # 동서북남
    ]
    dice = [0] * 6
    for c in commands:
        ndice = dice[:]
        if c == 1 and sc < len(maze[0]) - 1:
            sc += 1
        elif c == 2 and sc > 0:
            sc -= 1
        elif c == 3 and sr > 0:
            sr -= 1
        elif c == 4 and sr < len(maze) - 1:
            sr += 1
        else:
            continue
        for i in range(6):
            # set_trace()
            dice[i] = ndice[dir[c - 1][i] - 1]
        if maze[sr][sc] == 0:
            maze[sr][sc] = dice[3]
        else:
            dice[3] = maze[sr][sc]
            maze[sr][sc] = 0
        print(dice[1])


if __name__ == "__main__":
    r, c, sr, sc, n_commands = map(int, input().split())
    riddle = []
    for _ in range(r):
        tmp = list(map(int, input().split()))
        riddle.append(tmp)
    commands = list(map(int, input().split()))
    solve(riddle, commands, sr, sc)
