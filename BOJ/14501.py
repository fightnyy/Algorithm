def solve():
    dp = [0] * (size + 1)
    cmax = 0
    for i in range(size):
        cmax = max(dp[i], cmax)
        if i + times[i] > size:
            continue
        dp[i + times[i]] = max(cmax + moneys[i], dp[i + times[i]])
    print(f"dp: {dp}")
    return max(dp)


if __name__ == "__main__":
    size = int(input())
    times = []
    moneys = []
    for _ in range(size):
        time, money = map(int, input().split())
        times.append(time)
        moneys.append(money)
