def fibo(n):
    if 0 == n:
        return 0

    if 0 < n <= 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    n = int(input())
    print(fibo(n))
