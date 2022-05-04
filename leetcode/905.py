from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter, ans = Counter([n for n in nums if n <= k]), 0
        for key in counter:
            ans += min(counter[key], counter[k - key])
        return ans // 2