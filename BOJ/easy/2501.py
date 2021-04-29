

if __name__ == "__main__":
    N, C = map(int, input().split())
    divi = []
    for i in range(1,N+1):
        if N % i == 0:
            divi.append(i)

    try :
        print(divi[C-1])
    except :
        print(0)