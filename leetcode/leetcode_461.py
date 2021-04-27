class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        answer = 0
        if len(x) > len(y):
            pad = len(x) - len(y)
            y = "".join(pad * ["0"] + list(y))
        else:
            pad = len(y) - len(x)
            x = "".join(pad * ["0"] + list(x))

        for i, v in enumerate(x):
            if y[i] != v:
                answer += 1
        return answer


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
