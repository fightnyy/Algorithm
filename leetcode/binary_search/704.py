class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursion(left, right):
            mid = (left + right) // 2
            if left > right:
                return -1
            else:
                if nums[mid] > target:
                    return recursion(left, mid - 1)
                elif nums[mid] < target:
                    return recursion(mid + 1, right)
                else:
                    return mid

        return recursion(0, len(nums) - 1)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)

        except ValueError:
            return -1
