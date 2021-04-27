class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        outs = []
        for i in range(len(nums)):
            outs.append(a)
            a *= nums[i]

        a = 1
        for i in range((len(nums) - 1), -1, -1):
            outs[i] *= a
            a *= nums[i]
        return outs
