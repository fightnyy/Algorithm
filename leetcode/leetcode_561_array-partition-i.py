class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = [nums[i] for i, _ in enumerate(nums) if i % 2 == 0]
        return sum(answer)


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
