class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        for num in digits:
            result = result * 10 + num
        result += 1
        return list(str(result))
        