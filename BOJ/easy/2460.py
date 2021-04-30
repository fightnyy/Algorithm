if __name__ == "__main__":
    result = 0
    tmp = 0
    for _ in range(10):
        cout, cin = map(int, input().split())
        tmp += cin - cout
        result = max(result, tmp)
    print(result)
