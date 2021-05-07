import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    left, right = 0, 0
    tmp_sum = 0
    answer = 0
    min_ = float("inf")
    while True:
        if tmp_sum >= S:
            tmp = right - left
            if min_ > tmp:
                min_ = tmp
            tmp_sum -= numbers[left]
            left += 1
        elif right == N:
            break
        else:  # 합이 더 필요할 때
            tmp_sum += numbers[right]
            right += 1

    if min_ != float("inf"):
        answer = min_
    print(answer)
