from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        output_list = []
        stack.append([0, []])
        while stack:
            idx, subset = stack.pop()
            if idx == len(nums):
                output_list.append(subset)
                continue
            first = subset + [nums[idx]]
            second = subset
            stack.append([idx+1, first])
            stack.append([idx+1, second])
        return output_list


from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output_list = []
        def backtrack(idx, subset):
            if idx == len(nums):
                output_list.append(subset)
                return
            backtrack(idx+1, subset+[nums[idx]])
            backtrack(idx+1, subset)
        backtrack(0, [])
        return output_list