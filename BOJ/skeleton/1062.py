"""
A, N, T, I, C
"""
from itertools import combinations

import sys

input = sys.stdin.readline


def convert(characters):
    uni = []
    for c in characters:
        uni.append(ord(c) - ord("a"))

    return uni


if __name__ == "__main__":
    N, K = map(int, input().split())
    word_list = []
    remains = K - 5
    result = 0

    set_of_strips = set()
    for _ in range(N):
        tmp = input().strip()
        word_list.append((tmp))
        set_of_strips = set_of_strips.union(set(tmp.strip("antic")))
    if remains < 0:
        print(0)
        sys.exit(0)

    if len(set_of_strips) <= remains:
        print(N)
        sys.exit(0)
    base_uni = convert(("a", "n", "t", "i", "c"))
    base = 1
    for u in base_uni:
        base |= 1 << u
    uni_list = convert(set_of_strips)
    everychar_uni = (1 << 26) - 1
    n_word_list = []
    for word in word_list:
        tmp = 1
        for c in word:
            tmp |= 1 << (ord(c) - ord("a"))
        n_word_list.append(tmp)
    import pdb

    for cnd in combinations(uni_list, remains):
        # pdb.set_trace()
        t_r = 0
        tmp = base
        for char in cnd:
            tmp |= 1 << char
        tmp ^= everychar_uni
        for str in n_word_list:
            # # if tmp == 66445050:
            # #     import pdb

            #     pdb.set_trace()
            if tmp & str == 0:
                t_r += 1

        result = max(result, t_r)
    print(result)
