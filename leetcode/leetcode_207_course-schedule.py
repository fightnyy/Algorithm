class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        traced = set()
        visited = set()
        for x, y in prerequisites:
            graph[x].append(y)

        def _dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            visited.add(i)
            for e in graph[i]:
                if not _dfs(e):
                    return False
            traced.remove(i)
            return True

        for i in list(graph):
            if not _dfs(i):
                return False

        return True
