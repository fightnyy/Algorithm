class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        dist = collections.defaultdict(int)
        for i in times:
            start, end, taken = i
            graph[start].append((taken, end))

        Q = []
        heapq.heappush(Q, (0, k))  # (걸린시간, 시작노드)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for a, b in graph[node]:
                    alt = time + a
                    heapq.heappush(Q, (alt, b))

        if len(dist) == n:
            return max(dist.values())

        return -1
