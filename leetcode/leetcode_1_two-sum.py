class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, v in enumerate(nums):
            for jdx, j in enumerate(nums):
                if v + j == target and idx != jdx:
                    return [idx, jdx]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for idx, num in enumerate(nums):
            if target - num in nums_map:
                return [idx, nums_map[target - num]]
            nums_map[num] = idx
