from collections import defaultdict, deque
import pdb

"""
n: node의 개수
e: edge의 개수
s: 시작점 
"""

graph = defaultdict(list)

n, e, s = map(int, input().split())

stack = [s]
queue = deque([s])

for _ in range(e):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
for key in graph:
    graph[key].sort(reverse=True)
# pdb.set_trace()
"""
DFS
"""
visited = []
while stack:
    val = stack.pop()
    if val not in visited:
        visited.append(val)
        print(val, end=" ")
        for i in graph[val]:
            if i not in visited:
                stack.append(i)
print()
"""
BFS
"""
visited = []

for key in graph:
    graph[key].sort()
while queue:
    val = queue.popleft()
    if val not in visited:
        visited.append(val)
        print(val, end=" ")
        for i in graph[val]:
            if i not in visited:
                queue.append(i)
