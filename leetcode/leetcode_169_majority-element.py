"""
파이썬 다운 풀이
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]


"""
DP 문제 풀이 방식
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            if count[n] == 0:
                count[n] = nums.count(n)
            if count[n] > len(nums) // 2:
                return n


"""
분할정복
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > len(nums) // 2]
