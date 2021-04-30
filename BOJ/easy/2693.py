if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        tmp = list(map(int, input().split()))
        tmp.sort(reverse=True)
        print(tmp[2])
