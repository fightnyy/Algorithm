class Solution:
    """
    2345678이 들어왔다고 생각
    길이가 7개 나와야함
    """

    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        if not digits:
            return []
        i = 0

        def _dfs(index, path):
            if len(path) == len(digits):
                answer.append(path)
                return

            for a in range(index, len(digits)):
                for key in dic[digits[a]]:
                    _dfs(a + 1, path + key)

        _dfs(0, "")

        return answer
