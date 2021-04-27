"""
내 코드
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        while g:
            tmp = g.pop(0)
            for t in s:
                if tmp <= t:
                    answer += 1
                    s.remove(t)
                    break
        return answer


"""
그리디
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                g_idx += 1
            s_idx += 1
        return g_idx


"""
이진 검색
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        for i in s:
            idx = bisect_right(g, i)
            if idx > answer:
                answer += 1
        return answer
