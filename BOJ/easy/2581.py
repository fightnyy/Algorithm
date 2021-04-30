import sys

if __name__ == "__main__":
    s = int(input())
    e = int(input())
    sosu = []
    for cnd in range(s, e + 1):
        for di in range(2, cnd):
            if cnd % di == 0:
                break
        else:
            if cnd == 1:
                continue
            sosu.append(cnd)
    import pdb

    # pdb.set_trace()
    if not sosu:
        print(-1)
    else:
        print(sum(sosu))
        print(sorted(sosu)[0])
