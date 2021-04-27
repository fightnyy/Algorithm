"""
대부분의 그리디 문제는
우선 순위 큐로 풀이 할 수 있다!
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people:
            heapq.heappush(heap, [-p[0], p[1]])

        result = []
        while heap:
            val = heapq.heappop(heap)
            result.insert(val[1], [-val[0], val[1]])
        return result
