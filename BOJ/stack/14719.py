def solve(walls):
    lmax, rmax = 0, 0
    lngest = max(walls)
    lidx = walls.index(lngest)
    answer = 0

    for idx in range(lidx + 1):
        lmax = max(walls[idx], lmax)
        tmp = lmax - walls[idx]
        answer += tmp if tmp >= 0 else 0

    for idx in range(len(walls) - 1, lidx, -1):
        rmax = max(walls[idx], rmax)
        tmp = rmax - walls[idx]
        answer += tmp if tmp >= 0 else 0
    return answer


if __name__ == "__main__":
    h, w = map(int, input().split())
    walls = list(map(int, input().split()))
    print(solve(walls))
