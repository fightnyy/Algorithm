from itertools import combinations
from copy import deepcopy
import sys


"""
a, n, t, i, c
"""


if __name__ == "__main__":
    N, K = map(int, input().split())
    answer = -1
    w_list = []
    c_list = []
    for _ in range(N):
        w_list.append(input())
    tmp_list = deepcopy(w_list)
    AK = K - 5
    if K < 5:
        print(0)
        sys.exit(1)

    else:
        for word in tmp_list:
            c_list += list(word.strip("antic"))

        c_list = list(set(c_list))
        c_list = combinations(c_list, AK)
        for c in c_list:
            cnt = 0
            for v in tmp_list:
                if len(v.strip("".join(c) + "antic")) == 0:
                    cnt += 1
            answer = max(answer, cnt)
    print(answer)
