def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x


def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]


def run(many_set):
    parent = [0] * 6
    for i in range(6):
        parent[i] = i
    for x, y in many_set:
        union(parent, x-1, y-1)
    return parent


if __name__ == "__main__":
    many_set = [[1, 2], [2, 3], [3, 4], [1, 4], [5, 6]]
    print(run(many_set))
