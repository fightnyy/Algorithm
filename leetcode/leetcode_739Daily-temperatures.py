class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for idx, val in enumerate(T):
            while stack and val > T[stack[-1]]:

                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)

        return answer
