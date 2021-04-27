class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, val in enumerate(numbers):
            try:
                if target - val in numbers and idx != numbers.index(target - val):
                    return sorted([idx + 1, numbers.index(target - val) + 1])
            except:
                continue


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            right = bisect.bisect_left(numbers, expected, lo=k + 1)
            if right < len(numbers) and numbers[right] + v == target:
                return [k + 1, right + 1]
