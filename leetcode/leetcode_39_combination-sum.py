"""
이게 왜 answer을 인식을 못하지
=> https://dojang.io/mod/page/view.php?id=2366
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def _dfs(value):
            if value == target:
                answer += 1
                return
            elif value > target:
                return

            for c in candidates:
                value += c
                _dfs(value)

        answer = 0
        _dfs(candidates[0])
        return answer


"""
dfs 풀이
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def _dfs(value):
            if sum(value) == target:
                tmp = value[:]
                tmp.sort()
                if tmp in answer:
                    return
                answer.append(tmp)
                return
            elif sum(value) > target:
                return

            for c in candidates:
                value.append(c)
                _dfs(value)
                value.pop()

        _dfs([])
        return answer
