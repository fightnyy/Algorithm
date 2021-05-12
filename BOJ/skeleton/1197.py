import heapq

def find_parent(node):
    if node != parent[node]:
        parent[node]=find_parent(parent[node])
    return parent[node]




def check_same_parent(node1, node2):
    node1= find_parent(node1)
    node2 = find_parent(node2)
    if node1 > node2:
        parent[node1] = node2
    elif node2 > node1:
        parent[node2] = node1





if __name__ == "__main__":
    V, E = map(int, input().split())
    parent = [i for i in range(V)] 
    answer = 0
    q = []
    for i in range(E):
        start, end, cost = map(int, input().split())
        start -= 1
        end -= 1
        heapq.heappush(q, [cost, start, end])  # 걸리는 시간, 시작점, 도착점
    while q:
        tmp = heapq.heappop(q)
        if find_parent(tmp[1]) != find_parent(tmp[2]):
            check_same_parent(tmp[1],tmp[2])
            answer += tmp[0]
    print(answer)
    print(parent)





# import heapq

# def find_parent(node):
#     if node == parent[node]:
#         return node
#     parent[node]=find_parent(parent[node])
#     return parent[node]
        


# def check_same_parent(node1, node2):
#     node1= find_parent(node1)
#     node2 = find_parent(node2)
#     if node1 > node2:
#         parent[node1] = node2
#     elif node2 > node1:
#         parent[node2] = node1





# if __name__ == "__main__":
#     V, E = map(int, input().split())
#     parent = [i for i in range(V)] 
#     answer = 0
#     q = []
#     for i in range(E):
#         start, end, cost = map(int, input().split())
#         start -= 1
#         end -= 1
#         heapq.heappush(q, [cost, start, end])  # 걸리는 시간, 시작점, 도착점
#     while q:
#         tmp = heapq.heappop(q)
#         if find_parent(tmp[1]) != find_parent(tmp[2]):
#             check_same_parent(tmp[1],tmp[2])
#             answer += tmp[0]
#     print(answer)
#     # print(parent)
