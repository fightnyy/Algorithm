def solve(strs):

    answer = 0
    for str in strs:
        past = []
        for i in range(1, len(str)):
            if str[i] != str[i - 1]:
                past.append(str[i - 1])
            if str[i] in past:
                break
        else:
            answer += 1
    return answer


if __name__ == "__main__":
    num = int(input())
    strs = []
    for _ in range(num):
        strs.append(input())
    print(solve(strs))
