from itertools import combinations
from copy import deepcopy
import sys.stdin.readline as input

def virus(new_maze):
    visited = []
    def dfs(i, j, visited):
        if i < 0 or i >= len(new_maze) or j < 0 or j >= len(new_maze[0]) or new_maze[i][j] == 1 or [i,j] in visited:
            return
        else:
            new_maze[i][j] = 2
            visited.append([i,j])
            dfs(i + 1, j,visited)
            dfs(i - 1, j,visited)
            dfs(i, j + 1,visited)
            dfs(i, j - 1,visited)

    for i in range(len(new_maze)):
        for j in range(len(new_maze[0])):
            if new_maze[i][j] == 2:
                dfs(i,j,visited)
    return new_maze


def solve(maze):
    ori_maze = deepcopy(maze)
    answer = -1
    candidate = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 0:
                candidate.append([i, j])
    for idx,values in enumerate(list(combinations(candidate, 3))):
        tmp = 0
        new_maze = deepcopy(ori_maze)
        for v in values:
            new_maze[v[0]][v[1]] = 1
        after_maze = virus(new_maze)
        for row in (after_maze):
            tmp+=row.count(0)
        answer = max(answer, tmp)

    return answer


if __name__ == "__main__":
    row, col = map(int, input().split())
    maze = []
    for _ in range(row):
        maze.append(list(map(int, input().split())))
    print(solve(maze))
