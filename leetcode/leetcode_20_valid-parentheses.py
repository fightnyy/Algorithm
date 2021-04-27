class Solution:
    def isValid(self, s: str) -> bool:
        answer = []
        table = {")": "(", "}": "{", "]": "["}

        for p in s:
            if p not in table:
                answer.append(p)
            else:
                if not answer or answer.pop() != table[p]:
                    return False

        return len(answer) == 0
