# 내풀이 , 2016초


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        stack = deque([])
        candidate = deque([])
        """
        if all components are negative
        """
        at_least = max(nums)
        for num in nums:
            stack.append(num)
            if sum(stack) <= 0:
                stack.clear()
            else:
                candidate.append(sum(stack))
        candidate.append(at_least)
        return max(candidate)


# 64
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))
        return max(sums)


# 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = -sys.maxsize
        current_sum = 0
        for i in nums:
            current_sum = max(i, i + current_sum)
            sums = max(sums, current_sum)
        return sums
