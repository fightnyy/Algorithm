class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output_list = []
    
        def backtrack(used_idx, permute):
            
            if len(permute) == len(nums):
                if permute not in output_list:
                    output_list.append(permute)
                return
            for idx, num in enumerate(nums):
                if idx in used_idx:
                    continue
                backtrack(used_idx + [idx], permute + [nums[idx]])
        backtrack([], [])
        return output_list