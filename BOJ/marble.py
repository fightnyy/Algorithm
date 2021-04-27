from collections import deque, defaultdict


def init(riddle):
    for i in range(len(riddle)):
        for j in range(len(riddle[0])):
            if riddle[i][j] == "B":
                bx = i
                by = j
            if riddle[i][j] == "R":
                rx = i
                ry = j
    return rx, ry, bx, by


def move(rx, ry, cx, cy):
    count = 0
    while riddle[rx][ry] != "O" and riddle[rx][ry] != "#":
        rx = rx + cx
        ry = ry + cy
        count += 1
    rx -= cx
    ry -= cy
    return rx, ry, count


def bfs(riddle, count, visited, rx, ry, bx, by):
    q = deque()
    q.append([rx, ry, bx, by, count])
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count > 10:
            break
        for i in range(4):
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i])
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i])
            if riddle[next_bx + dx[i]][next_by + dy[i]] == "O":
                continue
            if riddle[next_rx + dx[i]][next_ry + dy[i]] == "O":
                print(count)
                return
            if next_rx == next_bx and next_ry == next_by:
                if r_count > b_count:
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            if visited[next_rx, next_ry, next_bx, next_by] == 0:
                visited[next_rx, next_ry, next_bx, next_by] = 1
                q.append([next_rx, next_ry, next_bx, next_by, count + 1])
    print(-1)


if __name__ == "__main__":
    riddle = []
    row, col = map(int, input().split())
    for _ in range(row):
        riddle.append(list(input()))
    rx, ry, bx, by = init(riddle)

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = defaultdict(int)
    visited[rx, ry, bx, by] = 1
    bfs(riddle, 1, visited, rx, ry, bx, by)
