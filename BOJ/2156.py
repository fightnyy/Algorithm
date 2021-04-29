# import sys
# from itertools import combinations
# from pdb import set_trace

# def solve(n_list):
#     n_len = len(n_list)
#     if len(n_list)<= 5:
#         sub = 1
#     else :
#         sub = 2
#     cnds = list(combinations(range(n_len), n_len-sub))
#     for cnd in cnds[:]:
#         cnt = 0
#         for idx in range(1, len(cnd)):
#             if cnd[idx] == cnd[idx-1]+1:
#                 cnt += 1
#             else :
#                 cnt = 0
#             if cnt == 2:
#                 try:
#                     cnds.remove(cnd)
#                 except:
#                     continue
#     result = -float('inf')

#     for c in cnds:
#         tmp = 0
#         for idx in c:
#             tmp += n_list[idx]
#         result = max(result,tmp)
#     return result

# if __name__ == '__main__':
#     input = sys.stdin.readline
#     num = int(input())
#     n_lst = []
#     for _ in range(num):
#         n_lst.append(int(input()))
#     print(solve(n_lst))

import sys
input = sys.stdin.readline


def solve(grapes):
    dp = [0] * (len(grapes))
    if len(grapes) == 1:
        return grapes[0]
    elif len(grapes) == 2:
        return sum(grapes)
    dp[1] = grapes[1]
    dp[2] = grapes[2]+grapes[1]
    for i in range(3, len(grapes)):
        dp[i] = max(dp[i-1], grapes[i] + dp[i-2],
                    grapes[i] + grapes[i-1] + dp[i-3])
    return max(dp)


if __name__ == '__main__':
    num = int(input())
    grapes = [0]
    for _ in range(num):
        grapes.append(int(input()))
    print(solve(grapes))
