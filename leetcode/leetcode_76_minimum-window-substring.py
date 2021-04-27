"""
s => ABOCB
t => ABC
"""
from collections import Counter
from pdb import set_trace


def m(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = end = 0

    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1

        # 필요 문자를 모두 찾았으면 최소값을 찾기 위해 왼쪽 포인터 이동
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            set_trace()
            if not end or right - left >= end - start:
                start, end = left, right
            need[s[left]] += 1
            missing += 1
            left += 1
    return s[start:end]


print(m("ADOBECODEBANC", "ABC"))
