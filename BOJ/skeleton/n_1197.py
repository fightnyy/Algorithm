import sys
import heapq

input = sys.stdin.readline


def find_parent(node):
    if parent[node] != node:
        parent[node] = find_parent(parent[node])
    return parent[node]


def union_parent(node1, node2):
    node1 = find_parent(node1)
    node2 = find_parent(node2)
    if node1 > node2:
        parent[node1] = node2
        return True
    elif node2 > node1:
        parent[node2] = node1
        return True
    return False


if __name__ == "__main__":
    v, e = map(int, input().split())
    h = []
    answer = 0
    parent = [i for i in range(v)]
    for _ in range(e):
        start, end, cost = map(int, input().split())
        heapq.heappush(h, [cost, start - 1, end - 1])
    while h:
        cost, start, end = heapq.heappop(h)
        if union_parent(start, end):
            answer += cost
    print(answer)
