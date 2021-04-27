def solve(times, prices):
    dp = [0] * (len(times) + 5)

    for i in range(len(times)):
        dp[i + times[i]] = max(max(dp[: i + 1]) + prices[i], dp[i + times[i]])
    return max(dp[: len(times) + 1])


if __name__ == "__main__":

    num = int(input())
    times = []
    prices = []
    for _ in range(num):
        tmp_t, tmp_p = map(int, input().split())
        times.append(tmp_t)
        prices.append(tmp_p)
    print(solve(times, prices))
