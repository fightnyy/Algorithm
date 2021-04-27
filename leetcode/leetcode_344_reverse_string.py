class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


class Soulution1:
    def reverseString(self, s: List[str]) -> None:
        def reverseString(self, s: List[str]) -> None:
            s[:] = s[::-1]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
