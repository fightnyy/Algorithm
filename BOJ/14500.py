def solve(maze):
    stick_dr = [
        [0, 1, 2, 3],
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 2],
        [0, 1, 1, 2],
        [1, 1, 0, 1],
        [0, 1, 1, 2],
        [0, 1, 1, 2],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [2, 2, 1, 0],
        [0, 1, 2, 2],
        [0, 0, 1, 2],
        [0, 0, 1, 2],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 1, 1, 1],
    ]
    stick_dc = [
        [0, 0, 0, 0],
        [0, 1, 2, 3],
        [0, 1, 0, 1],
        [0, 1, 1, 2],
        [1, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 2],
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 2],
        [0, 1, 1, 2],
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 2, 0],
        [0, 1, 2, 2],
        [0, 0, 1, 2],
        [2, 2, 1, 0],
    ]
    # import pdb
    # pdb.set_trace()
    result = 0
    for a in range(19):
        for b in range(len(maze)):
            for c in range(len(maze[0])):
                tmp = 0
                for d in range(4):
                    if b + stick_dr[a][d] >= len(maze) or c + stick_dc[a][d] >= len(
                        maze[0]
                    ):
                        tmp = 0
                        continue
                    tmp += maze[b + stick_dr[a][d]][c + stick_dc[a][d]]

                result = max(result, tmp)

    return result


if __name__ == "__main__":
    row, col = map(int, input().split())
    maze = []
    for _ in range(row):
        maze.append(list(map(int, input().split())))
    print(solve(maze))
