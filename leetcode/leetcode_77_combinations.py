"""
itertools.combinations를 활용한 풀이
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


"""
dfs를 활용한 풀이
설명

e+1을 해줌으로써 (1,1)이 안되고 (1,2)부터 되게하는 것 
왜냐하면 첫번째원소 기준으로는 이미 다 조합이 나왔으니까 그 이후것으로 해야함
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        prev_list = []
        answer = []
        if k == 0:
            return [[a] for a in range(n)]

        def _dfs(start, k):
            if k == 0:
                answer.append(prev_list[:])

            for e in range(start, n + 1):

                prev_list.append(e)
                _dfs(e + 1, k - 1)
                prev_list.pop()

        _dfs(1, k)

        return answer
