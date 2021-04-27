from copy import deepcopy


def rotate(n, b):
    nb = deepcopy(b)
    for i in range(len(b)):
        for j in range(len(b[0])):
            nb[j][n - i - 1] = b[i][j]
    return nb


def convert(n, b):
    new_list = [v for v in b if v]
    for i in range(1, len(new_list)):
        if new_list[i - 1] == new_list[i]:
            new_list[i - 1] *= 2
            new_list[i] = 0
    new_list = [v for v in new_list if v]
    return new_list + [0] * (n - len(new_list))


def dfs(n, riddle, count):
    ret = max([max(r) for r in riddle])
    if count == 0:
        return ret
    for _ in range(4):
        result = [convert(n, riddle[i]) for i in range(n)]
        ret = max(ret, dfs(n, result, count - 1))
        riddle = rotate(n, riddle)
    return ret


if __name__ == "__main__":
    num = int(input())
    riddle = []
    for _ in range(num):
        riddle.append(list(map(int, input().split())))
    print(dfs(num, riddle, 5))
