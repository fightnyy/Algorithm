class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)
        dp[1] = 1
        dp[2] = 2

        def _recursive(n):
            if dp[n]:
                return dp[n]
            dp[n] = _recursive(n - 1) + _recursive(n - 2)
            return dp[n]

        return _recursive(n)
