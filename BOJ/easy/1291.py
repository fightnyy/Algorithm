if __name__ == "__main__":
    start, end = map(int, input().split())
    per = []
    idx = 1
    result = 0
    while True:
        if len(per) > 2000:
            break
        per.extend([idx] * idx)
        idx += 1
    for i in range(start - 1, end):
        result += per[i]

    print(result)
