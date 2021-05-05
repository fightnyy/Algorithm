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
    # set_trace()

    candidates = set().union(*arr)
    candidates -= first_word
    answer = 0
    if k < 5:
        print(0)
    else:
        if len(candidates) <= (k - 5):
            print(n)
        else:
            import pdb

            for c in combinations(candidates, k - 5):

                t_ans = 0
                temp = base
                for i in c:
                    temp |= 1 << i
                temp ^= (1 << 26) - 1  # 다 있는거랑 xor 없는거만 1 나옴
                for a in squareword:
                    if temp & a == 0:  # 다 커버하면
                        pdb.set_trace()
                        t_ans += 1
                answer = max(answer, t_ans)

    print(answer)
