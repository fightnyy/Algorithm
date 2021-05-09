

# import sys
# import heapq
# from pdb import set_trace
# input = sys.stdin.readline


# def dijkstra(N, start, end, edges):
#     q = []
#     dist = [float('inf')]*N
#     dist[start-1] = 0 # 본인과 본인과의 거리는 0으로 초기화
#     heapq.heappush(q, [0, start-1]) 
#     # set_trace()
#     while q: 
#         # set_trace()
#         cost, pos = heapq.heappop(q) #도착지, 소요시간
#         for c,p in edges[pos]: 
#             c+= cost
#             if c <= dist[p] :
#                 dist[p] = c
#                 heapq.heappush(q, [c,p]) # cost가 작은순으로 pop이 된다.
#     return dist[end-1]


# if __name__ == "__main__":
#     N = int(input())
#     M = int(input())

#     edges = [[] for _ in range(N)]

#     for i in range(M):
#         u, v, w = list(map(int, input().split()))
#         edges[u-1].append([w,v-1])

#     start, end = map(int, input().split())
#     # print(edges)
#     print(dijkstra(N, start, end, edges))






# #     5
# # 8
# # 1 2 2
# # 1 3 3
# # 1 4 1
# # 1 5 10
# # 2 4 2
# # 3 4 1
# # 3 5 1
# # 4 5 3
# # 1 5
import heapq
import sys
input = sys.stdin.readline
def dijkstra(graph, start, end, N):
    q = [[0, start-1]]
    dist = [float('inf')]*N
    dist[start-1] = 0
    while q:
        cs, st = heapq.heappop(q)
        for c, s in graph[st]:
            c+=cs
            if c < dist[s]:
                dist[s]=c
                heapq.heappush(q,[c,s])
    return dist[end-1]



    

if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = dict()
    for i in range(N):
        graph[i] = []
    for _ in range(M):
        start, end, cost = map(int, input().split())
        graph[start-1].append([cost, end-1])
    start, end = map(int, input().split())
    # print(graph)
    print(dijkstra(graph, start, end, N))
