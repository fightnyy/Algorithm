def solve():
    answer = 0
    after = []
    for v in each_many:
        v -= m
        after.append(v)
        answer += 1
    for v in after:
        if v >= 0:
            answer += v // s
            if v % s != 0:
                answer += 1
    return answer


if __name__ == "__main__":
    n_exam = input()
    each_many = list(map(int, input().strip().split()))
    m, s = map(int, input().split())
    print(solve())
