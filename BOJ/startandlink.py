from itertools import combinations
import sys


def solve(num, ablist):
    cnd = list(combinations(range(num), num // 2))
    answer = sys.maxsize
    total = set(range(num))
    for each in cnd:
        last = total - set(each)
        # import pdb;pdb.set_trace()
        tmp1, tmp2 = 0, 0
        for idx in last:
            for jdx in last:
                if idx == jdx:
                    continue
                else:
                    tmp1 += ablist[idx][jdx]
        for idx in each:
            for jdx in each:
                if idx == jdx:
                    continue
                else:
                    tmp2 += ablist[idx][jdx]
        result = abs(tmp2 - tmp1)
        answer = min(answer, result)
    return answer


if __name__ == "__main__":
    num = int(input())
    ablist = []
    for _ in range(num):
        ablist.append(list(map(int, input().split())))
    print(solve(num, ablist))
