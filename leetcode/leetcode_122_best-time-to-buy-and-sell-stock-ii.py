"""
가장 훌륭한 코드
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        for idx in range(len(prices) - 1):
            if prices[idx + 1] > prices[idx]:
                answer += prices[idx + 1] - prices[idx]
        return answer


"""
파이썬 다운 코드
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = sum(
            max(prices[idx + 1] - prices[idx], 0) for idx in range(len(prices) - 1)
        )
        return answer
