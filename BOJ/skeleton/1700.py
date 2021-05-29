import sys

input = sys.stdin.readline


if __name__ == "__main__":
    N, K = map(int, input().split())
    machines = list(map(int, input().split()))
    concent = []
    result = 0
    for key, value in enumerate(machines):
        if value in concent:
            continue

        if len(concent) < N:
            concent.append(value)
            continue
        idxs = []
        flag = False
        idx = 0
        for i in range(N):  # 뭘 빼야하는지 체크
            if concent[i] in machines[key:]:
                idx = machines[key:].index(concent[i])
            else:
                idx = 101
                flag = True
            idxs.append(idx)

            if flag:
                break
        out = idxs.index(max(idxs))
        del concent[out]
        concent.append(value)
        result += 1
    print(result)
