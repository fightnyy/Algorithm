from typing import List, Dict


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        first = True
        stack = []
        answer = []
        for val in intervals:

            if first:
                stack = val
                first = False
                continue

            if stack[1] >= val[0]:
                if stack[1] <= val[1]:
                    stack[1] = val[1]

            else:
                answer.append(stack)
                stack = val
        if stack not in answer:
            answer.append(stack)
        return answer


"""
책에 나온 솔루션
"""


def merge(self, intervals: List[int]):
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):

        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])

        else:
            merged += (i,)
    return merged


"""
예를들어 i = [1,2,3] 이고 이때
merged += i 를 하게 되면 
merged = [1,2,3]이 된다.

하지만 merged += i, 를 하게 되면
merged = [[1,2,3]] 이 된다.

"""
