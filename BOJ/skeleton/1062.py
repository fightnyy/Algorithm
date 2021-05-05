# from itertools import combinations
# from copy import deepcopy
# import sys

# input = sys.stdin.readline

# """
# a, n, t, i, c
# """


# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     answer = -1
#     tmp_list = []
#     c_list = []
#     for _ in range(N):
#         tmp_list.append(input())
#     AK = K - 5
#     if K < 5:
#         print(0)
#         sys.exit(1)

#     else:
#         for word in tmp_list:
#             c_list += list(word.strip("antic"))

#         c_list = list(set(c_list))
#         for c in combinations(c_list, AK):
#             cnt = 0
#             for v in tmp_list:
#                 if len(v.strip("".join(c) + "antic")) == 0:
#                     cnt += 1
#             answer = max(answer, cnt)
#     print(answer)
import sys
from itertools import combinations
from pdb import set_trace

input = sys.stdin.readline

# ord(): 함수의 괄호 안에 문자열을 입력하면 문자에 해당하는 아스키코드를 반환한다.
def convert(x):
    return ord(x) - ord("a")


def word2square(arr):
    result = 0
    for a in arr:
        result |= 1 << a
    return result


if __name__ == "__main__":
    n, k = map(int, input().split())
    first_word = set([convert(a) for a in ["a", "c", "i", "n", "t"]])
    base = 0
    for i in first_word:
        base |= 1 << i
    arr = [set(map(convert, input().strip())) for _ in range(n)]
    # set_trace()
    squareword = [word2square(a) for a in arr]
    set_trace()

    candidates = set().union(*arr)
    candidates -= first_word
    answer = 0
    if k < 5:
        print(0)
    else:
        if len(candidates) <= (k - 5):
            print(n)
        else:
            for c in combinations(candidates, k - 5):
                t_ans = 0
                temp = base
                for i in c:
                    temp |= 1 << i
                temp ^= (1 << 26) - 1
                for a in squareword:
                    if temp & a == 0:
                        t_ans += 1
                answer = max(answer, t_ans)
            print(answer)
