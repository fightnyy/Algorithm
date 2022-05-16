"""
# 다익스트라 알고리즘

항상 노드 주변의 최단 경로만을 택하는 대표적인 그리디 알고리즘입니다.
구현도 단순하고 실행속도도 O(ElogV) 이므로 매우 빠릅니다.(여기서 E 는 선분의 개수 V는 점의 개수입니다.)
다익스트라 알고리즘은 노드주변을 탐색할 때 BFS 를 이용하는 대표적인 알고리즘입니다.
최단거리를 찾기 때문에 선분의 가중치가 음수인 경우엔 처리할 수 없습니다.
다익스트라 알고리즘은 정점을 출발 집합에 더할 때, 그 정점까지의 최단거리는 계산이 끝났다는 확실을 갖고 더합니다. 
음수인  선분 가중치에 대해서 사용 할 수 알고리즘은 벨만 포드 알고리즘입니다.
"""


from typing import List
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        point_dict = defaultdict(list)
        dist = defaultdict(int)
        for start, end, cost in times:
            point_dict[start].append([end, cost])
        stack = [(0,k)]
        while stack:
            cost, end_point = heappop(stack)
            if end_point not in dist:
                dist[end_point] = cost
                for e, c in point_dict[end_point]:
                    heappush(stack, (c+cost, e))
        print(dist)
        if len(dist) == n:
            return max(dist.values())
        return -1