class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num = 0
        a = list(jewels)
        for b in list(stones):
            if b in a:
                num += 1
        return num
