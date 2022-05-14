class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        while not n % 4:
            n /= 4
        if n == 1:
            return True
        return False

            