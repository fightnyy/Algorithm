class Solution:
    def getSum(self, a: int, b: int) -> int:
        a = str(a)
        b = str(b)
        return eval(f"{a} + {b}")
