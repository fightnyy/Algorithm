class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        graph = collections.defaultdict(list)
        leaves = []
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        for key in graph:
            if len(graph[key]) == 1:
                leaves.append(key)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for key in leaves:
                neighbor = graph[key].pop()
                graph[neighbor].remove(key)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves
