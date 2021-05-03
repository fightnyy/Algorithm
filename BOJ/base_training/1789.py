import sys


if __name__ == "__main__":
    N = int(input())
    tmp = N
    if tmp <= 2:
        print(1)
        sys.exit(0)
    for i in range(1, N):
        tmp -= i
        if tmp <= 0:
            break
    if tmp != 0:
        i -= 1
    print(i)
