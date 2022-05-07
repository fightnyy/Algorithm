from itertools import combinations
from typing import List
import sys
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return False
        
        stack = []
        third_value = -float('inf')
        for i in range(len(nums) -1, -1, -1) :
            if nums[i] < third_value:
                return True
            while (len(stack) != 0 and stack[-1] < nums[i]):
                third_value = stack.pop()
            stack.append(nums[i])
        return False