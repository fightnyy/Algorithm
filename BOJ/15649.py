from itertools import permutations


def solve(n, c):
    new_list = []
    for v in range(n):
        v += 1
        new_list.append(v)
    return list(permutations(new_list, c))


if __name__ == "__main__":
    n, c = map(int, input().split())
    print(solve(n, c))
