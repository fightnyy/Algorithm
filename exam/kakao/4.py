from collections import defaultdict


def solution(n, start, end, roads, traps):
    graph = dict()
    inverse_graph = dict()
    for i in range(1, n + 1):
        graph[i] = [[], []]  # graph key, value
    inverse_graph[i] = [[], []]
    # 출발 = [도착, 걸린시간]
    for s, e, c in roads:
        graph[s][0].append(e)
        graph[s][1].append(c)
        inverse_graph[e][0].append(s)
        inverse_graph[e][1].append(c)
    # for mid in graph:
    #     for end in graph:
    #         for start in graph:
    #             if graph[start][0] in mid and graph[mid][0] in end:
    #                 graph[start][1][end] = min(graph[start][1][end],graph[start][1][mid]+graph[mid][1][end])

    # for mid in inverse_graph:
    #     for end in inverse_graph:
    #         for start in inverse_graph:
    #             if inverse_graph[start][0] == mid and inverse_graph[mid][0] == end:
    #                 inverse_graph[start][1][end] = min(inverse_graph[start][1][end],inverse_graph[start][1][mid]+inverse_graph[mid][1][end])

    print(graph)
    print(inverse_graph)

    # def solve(start, inverse_graph, graph, end):
    #     for i in range(1,n):
    #         if i ==
    #         graph[start]
    # answer = 0
    # return answer


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
