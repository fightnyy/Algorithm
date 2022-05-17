class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_cnt = defaultdict(int)
        for char in s:
            char_cnt[char] += 1
        for char in char_cnt:
            if char_cnt[char] == 1:
                return s.index(char)
        return -1
        