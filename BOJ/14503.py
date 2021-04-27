from pprint import pprint
import sys
def solution(n, s, a, b, fares):
    maze = [[float('inf')] * n for _ in range(n)]
    answer = float('inf')
    for start, end , spend in fares:
        maze[start-1][end-1] = spend
        maze[end-1][start-1] = spend
    for k in range(len(maze)):
        for i in range(len(maze)):
            for j in range(len(maze)):
                if i == j:
                    maze[i][j] = 0
                    continue
                maze[i][j] = min(maze[i][j], maze[i][k]+maze[k][j])
    for i in maze:
        print(i)
    for i in range(n):
        answer = min(answer, maze[s-1][i] + maze[i][a-1] + maze[i][b-1], maze[s-1][a-1]+maze[s-1][b-1])
    return answer

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n,s,a,b,fares)