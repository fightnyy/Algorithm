from collections import Counter
from itertools import combinations
from pprint import pprint
from pdb import set_trace


def solution(orders, course):
    candidate = []
    for order in orders:
        for i in range(2, len(order) + 1):
            for val in sorted(list(combinations(order, i))):
                c_str = "".join(val)
                candidate.append(c_str)
    counter = Counter(candidate)
    pprint(counter)
    counter = sorted(counter.items(), key=lambda x: len(x[0]))
    tmp = []
    for val in counter:
        if len(val) in course and val not in tmp and val[1] >= 2:
            tmp.append(val)
    print(tmp)


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

solution(orders, course)
