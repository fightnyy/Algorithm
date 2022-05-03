class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = -1, -1
        max, min = -float('inf'), float('inf')

        for idx, num in enumerate(nums):
            if max > num:
                start = idx
            elif max < num:
                max = num

        for idx, num in enumerate(nums[::-1]):
            if min < num:
                end = idx
            elif min > num:
                min = num
        if end == -1:
            return 0
        return start - (len(nums) - end - 1) + 1